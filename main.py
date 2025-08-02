#!/usr/bin/env python3
"""
Weekly AI Papers Agent - Free Implementation
Automatically finds, ranks, and publishes top 5 AI papers weekly
"""

import arxiv
import requests
from bs4 import BeautifulSoup
import sqlite3
import smtplib
import time
import random
import re
import os
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from urllib.parse import quote
import json

# Configuration from environment variables
GMAIL_EMAIL = os.getenv('GMAIL_EMAIL')
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')  # Use app password
SUBSTACK_EMAIL = os.getenv('SUBSTACK_EMAIL')
HF_TOKEN = os.getenv('HF_TOKEN', '')  # Hugging Face token (optional)

def setup_database():
    """Initialize SQLite database for tracking published papers"""
    conn = sqlite3.connect('published_papers.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS published_papers (
            arxiv_id TEXT PRIMARY KEY,
            title TEXT,
            published_date DATE,
            week_published DATE,
            score INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def is_already_published(arxiv_id):
    """Check if paper was already published"""
    conn = sqlite3.connect('published_papers.db')
    cursor = conn.execute(
        "SELECT COUNT(*) FROM published_papers WHERE arxiv_id = ?",
        (arxiv_id,)
    )
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0

def mark_as_published(arxiv_id, title, score=0):
    """Mark paper as published"""
    conn = sqlite3.connect('published_papers.db')
    conn.execute(
        "INSERT OR REPLACE INTO published_papers VALUES (?, ?, ?, ?, ?)",
        (arxiv_id, title, datetime.now().date(), datetime.now().date(), score)
    )
    conn.commit()
    conn.close()

def fetch_recent_papers():
    """Get recent papers from arXiv"""
    print("🔍 Fetching papers from arXiv...")
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    
    # Search multiple AI categories
    categories = ["cs.AI", "cs.LG", "cs.CV", "cs.CL", "cs.NE", "stat.ML"]
    all_papers = []
    
    for category in categories:
        try:
            search = arxiv.Search(
                query=f"cat:{category}",
                max_results=50,
                sort_by=arxiv.SortCriterion.SubmittedDate
            )
            
            for result in search.results():
                if result.published.date() >= start_date.date():
                    arxiv_id = result.entry_id.split('/')[-1].split('v')[0]  # Clean ID
                    
                    paper = {
                        'title': result.title.strip(),
                        'authors': [author.name for author in result.authors],
                        'abstract': result.summary.strip(),
                        'url': result.entry_id,
                        'pdf_url': result.pdf_url,
                        'published': result.published,
                        'arxiv_id': arxiv_id,
                        'category': category
                    }
                    all_papers.append(paper)
                    
        except Exception as e:
            print(f"⚠️ Error fetching from {category}: {e}")
            continue
            
        time.sleep(1)  # Be respectful to arXiv
    
    # Remove duplicates by arxiv_id
    seen_ids = set()
    unique_papers = []
    for paper in all_papers:
        if paper['arxiv_id'] not in seen_ids:
            seen_ids.add(paper['arxiv_id'])
            unique_papers.append(paper)
    
    print(f"📚 Found {len(unique_papers)} recent papers")
    return unique_papers

def scrape_twitter_mentions(paper_title, arxiv_id):
    """Scrape Twitter mentions using nitter.net"""
    
    # Try multiple search terms
    search_terms = [
        paper_title[:50],
        arxiv_id,
        f"arxiv:{arxiv_id}"
    ]
    
    total_mentions = 0
    total_engagement = 0
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    for term in search_terms:
        try:
            search_query = quote(f'"{term}"')
            url = f"https://nitter.net/search?q={search_query}"
            
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Count tweets
                tweets = soup.find_all('div', class_='tweet-content')
                mentions = len(tweets)
                total_mentions += mentions
                
                # Count engagement metrics
                for stat_div in soup.find_all('div', class_='tweet-stat'):
                    stat_text = stat_div.get_text().strip()
                    numbers = re.findall(r'[\d,]+', stat_text)
                    for num in numbers:
                        try:
                            total_engagement += int(num.replace(',', ''))
                        except:
                            continue
                            
            time.sleep(random.uniform(2, 4))
            
        except Exception as e:
            print(f"⚠️ Twitter scraping error for '{term}': {e}")
            continue
    
    return {
        'mentions': total_mentions,
        'engagement': min(total_engagement, 10000)  # Cap to prevent outliers
    }

def scrape_reddit_mentions(paper_title):
    """Scrape Reddit mentions from relevant subreddits"""
    
    subreddits = ['MachineLearning', 'artificial', 'deeplearning', 'compsci', 'singularity']
    total_score = 0
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; AI-Paper-Bot/1.0)'
    }
    
    for subreddit in subreddits:
        try:
            # Search for paper title
            search_query = quote(paper_title[:40])
            url = f"https://old.reddit.com/r/{subreddit}/search.json?q={search_query}&sort=new&restrict_sr=1&limit=10"
            
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                
                for post in data.get('data', {}).get('children', []):
                    post_data = post.get('data', {})
                    score = post_data.get('score', 0)
                    comments = post_data.get('num_comments', 0)
                    
                    # Weight by score and comments
                    total_score += score + (comments * 2)
                    
            time.sleep(random.uniform(2, 3))
            
        except Exception as e:
            print(f"⚠️ Reddit scraping error for r/{subreddit}: {e}")
            continue
    
    return min(total_score, 5000)  # Cap to prevent outliers

def scrape_hackernews_mentions(paper_title):
    """Scrape Hacker News mentions using Algolia API"""
    
    try:
        search_query = quote(paper_title[:40])
        url = f"https://hn.algolia.com/api/v1/search?query={search_query}&tags=story&hitsPerPage=20"
        
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            
            total_points = 0
            for hit in data.get('hits', []):
                points = hit.get('points', 0)
                comments = hit.get('num_comments', 0)
                
                # Weight by points and comments
                total_points += points + (comments * 3)
            
            return min(total_points, 3000)  # Cap to prevent outliers
            
    except Exception as e:
        print(f"⚠️ HN scraping error: {e}")
    
    return 0

def scrape_github_activity(paper_title, arxiv_id):
    """Check GitHub for implementations"""
    
    search_terms = [paper_title[:30], arxiv_id]
    total_stars = 0
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; AI-Paper-Bot/1.0)'
    }
    
    for term in search_terms:
        try:
            search_url = f"https://github.com/search?q={quote(term)}&type=repositories"
            
            response = requests.get(search_url, headers=headers, timeout=15)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Look for star counts
                for link in soup.find_all('a', href=re.compile(r'/stargazers$')):
                    star_text = link.get_text().strip()
                    
                    # Parse star count (handle "1.2k" format)
                    if 'k' in star_text.lower():
                        try:
                            stars = int(float(star_text.lower().replace('k', '')) * 1000)
                        except:
                            stars = 0
                    elif star_text.replace(',', '').isdigit():
                        stars = int(star_text.replace(',', ''))
                    else:
                        stars = 0
                    
                    total_stars += stars
                    
            time.sleep(random.uniform(3, 5))  # Be extra respectful to GitHub
            
        except Exception as e:
            print(f"⚠️ GitHub scraping error: {e}")
            continue
    
    return min(total_stars, 2000)  # Cap to prevent outliers

def generate_summary_huggingface(paper):
    """Generate summary using Hugging Face API"""
    
    if not HF_TOKEN:
        return None
        
    try:
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}
        
        # Prepare text for summarization
        text = f"{paper['title']}. {paper['abstract']}"[:1000]
        
        payload = {
            "inputs": text,
            "parameters": {
                "max_length": 250,
                "min_length": 100,
                "do_sample": False
            }
        }
        
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get('summary_text', '')
                
    except Exception as e:
        print(f"⚠️ HuggingFace API error: {e}")
    
    return None

def generate_rule_based_summary(paper):
    """Generate summary using rule-based approach"""
    
    title = paper['title']
    abstract = paper['abstract']
    
    # Split abstract into sentences
    sentences = [s.strip() for s in abstract.split('.') if len(s.strip()) > 20]
    
    # Find key sentences with important keywords
    key_keywords = [
        'propose', 'introduce', 'present', 'develop', 'novel', 'new',
        'method', 'approach', 'algorithm', 'model', 'framework',
        'achieve', 'improve', 'outperform', 'demonstrate', 'show',
        'results', 'performance', 'accuracy', 'efficiency'
    ]
    
    key_sentences = []
    method_sentences = []
    result_sentences = []
    
    for sentence in sentences:
        sentence_lower = sentence.lower()
        
        # Categorize sentences
        if any(word in sentence_lower for word in ['propose', 'introduce', 'present', 'novel', 'new']):
            key_sentences.append(sentence)
        elif any(word in sentence_lower for word in ['method', 'approach', 'algorithm', 'model']):
            method_sentences.append(sentence)
        elif any(word in sentence_lower for word in ['results', 'achieve', 'outperform', 'demonstrate']):
            result_sentences.append(sentence)
    
    # Build summary
    summary_parts = []
    
    # Add key contribution
    if key_sentences:
        summary_parts.append(key_sentences[0])
    elif sentences:
        summary_parts.append(sentences[0])
    
    # Add methodology
    if method_sentences:
        summary_parts.append(method_sentences[0])
    elif len(sentences) > 1:
        summary_parts.append(sentences[1])
    
    # Add results
    if result_sentences:
        summary_parts.append(result_sentences[0])
    elif len(sentences) > 2:
        summary_parts.append(sentences[-1])
    
    summary = '. '.join(summary_parts) + '.'
    
    # Ensure reasonable length
    if len(summary) > 500:
        summary = summary[:497] + '...'
    
    return summary

def generate_summary(paper):
    """Generate summary with fallback options"""
    
    # Try HuggingFace first
    hf_summary = generate_summary_huggingface(paper)
    if hf_summary and len(hf_summary) > 50:
        return hf_summary
    
    # Fallback to rule-based
    return generate_rule_based_summary(paper)

def calculate_paper_score(paper):
    """Calculate comprehensive score for paper"""
    
    print(f"  📊 Scoring: {paper['title'][:50]}...")
    
    # Get social media metrics
    twitter_data = scrape_twitter_mentions(paper['title'], paper['arxiv_id'])
    reddit_score = scrape_reddit_mentions(paper['title'])
    hn_score = scrape_hackernews_mentions(paper['title'])
    github_stars = scrape_github_activity(paper['title'], paper['arxiv_id'])
    
    # Calculate social media score
    social_score = (
        twitter_data['mentions'] * 5 +
        twitter_data['engagement'] * 0.1 +
        reddit_score * 2 +
        hn_score * 3 +
        github_stars * 0.8
    )
    
    # Author count bonus (more authors often means more established work)
    author_score = min(len(paper['authors']) * 3, 30)
    
    # Recency boost (newer papers get higher scores)
    days_old = (datetime.now() - paper['published'].replace(tzinfo=None)).days
    recency_score = max(0, 7 - days_old) * 10
    
    # Title/abstract keyword analysis
    impact_keywords = [
        'breakthrough', 'novel', 'state-of-the-art', 'sota', 'efficient', 'robust',
        'transformer', 'attention', 'neural', 'deep learning', 'machine learning',
        'gpt', 'llm', 'language model', 'bert', 'vision', 'multimodal',
        'reinforcement', 'generative', 'diffusion', 'gan', 'vae'
    ]
    
    text_to_check = (paper['title'] + ' ' + paper['abstract']).lower()
    keyword_score = sum(10 for keyword in impact_keywords if keyword in text_to_check)
    
    # Category bonus (some categories are more popular)
    category_bonuses = {
        'cs.AI': 10,
        'cs.LG': 15,
        'cs.CV': 12,
        'cs.CL': 13,
        'cs.NE': 8,
        'stat.ML': 10
    }
    category_score = category_bonuses.get(paper.get('category', ''), 5)
    
    # Calculate total score
    total_score = (
        social_score +
        author_score +
        recency_score +
        keyword_score +
        category_score
    )
    
    # Store breakdown for debugging
    paper['score_breakdown'] = {
        'social': int(social_score),
        'authors': author_score,
        'recency': recency_score,
        'keywords': keyword_score,
        'category': category_score,
        'total': int(total_score)
    }
    
    print(f"    Score: {int(total_score)} (social: {int(social_score)}, keywords: {keyword_score})")
    
    return total_score

def format_email_post(papers):
    """Format papers into HTML email"""
    
    current_date = datetime.now().strftime('%B %d, %Y')
    
    html = f"""
    <html>
    <body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto;">
        
        <div style="text-align: center; padding: 30px 0; border-bottom: 2px solid #007acc;">
            <h1 style="color: #007acc; margin: 0; font-size: 2.5em;">🤖 Top 5 AI Papers This Week</h1>
            <p style="color: #666; font-size: 1.2em; margin: 10px 0;"><em>Week of {current_date}</em></p>
        </div>
        
        <div style="padding: 20px 0;">
            <p style="font-size: 1.1em; color: #444;">
                Here are the most discussed and impactful AI papers from the past week, 
                ranked by social media engagement, academic interest, and community buzz across 
                Twitter, Reddit, Hacker News, and GitHub:
            </p>
        </div>
    """
    
    for i, paper in enumerate(papers, 1):
        # Truncate long author lists
        authors_display = ', '.join(paper['authors'][:4])
        if len(paper['authors']) > 4:
            authors_display += f" (+{len(paper['authors']) - 4} more)"
        
        # Format publication date
        pub_date = paper['published'].strftime('%B %d, %Y')
        
        # Create score badge
        score = paper['score_breakdown']['total']
        if score > 200:
            badge_color = "#28a745"  # Green
            badge_text = "🔥 Hot"
        elif score > 100:
            badge_color = "#ffc107"  # Yellow
            badge_text = "⭐ Trending"
        else:
            badge_color = "#6c757d"  # Gray
            badge_text = "📈 Rising"
        
        html += f"""
        <div style="margin: 40px 0; border: 1px solid #e0e0e0; border-radius: 10px; overflow: hidden;">
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px;">
                    <h2 style="margin: 0; font-size: 1.8em;">#{i}</h2>
                    <span style="background: {badge_color}; padding: 5px 10px; border-radius: 15px; font-size: 0.9em; font-weight: bold;">
                        {badge_text}
                    </span>
                </div>
                <h3 style="margin: 0; font-size: 1.4em; line-height: 1.3;">{paper['title']}</h3>
            </div>
            
            <div style="padding: 25px;">
                <div style="margin-bottom: 20px;">
                    <p style="margin: 5px 0;"><strong>📝 Authors:</strong> {authors_display}</p>
                    <p style="margin: 5px 0;"><strong>📅 Published:</strong> {pub_date}</p>
                    <p style="margin: 5px 0;">
                        <strong>🔗 Links:</strong> 
                        <a href="{paper['url']}" style="color: #007acc; text-decoration: none; margin-right: 15px;">arXiv Page</a>
                        <a href="{paper['pdf_url']}" style="color: #dc3545; text-decoration: none;">📄 PDF</a>
                    </p>
                </div>
                
                <div style="background-color: #f8f9fa; padding: 20px; border-left: 4px solid #007acc; border-radius: 0 5px 5px 0; margin: 20px 0;">
                    <h4 style="margin-top: 0; color: #007acc;">📋 Summary</h4>
                    <p style="margin-bottom: 0; line-height: 1.7;">{paper['summary']}</p>
                </div>
                
                <div style="background-color: #e8f4fd; padding: 15px; border-radius: 5px; font-size: 0.95em; color: #0066cc;">
                    <strong>🔥 Why it's trending:</strong> 
                    Buzz Score: {score} • 
                    Social mentions: {paper['score_breakdown']['social']} • 
                    Keyword relevance: {paper['score_breakdown']['keywords']} • 
                    Category: {paper.get('category', 'N/A')}
                </div>
            </div>
        </div>
        """
    
    html += """
        <div style="text-align: center; padding: 30px 0; border-top: 2px solid #e0e0e0; margin-top: 40px; color: #666;">
            <p style="font-style: italic; margin-bottom: 10px;">
                🤖 This weekly digest is automatically generated by analyzing discussions across 
                Twitter, Reddit, Hacker News, and GitHub.
            </p>
            <p style="font-style: italic; margin: 0;">
                Have suggestions or found an amazing paper we missed? Reply to this email!
            </p>
            <p style="margin-top: 20px; font-size: 0.9em; color: #999;">
                Built with ❤️ using arXiv, web scraping, and free APIs
            </p>
        </div>
    
    </body>
    </html>
    """
    
    return html

def publish_to_substack(top_papers):
    """Publish to Substack via email"""
    
    if not all([GMAIL_EMAIL, GMAIL_PASSWORD, SUBSTACK_EMAIL]):
        print("❌ Missing email configuration. Please set GMAIL_EMAIL, GMAIL_PASSWORD, and SUBSTACK_EMAIL")
        return False
    
    try:
        # Create email
        message = MIMEMultipart("alternative")
        message["Subject"] = f"🤖 Top 5 AI Papers - Week of {datetime.now().strftime('%B %d, %Y')}"
        message["From"] = GMAIL_EMAIL
        message["To"] = SUBSTACK_EMAIL
        
        # Create HTML content
        html_content = format_email_post(top_papers)
        html_part = MIMEText(html_content, "html")
        message.attach(html_part)
        
        # Send email
        print("📧 Sending email to Substack...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_EMAIL, GMAIL_PASSWORD)
            server.sendmail(GMAIL_EMAIL, SUBSTACK_EMAIL, message.as_string())
        
        print("✅ Email sent successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False

def main():
    """Main execution function"""
    
    print("🚀 Starting Weekly AI Papers Agent...")
    print(f"📅 Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Initialize database
    setup_database()
    
    # Fetch recent papers
    papers = fetch_recent_papers()
    
    if not papers:
        print("❌ No papers found. Exiting.")
        return
    
    # Filter out already published papers
    new_papers = [p for p in papers if not is_already_published(p['arxiv_id'])]
    
    print(f"📊 Found {len(new_papers)} new papers to analyze...")
    
    if len(new_papers) < 5:
        print("⚠️ Less than 5 new papers found. Consider adjusting date range or categories.")
    
    # Score papers (limit to reasonable number for processing time)
    scored_papers = []
    papers_to_process = new_papers[:min(100, len(new_papers))]
    
    print("🔍 Analyzing papers and calculating scores...")
    
    for i, paper in enumerate(papers_to_process):
        print(f"\n📄 Paper {i+1}/{len(papers_to_process)}")
        
        try:
            score = calculate_paper_score(paper)
            paper['total_score'] = score
            scored_papers.append(paper)
            
            # Random delay to be respectful
            time.sleep(random.uniform(1, 3))
            
        except Exception as e:
            print(f"⚠️ Error processing paper: {e}")
            continue
    
    if not scored_papers:
        print("❌ No papers could be scored. Exiting.")
        return
    
    # Sort by score and get top 5
    top_papers = sorted(scored_papers, key=lambda x: x['total_score'], reverse=True)[:5]
    
    print(f"\n🏆 Top 5 papers selected:")
    for i, paper in enumerate(top_papers, 1):
        print(f"{i}. {paper['title'][:80]}... (Score: {int(paper['total_score'])})")
    
    # Generate summaries
    print("\n✍️ Generating summaries...")
    for i, paper in enumerate(top_papers):
        print(f"  Summarizing paper {i+1}/5...")
        paper['summary'] = generate_summary(paper)
        time.sleep(1)  # Brief pause between summary generations
    
    # Publish to Substack
    print("\n📤 Publishing to Substack...")
    success = publish_to_substack(top_papers)
    
    if success:
        # Mark papers as published
        for paper in top_papers:
            mark_as_published(paper['arxiv_id'], paper['title'], int(paper['total_score']))
        
        print("✅ Weekly AI papers published successfully!")
        
        # Print final summary
        print(f"\n📋 Published papers summary:")
        for i, paper in enumerate(top_papers, 1):
            breakdown = paper['score_breakdown']
            print(f"{i}. {paper['title'][:60]}...")
            print(f"   Score: {breakdown['total']} (Social: {breakdown['social']}, Keywords: {breakdown['keywords']})")
        
    else:
        print("❌ Failed to publish papers.")
    
    print(f"\n🎯 Agent completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
