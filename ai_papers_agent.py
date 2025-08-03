#!/usr/bin/env python3
"""
AI Papers Agent - Social Media Engagement Ranking
Finds the top 5 AI papers with highest social media engagement in the last 7 days
"""

import arxiv
import requests
import json
import sqlite3
import smtplib
import re
import time
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
from urllib.parse import quote
import os
from typing import List, Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SocialMediaTracker:
    """Tracks social media engagement for papers"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def search_twitter_mentions(self, paper_title: str, arxiv_id: str) -> Dict[str, int]:
        """Search for Twitter mentions using nitter instances"""
        mentions_data = {'mentions': 0, 'replies': 0, 'likes': 0}
        
        # Try multiple nitter instances
        nitter_instances = [
            'https://nitter.net',
            'https://nitter.1d4.us',
            'https://nitter.kavin.rocks'
        ]
        
        search_terms = [
            f'"{paper_title}"',
            f'arxiv.org/abs/{arxiv_id}',
            f'{arxiv_id}'
        ]
        
        for instance in nitter_instances:
            try:
                for term in search_terms:
                    mentions = self._scrape_twitter_data(instance, term)
                    mentions_data['mentions'] += mentions['mentions']
                    mentions_data['replies'] += mentions['replies']
                    mentions_data['likes'] += mentions['likes']
                    time.sleep(1)  # Rate limiting
                break  # If successful, don't try other instances
            except Exception as e:
                logger.warning(f"Failed to scrape {instance}: {e}")
                continue
                
        return mentions_data
    
    def _scrape_twitter_data(self, instance: str, search_term: str) -> Dict[str, int]:
        """Scrape Twitter data from nitter instance"""
        try:
            url = f"{instance}/search?f=tweets&q={quote(search_term)}&since=7d"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            tweets = soup.find_all('div', class_='timeline-item')
            
            total_mentions = len(tweets)
            total_replies = 0
            total_likes = 0
            
            for tweet in tweets:
                # Extract reply count
                reply_elem = tweet.find('div', class_='icon-comment')
                if reply_elem and reply_elem.parent:
                    reply_text = reply_elem.parent.get_text(strip=True)
                    reply_count = self._extract_number(reply_text)
                    total_replies += reply_count
                
                # Extract like count
                like_elem = tweet.find('div', class_='icon-heart')
                if like_elem and like_elem.parent:
                    like_text = like_elem.parent.get_text(strip=True)
                    like_count = self._extract_number(like_text)
                    total_likes += like_count
            
            return {
                'mentions': total_mentions,
                'replies': total_replies,
                'likes': total_likes
            }
            
        except Exception as e:
            logger.error(f"Error scraping Twitter data: {e}")
            return {'mentions': 0, 'replies': 0, 'likes': 0}
    
    def search_reddit_mentions(self, paper_title: str, arxiv_id: str) -> Dict[str, int]:
        """Search for Reddit mentions"""
        mentions_data = {'mentions': 0, 'replies': 0, 'likes': 0}
        
        try:
            # Search Reddit using pushshift API alternative or direct Reddit
            search_terms = [paper_title, arxiv_id]
            
            for term in search_terms:
                url = f"https://www.reddit.com/search.json?q={quote(term)}&sort=new&t=week"
                response = self.session.get(url, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    posts = data.get('data', {}).get('children', [])
                    
                    for post in posts:
                        post_data = post.get('data', {})
                        mentions_data['mentions'] += 1
                        mentions_data['likes'] += post_data.get('ups', 0)
                        mentions_data['replies'] += post_data.get('num_comments', 0)
                
                time.sleep(1)  # Rate limiting
                
        except Exception as e:
            logger.error(f"Error searching Reddit: {e}")
            
        return mentions_data
    
    def search_hackernews_mentions(self, paper_title: str, arxiv_id: str) -> Dict[str, int]:
        """Search for Hacker News mentions using Algolia API"""
        mentions_data = {'mentions': 0, 'replies': 0, 'likes': 0}
        
        try:
            # Get timestamp for 7 days ago
            week_ago = int((datetime.now() - timedelta(days=7)).timestamp())
            
            search_terms = [paper_title, arxiv_id]
            
            for term in search_terms:
                url = "https://hn.algolia.com/api/v1/search"
                params = {
                    'query': term,
                    'numericFilters': f'created_at_i>{week_ago}',
                    'hitsPerPage': 100
                }
                
                response = self.session.get(url, params=params, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    hits = data.get('hits', [])
                    
                    for hit in hits:
                        mentions_data['mentions'] += 1
                        mentions_data['likes'] += hit.get('points', 0)
                        mentions_data['replies'] += hit.get('num_comments', 0)
                
                time.sleep(1)  # Rate limiting
                
        except Exception as e:
            logger.error(f"Error searching Hacker News: {e}")
            
        return mentions_data
    
    def search_github_mentions(self, paper_title: str, arxiv_id: str) -> Dict[str, int]:
        """Search for GitHub mentions"""
        mentions_data = {'mentions': 0, 'replies': 0, 'likes': 0}
        
        try:
            # Search GitHub using their API
            search_terms = [f'"{paper_title}"', arxiv_id]
            
            for term in search_terms:
                url = f"https://api.github.com/search/repositories"
                params = {
                    'q': f'{term} created:>{(datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")}',
                    'per_page': 100
                }
                
                response = self.session.get(url, params=params, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    items = data.get('items', [])
                    
                    for item in items:
                        mentions_data['mentions'] += 1
                        mentions_data['likes'] += item.get('stargazers_count', 0)
                        mentions_data['replies'] += item.get('forks_count', 0)
                
                time.sleep(1)  # Rate limiting
                
        except Exception as e:
            logger.error(f"Error searching GitHub: {e}")
            
        return mentions_data
    
    def _extract_number(self, text: str) -> int:
        """Extract number from text, handling K/M suffixes"""
        if not text:
            return 0
            
        # Remove non-numeric characters except K, M, and decimal points
        clean_text = re.sub(r'[^\d.KM]', '', text.upper())
        
        if 'K' in clean_text:
            number = float(clean_text.replace('K', '')) * 1000
        elif 'M' in clean_text:
            number = float(clean_text.replace('M', '')) * 1000000
        else:
            try:
                number = float(clean_text)
            except:
                number = 0
                
        return int(number)

class AIPapersAgent:
    """Main agent class for finding and ranking AI papers"""
    
    def __init__(self):
        self.social_tracker = SocialMediaTracker()
        self.db_path = 'previous_papers.db'
        self.json_path = 'previous_papers.json'
        self.init_database()
        
        # ArXiv categories to search
        self.categories = [
            "cs.AI",    # Artificial Intelligence
            "cs.LG",    # Machine Learning
            "cs.CV",    # Computer Vision
            "cs.CL",    # Computation and Language
            "cs.NE",    # Neural and Evolutionary Computing
            "stat.ML"   # Machine Learning (Statistics)
        ]
    
    def init_database(self):
        """Initialize SQLite database for tracking papers"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS processed_papers (
                arxiv_id TEXT PRIMARY KEY,
                title TEXT,
                date_processed TEXT,
                social_score REAL
            )
        ''')
        
        conn.commit()
        conn.close()
        
        # Migrate from JSON if exists
        self.migrate_from_json()
    
    def migrate_from_json(self):
        """Migrate existing JSON data to SQLite"""
        if os.path.exists(self.json_path):
            try:
                with open(self.json_path, 'r') as f:
                    data = json.load(f)
                
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                
                for paper in data.get('processed_papers', []):
                    cursor.execute('''
                        INSERT OR IGNORE INTO processed_papers 
                        (arxiv_id, title, date_processed, social_score)
                        VALUES (?, ?, ?, ?)
                    ''', (
                        paper.get('arxiv_id', ''),
                        paper.get('title', ''),
                        paper.get('date_processed', ''),
                        paper.get('social_score', 0)
                    ))
                
                conn.commit()
                conn.close()
                
                logger.info("Successfully migrated JSON data to SQLite")
                
            except Exception as e:
                logger.error(f"Error migrating from JSON: {e}")
    
    def is_paper_processed(self, arxiv_id: str) -> bool:
        """Check if paper has been processed before"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT arxiv_id FROM processed_papers WHERE arxiv_id = ?', (arxiv_id,))
        result = cursor.fetchone()
        
        conn.close()
        return result is not None
    
    def add_processed_paper(self, arxiv_id: str, title: str, social_score: float):
        """Add paper to processed list"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO processed_papers 
            (arxiv_id, title, date_processed, social_score)
            VALUES (?, ?, ?, ?)
        ''', (arxiv_id, title, datetime.now().isoformat(), social_score))
        
        conn.commit()
        conn.close()
    
    def fetch_recent_papers(self, max_results: int = 200) -> List[arxiv.Result]:
        """Fetch recent papers from arXiv"""
        papers = []
        
        for category in self.categories:
            try:
                logger.info(f"Fetching papers from category: {category}")
                
                search = arxiv.Search(
                    query=f"cat:{category}",
                    max_results=max_results // len(self.categories),
                    sort_by=arxiv.SortCriterion.SubmittedDate
                )
                
                category_papers = list(search.results())
                papers.extend(category_papers)
                
                logger.info(f"Found {len(category_papers)} papers in {category}")
                time.sleep(1)  # Rate limiting
                
            except Exception as e:
                logger.error(f"Error fetching papers from {category}: {e}")
        
        logger.info(f"Total papers fetched: {len(papers)}")
        return papers
    
    def calculate_social_score(self, paper: arxiv.Result) -> float:
        """Calculate social media engagement score for a paper"""
        logger.info(f"Calculating social score for: {paper.title[:50]}...")
        
        # Get social media data
        twitter_data = self.social_tracker.search_twitter_mentions(paper.title, paper.get_short_id())
        reddit_data = self.social_tracker.search_reddit_mentions(paper.title, paper.get_short_id())
        hn_data = self.social_tracker.search_hackernews_mentions(paper.title, paper.get_short_id())
        github_data = self.social_tracker.search_github_mentions(paper.title, paper.get_short_id())
        
        # Calculate weighted score based on engagement metrics
        # Focus on mentions, replies, and likes from last 7 days
        score = (
            # Twitter engagement (weight: 3.0)
            (twitter_data['mentions'] * 10 + 
             twitter_data['replies'] * 5 + 
             twitter_data['likes'] * 2) * 3.0 +
            
            # Reddit engagement (weight: 2.5)
            (reddit_data['mentions'] * 15 + 
             reddit_data['replies'] * 3 + 
             reddit_data['likes'] * 1) * 2.5 +
            
            # Hacker News engagement (weight: 2.0)
            (hn_data['mentions'] * 20 + 
             hn_data['replies'] * 4 + 
             hn_data['likes'] * 2) * 2.0 +
            
            # GitHub engagement (weight: 1.5)
            (github_data['mentions'] * 25 + 
             github_data['replies'] * 5 + 
             github_data['likes'] * 1) * 1.5
        )
        
        total_engagement = (
            twitter_data['mentions'] + twitter_data['replies'] + twitter_data['likes'] +
            reddit_data['mentions'] + reddit_data['replies'] + reddit_data['likes'] +
            hn_data['mentions'] + hn_data['replies'] + hn_data['likes'] +
            github_data['mentions'] + github_data['replies'] + github_data['likes']
        )
        
        logger.info(f"Social score: {score:.2f} (Total engagement: {total_engagement})")
        
        return score
    
    def rank_papers(self, papers: List[arxiv.Result]) -> List[tuple]:
        """Rank papers by social media engagement"""
        logger.info("Ranking papers by social media engagement...")
        
        ranked_papers = []
        
        for paper in papers:
            # Skip if already processed
            if self.is_paper_processed(paper.get_short_id()):
                logger.info(f"Skipping already processed paper: {paper.get_short_id()}")
                continue
            
            try:
                social_score = self.calculate_social_score(paper)
                
                # Only include papers with some social engagement
                if social_score > 0:
                    ranked_papers.append((paper, social_score))
                    logger.info(f"Added paper with score {social_score:.2f}: {paper.title[:50]}...")
                
            except Exception as e:
                logger.error(f"Error processing paper {paper.get_short_id()}: {e}")
        
        # Sort by social score (descending)
        ranked_papers.sort(key=lambda x: x[1], reverse=True)
        
        logger.info(f"Ranked {len(ranked_papers)} papers with social engagement")
        
        return ranked_papers
    
    def generate_summary(self, paper: arxiv.Result) -> str:
        """Generate a summary for the paper"""
        try:
            # Simple extractive summary from abstract
            abstract = paper.summary
            sentences = abstract.split('. ')
            
            # Take first 2-3 sentences or up to 200 words
            summary_sentences = []
            word_count = 0
            
            for sentence in sentences:
                words_in_sentence = len(sentence.split())
                if word_count + words_in_sentence > 200:
                    break
                summary_sentences.append(sentence)
                word_count += words_in_sentence
                
                if len(summary_sentences) >= 3:
                    break
            
            summary = '. '.join(summary_sentences)
            if not summary.endswith('.'):
                summary += '.'
                
            return summary
            
        except Exception as e:
            logger.error(f"Error generating summary: {e}")
            return paper.summary[:200] + "..."
    
    def format_email_content(self, top_papers: List[tuple]) -> str:
        """Format papers into email content"""
        current_date = datetime.now().strftime("%B %d, %Y")
        
        content = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
        
        <h1 style="color: #2c3e50;">🤖 Top 5 AI Papers This Week</h1>
        <p style="color: #7f8c8d; font-size: 16px;">Week of {current_date}</p>
        <p style="color: #7f8c8d;">Papers ranked by social media engagement (mentions, replies, likes) in the last 7 days</p>
        
        <hr style="border: 1px solid #ecf0f1; margin: 30px 0;">
        """
        
        for i, (paper, score) in enumerate(top_papers, 1):
            # Format author names
            authors = ", ".join([author.name for author in paper.authors[:3]])
            if len(paper.authors) > 3:
                authors += ", et al."
            
            # Generate emoji based on ranking
            emoji = ["🥇", "🥈", "🥉", "🏅", "⭐"][i-1] if i <= 5 else "📄"
            
            summary = self.generate_summary(paper)
            
            content += f"""
            <div style="margin: 30px 0; padding: 20px; border-left: 4px solid #3498db; background-color: #f8f9fa;">
                <h2 style="color: #2c3e50; margin-bottom: 10px;">
                    {emoji} #{i}. {paper.title}
                </h2>
                
                <p style="color: #7f8c8d; margin: 5px 0;">
                    <strong>Authors:</strong> {authors}
                </p>
                
                <p style="color: #e74c3c; margin: 5px 0; font-weight: bold;">
                    🔥 Social Engagement Score: {score:.1f}
                </p>
                
                <p style="color: #34495e; margin: 15px 0;">
                    {summary}
                </p>
                
                <p style="margin: 10px 0;">
                    <a href="{paper.entry_id}" style="color: #3498db; text-decoration: none;">
                        📖 Read Full Paper
                    </a> | 
                    <a href="{paper.pdf_url}" style="color: #3498db; text-decoration: none;">
                        📄 Download PDF
                    </a>
                </p>
            </div>
            """
        
        content += """
        <hr style="border: 1px solid #ecf0f1; margin: 30px 0;">
        
        <div style="text-align: center; color: #7f8c8d; font-size: 14px;">
            <p>This digest was automatically generated by AI Papers Agent</p>
            <p>Tracking social media engagement across Twitter, Reddit, Hacker News, and GitHub</p>
            <p>🤖 Built with ❤️ for the AI research community</p>
        </div>
        
        </body>
        </html>
        """
        
        return content
    
    def send_email(self, content: str):
        """Send email to Substack"""
        try:
            gmail_email = os.getenv('GMAIL_EMAIL')
            gmail_password = os.getenv('GMAIL_PASSWORD')
            substack_email = os.getenv('SUBSTACK_EMAIL')
            
            if not all([gmail_email, gmail_password, substack_email]):
                raise ValueError("Missing required environment variables")
            
            msg = MIMEMultipart('alternative')
            msg['Subject'] = f"🤖 Top 5 AI Papers - {datetime.now().strftime('%B %d, %Y')}"
            msg['From'] = gmail_email
            msg['To'] = substack_email
            
            html_part = MIMEText(content, 'html')
            msg.attach(html_part)
            
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(gmail_email, gmail_password)
            server.send_message(msg)
            server.quit()
            
            logger.info("Email sent successfully to Substack!")
            
        except Exception as e:
            logger.error(f"Error sending email: {e}")
            raise
    
    def run(self):
        """Main execution function"""
        logger.info("Starting AI Papers Agent - Social Media Engagement Ranking")
        
        try:
            # Fetch recent papers
            papers = self.fetch_recent_papers()
            
            if not papers:
                logger.warning("No papers found")
                return
            
            # Rank papers by social engagement
            ranked_papers = self.rank_papers(papers)
            
            if not ranked_papers:
                logger.warning("No papers with social engagement found")
                return
            
            # Get top 5 papers
            top_papers = ranked_papers[:5]
            
            logger.info(f"Selected top {len(top_papers)} papers:")
            for i, (paper, score) in enumerate(top_papers, 1):
                logger.info(f"{i}. {paper.title[:50]}... (Score: {score:.2f})")
            
            # Generate and send email
            email_content = self.format_email_content(top_papers)
            self.send_email(email_content)
            
            # Mark papers as processed
            for paper, score in top_papers:
                self.add_processed_paper(paper.get_short_id(), paper.title, score)
            
            logger.info("AI Papers Agent completed successfully!")
            
        except Exception as e:
            logger.error(f"Error in main execution: {e}")
            raise

if __name__ == "__main__":
    agent = AIPapersAgent()
    agent.run()
