#!/usr/bin/env python3
"""
AI Papers Agent - GitHub Pages + RSS Output
Finds the top 5 AI papers with highest social media engagement in the last 7 days
Outputs to GitHub Pages and RSS feed (no email required)
"""

import arxiv
import requests
import json
import sqlite3
import re
import time
import os
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from urllib.parse import quote
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
    """Search for Twitter mentions using snscrape"""
    mentions_data = {'mentions': 0, 'replies': 0, 'likes': 0}
    search_queries = [arxiv_id, f'arxiv.org/abs/{arxiv_id}', paper_title]
    try:
        import snscrape.modules.twitter as sntwitter
        for query in search_queries:
            count = 0
            for tweet in sntwitter.TwitterSearchScraper(f'"{query}" since:{(datetime.now()-timedelta(days=7)).strftime("%Y-%m-%d")}').get_items():
                if count >= 100:  # Limit to 100 tweets per query to avoid long runtimes
                    break
                mentions_data['mentions'] += 1
                mentions_data['replies'] += getattr(tweet, 'replyCount', 0)
                mentions_data['likes'] += getattr(tweet, 'likeCount', 0)
                count += 1
            time.sleep(1)  # Gentle rate limiting
    except Exception as e:
        logger.warning(f"snscrape Twitter search failed: {e}")
    return mentions_data
    
    def _scrape_twitter_data(self, instance: str, search_term: str) -> Dict[str, int]:
        """Scrape Twitter data from nitter instance with better error handling"""
        try:
            url = f"{instance}/search?f=tweets&q={quote(search_term)}&since=7d"
            
            # More aggressive timeout and retry settings
            response = self.session.get(
                url, 
                timeout=15,  # Increased timeout
                headers={
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'keep-alive',
                }
            )
            
            if response.status_code != 200:
                logger.warning(f"HTTP {response.status_code} from {instance}")
                return {'mentions': 0, 'replies': 0, 'likes': 0}
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Look for various tweet container classes (nitter sites use different ones)
            tweet_selectors = [
                'div.timeline-item',
                'div.tweet',
                'article[data-testid="tweet"]',
                '.tweet-content',
                '.timeline-tweet'
            ]
            
            tweets = []
            for selector in tweet_selectors:
                found_tweets = soup.select(selector)
                if found_tweets:
                    tweets = found_tweets
                    break
            
            if not tweets:
                logger.info(f"No tweets found with standard selectors on {instance}")
                return {'mentions': 0, 'replies': 0, 'likes': 0}
            
            total_mentions = len(tweets)
            total_replies = 0
            total_likes = 0
            
            # Try multiple selectors for engagement metrics
            for tweet in tweets[:10]:  # Limit to first 10 to avoid timeouts
                # Try different reply count selectors
                reply_selectors = [
                    'div.icon-comment',
                    '.tweet-stat[title*="repl"]',
                    '.tweet-replies',
                    '[data-testid="reply"]'
                ]
                
                for selector in reply_selectors:
                    reply_elem = tweet.select_one(selector)
                    if reply_elem and reply_elem.parent:
                        reply_text = reply_elem.parent.get_text(strip=True)
                        reply_count = self._extract_number(reply_text)
                        total_replies += reply_count
                        break
                
                # Try different like count selectors
                like_selectors = [
                    'div.icon-heart',
                    '.tweet-stat[title*="like"]',
                    '.tweet-likes',
                    '[data-testid="like"]'
                ]
                
                for selector in like_selectors:
                    like_elem = tweet.select_one(selector)
                    if like_elem and like_elem.parent:
                        like_text = like_elem.parent.get_text(strip=True)
                        like_count = self._extract_number(like_text)
                        total_likes += like_count
                        break
            
            result = {
                'mentions': total_mentions,
                'replies': total_replies,
                'likes': total_likes
            }
            
            logger.info(f"Twitter scraping successful: {result}")
            return result
            
        except requests.exceptions.Timeout:
            logger.warning(f"Timeout connecting to {instance}")
            return {'mentions': 0, 'replies': 0, 'likes': 0}
        except requests.exceptions.ConnectionError:
            logger.warning(f"Connection error to {instance}")
            return {'mentions': 0, 'replies': 0, 'likes': 0}
        except Exception as e:
            logger.error(f"Error scraping Twitter data from {instance}: {str(e)[:100]}...")
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

class OutputManager:
    """Handles GitHub Pages and RSS output generation"""
    
    def __init__(self):
        self.output_dir = "docs"  # GitHub Pages serves from docs/ folder
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_github_pages(self, top_papers: List[tuple]) -> str:
        """Generate static HTML for GitHub Pages"""
        current_date = datetime.now().strftime("%B %d, %Y")
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🤖 Top 5 AI Papers - {current_date}</title>
    <meta name="description" content="Weekly digest of AI papers ranked by social media engagement">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6; 
            color: #333; 
            background: #f8f9fa;
        }}
        .container {{ max-width: 900px; margin: 0 auto; padding: 20px; }}
        .header {{ 
            text-align: center; 
            background: white; 
            padding: 40px 20px; 
            border-radius: 12px; 
            box-shadow: 0 2px 20px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}
        .header h1 {{ font-size: 2.5em; margin-bottom: 10px; color: #2c3e50; }}
        .header p {{ color: #7f8c8d; font-size: 1.1em; }}
        .paper {{ 
            background: white; 
            margin: 25px 0; 
            padding: 30px; 
            border-radius: 12px; 
            box-shadow: 0 2px 15px rgba(0,0,0,0.08);
            border-left: 5px solid #3498db; 
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}
        .paper:hover {{ 
            transform: translateY(-2px); 
            box-shadow: 0 4px 25px rgba(0,0,0,0.12); 
        }}
        .paper h2 {{ 
            color: #2c3e50; 
            margin-bottom: 15px; 
            font-size: 1.4em; 
            line-height: 1.3;
        }}
        .paper-meta {{ 
            display: flex; 
            flex-wrap: wrap; 
            gap: 15px; 
            margin-bottom: 15px; 
            font-size: 0.9em;
        }}
        .authors {{ color: #7f8c8d; }}
        .score {{ 
            color: #e74c3c; 
            font-weight: bold; 
            background: #ffe6e6; 
            padding: 4px 8px; 
            border-radius: 6px;
        }}
        .summary {{ 
            color: #34495e; 
            margin: 20px 0; 
            line-height: 1.7;
        }}
        .links {{ margin-top: 20px; }}
        .links a {{ 
            color: #3498db; 
            text-decoration: none; 
            margin-right: 15px; 
            padding: 8px 16px; 
            border: 2px solid #3498db; 
            border-radius: 6px; 
            transition: all 0.2s ease;
            display: inline-block;
        }}
        .links a:hover {{ 
            background: #3498db; 
            color: white; 
            transform: translateY(-1px);
        }}
        .footer {{ 
            text-align: center; 
            margin-top: 50px; 
            padding: 30px; 
            background: white; 
            border-radius: 12px; 
            color: #7f8c8d; 
            box-shadow: 0 2px 15px rgba(0,0,0,0.08);
        }}
        .social-badge {{ 
            background: #e8f4f8; 
            color: #2980b9; 
            padding: 4px 8px; 
            border-radius: 4px; 
            font-size: 0.85em; 
            margin-left: 10px;
        }}
        @media (max-width: 768px) {{
            .container {{ padding: 10px; }}
            .header h1 {{ font-size: 2em; }}
            .paper {{ padding: 20px; margin: 15px 0; }}
            .paper-meta {{ flex-direction: column; gap: 8px; }}
            .links a {{ display: block; margin: 5px 0; text-align: center; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 Top 5 AI Papers This Week</h1>
            <p>Week of {current_date}</p>
            <p>Ranked by social media engagement (mentions, replies, likes) in the last 7 days</p>
            <div class="social-badge">🔥 Trending • 📊 Data-Driven • 🚀 Real-Time</div>
        </div>
"""
        
        for i, (paper, score) in enumerate(top_papers, 1):
            authors = ", ".join([author.name for author in paper.authors[:3]])
            if len(paper.authors) > 3:
                authors += f", et al. ({len(paper.authors)} total)"
            
            emoji = ["🥇", "🥈", "🥉", "🏅", "⭐"][i-1]
            summary = self._generate_summary(paper)
            
            html_content += f"""
        <div class="paper">
            <h2>{emoji} #{i}. {paper.title}</h2>
            <div class="paper-meta">
                <div class="authors"><strong>Authors:</strong> {authors}</div>
                <div class="score">🔥 Social Engagement Score: {score:.1f}</div>
            </div>
            <div class="summary">{summary}</div>
            <div class="links">
                <a href="{paper.entry_id}" target="_blank">📖 Read Full Paper</a>
                <a href="{paper.pdf_url}" target="_blank">📄 Download PDF</a>
            </div>
        </div>
"""
        
        html_content += f"""
        <div class="footer">
            <p><strong>Generated by AI Papers Agent</strong></p>
            <p>Tracking social media engagement across Twitter, Reddit, Hacker News, and GitHub</p>
            <p>🤖 Built with ❤️ for the AI research community</p>
            <p><small>Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M UTC")}</small></p>
            <p style="margin-top: 15px;">
                <a href="feed.xml" style="color: #e67e22; text-decoration: none;">📡 Subscribe to RSS Feed</a>
            </p>
        </div>
    </div>
</body>
</html>"""
        
        # Save to docs/index.html for GitHub Pages
        filename = f"{self.output_dir}/index.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        logger.info(f"Generated GitHub Pages site: {filename}")
        return filename
    
    def generate_rss_feed(self, top_papers: List[tuple]) -> str:
        """Generate RSS feed"""
        current_date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
        build_date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
        week_date = datetime.now().strftime("%B %d, %Y")
        
        # Get GitHub Pages URL from environment or use placeholder
        base_url = os.getenv('GITHUB_PAGES_URL', 'https://your-username.github.io/ai-papers-agent')
        
        rss_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
    <title>Top AI Papers - Social Engagement Rankings</title>
    <description>Weekly digest of AI papers ranked by social media buzz (mentions, replies, likes) from the past 7 days</description>
    <link>{base_url}</link>
    <atom:link href="{base_url}/feed.xml" rel="self" type="application/rss+xml" />
    <language>en-us</language>
    <lastBuildDate>{build_date}</lastBuildDate>
    <pubDate>{current_date}</pubDate>
    <generator>AI Papers Agent</generator>
    <webMaster>ai-papers-agent@github.com</webMaster>
    <category>Artificial Intelligence</category>
    <category>Machine Learning</category>
    <category>Research</category>
"""
        
        for i, (paper, score) in enumerate(top_papers, 1):
            authors = ", ".join([author.name for author in paper.authors[:3]])
            if len(paper.authors) > 3:
                authors += ", et al."
            
            emoji = ["🥇", "🥈", "🥉", "🏅", "⭐"][i-1]
            summary = self._generate_summary(paper)
            
            # Create unique GUID for this paper in this week
            guid = f"{paper.get_short_id()}-{datetime.now().strftime('%Y-W%U')}"
            
            rss_content += f"""
    <item>
        <title>{emoji} #{i}. {paper.title}</title>
        <description><![CDATA[
            <p><strong>Authors:</strong> {authors}</p>
            <p><strong>Social Engagement Score:</strong> {score:.1f} 🔥</p>
            <p><strong>Week of:</strong> {week_date}</p>
            <hr>
            <p>{summary}</p>
            <p style="margin-top: 20px;">
                <a href="{paper.entry_id}" style="color: #3498db; text-decoration: none; margin-right: 15px;">📖 Read Full Paper</a>
                <a href="{paper.pdf_url}" style="color: #3498db; text-decoration: none;">📄 Download PDF</a>
            </p>
        ]]></description>
        <link>{paper.entry_id}</link>
        <guid isPermaLink="false">{guid}</guid>
        <pubDate>{current_date}</pubDate>
        <category>AI Research</category>
        <author>ai-papers-agent@github.com ({authors})</author>
        <source url="{base_url}/feed.xml">Top AI Papers - Social Engagement Rankings</source>
    </item>"""
        
        rss_content += """
</channel>
</rss>"""
        
        # Save RSS feed
        filename = f"{self.output_dir}/feed.xml"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(rss_content)
        
        logger.info(f"Generated RSS feed: {filename}")
        return filename
    
    def generate_json_api(self, top_papers: List[tuple]) -> str:
        """Generate JSON API for developers"""
        current_date = datetime.now().isoformat()
        
        feed_data = {
            "generated_at": current_date,
            "title": "Top 5 AI Papers This Week",
            "description": "AI papers ranked by social media engagement in the last 7 days",
            "methodology": "Papers ranked by weighted social media engagement (Twitter, Reddit, Hacker News, GitHub)",
            "time_window": "7 days",
            "update_frequency": "Weekly (Fridays)",
            "papers": []
        }
        
        for i, (paper, score) in enumerate(top_papers, 1):
            authors = [author.name for author in paper.authors]
            
            paper_data = {
                "rank": i,
                "title": paper.title,
                "authors": authors,
                "arxiv_id": paper.get_short_id(),
                "arxiv_url": paper.entry_id,
                "pdf_url": paper.pdf_url,
                "published_date": paper.published.isoformat(),
                "social_engagement_score": round(score, 2),
                "summary": self._generate_summary(paper),
                "categories": [cat.term for cat in paper.categories],
                "primary_category": paper.primary_category
            }
            feed_data["papers"].append(paper_data)
        
        # Save JSON API
        filename = f"{self.output_dir}/api.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(feed_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Generated JSON API: {filename}")
        return filename
    
    def _generate_summary(self, paper) -> str:
        """Generate a concise summary from paper abstract"""
        try:
            abstract = paper.summary
            sentences = abstract.split('. ')
            
            # Take first 2-3 sentences or up to 200 words
            summary_sentences = []
            word_count = 0
            
            for sentence in sentences:
                words_in_sentence = len(sentence.split())
                if word_count + words_in_sentence > 200:
                    break
                summary_sentences.append(sentence.strip())
                word_count += words_in_sentence
                
                if len(summary_sentences) >= 3:
                    break
            
            summary = '. '.join(summary_sentences)
            if summary and not summary.endswith('.'):
                summary += '.'
                
            return summary if summary else abstract[:200] + "..."
            
        except Exception as e:
            logger.error(f"Error generating summary: {e}")
            return paper.summary[:200] + "..."

class AIPapersAgent:
    """Main agent class for finding and ranking AI papers"""
    
    def __init__(self):
        self.social_tracker = SocialMediaTracker()
        self.output_manager = OutputManager()
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
        """Calculate social media engagement score for a paper with resilient error handling"""
        logger.info(f"Calculating social score for: {paper.title[:50]}...")
        
        # Initialize scores
        twitter_data = {'mentions': 0, 'replies': 0, 'likes': 0}
        reddit_data = {'mentions': 0, 'replies': 0, 'likes': 0}
        hn_data = {'mentions': 0, 'replies': 0, 'likes': 0}
        github_data = {'mentions': 0, 'replies': 0, 'likes': 0}
        
        # Try each platform with error recovery
        platforms_attempted = 0
        platforms_successful = 0
        
        # Twitter with timeout protection
        try:
            logger.info("Searching Twitter...")
            twitter_data = self.social_tracker.search_twitter_mentions(paper.title, paper.get_short_id())
            platforms_attempted += 1
            if sum(twitter_data.values()) > 0:
                platforms_successful += 1
        except Exception as e:
            logger.warning(f"Twitter search failed: {str(e)[:100]}...")
        
        # Reddit search
        try:
            logger.info("Searching Reddit...")
            reddit_data = self.social_tracker.search_reddit_mentions(paper.title, paper.get_short_id())
            platforms_attempted += 1
            if sum(reddit_data.values()) > 0:
                platforms_successful += 1
        except Exception as e:
            logger.warning(f"Reddit search failed: {str(e)[:100]}...")
        
        # Hacker News search
        try:
            logger.info("Searching Hacker News...")
            hn_data = self.social_tracker.search_hackernews_mentions(paper.title, paper.get_short_id())
            platforms_attempted += 1
            if sum(hn_data.values()) > 0:
                platforms_successful += 1
        except Exception as e:
            logger.warning(f"Hacker News search failed: {str(e)[:100]}...")
        
        # GitHub search
        try:
            logger.info("Searching GitHub...")
            github_data = self.social_tracker.search_github_mentions(paper.title, paper.get_short_id())
            platforms_attempted += 1
            if sum(github_data.values()) > 0:
                platforms_successful += 1
        except Exception as e:
            logger.warning(f"GitHub search failed: {str(e)[:100]}...")
        
        # Calculate weighted score with platform availability adjustment
        base_score = (
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
        
        # If some platforms failed, boost scores from successful platforms
        if platforms_attempted > 0 and platforms_successful < platforms_attempted:
            platform_boost = 1 + (0.2 * (platforms_attempted - platforms_successful))
            score = base_score * platform_boost
            logger.info(f"Applied platform failure boost: {platform_boost:.2f}x")
        else:
            score = base_score
        
        total_engagement = (
            twitter_data['mentions'] + twitter_data['replies'] + twitter_data['likes'] +
            reddit_data['mentions'] + reddit_data['replies'] + reddit_data['likes'] +
            hn_data['mentions'] + hn_data['replies'] + hn_data['likes'] +
            github_data['mentions'] + github_data['replies'] + github_data['likes']
        )
        
        logger.info(f"Social score: {score:.2f} (Total engagement: {total_engagement}, Platforms: {platforms_successful}/{platforms_attempted})")
        
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
    
    def run(self):
        """Main execution function"""
        logger.info("Starting AI Papers Agent - GitHub Pages + RSS Output")
        
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
            
            # Generate outputs
            logger.info("Generating GitHub Pages and RSS outputs...")
            
            html_file = self.output_manager.generate_github_pages(top_papers)
            rss_file = self.output_manager.generate_rss_feed(top_papers)
            json_file = self.output_manager.generate_json_api(top_papers)
            
            logger.info("Generated outputs:")
            logger.info(f"  - GitHub Pages: {html_file}")
            logger.info(f"  - RSS Feed: {rss_file}")
            logger.info(f"  - JSON API: {json_file}")
            
            # Mark papers as processed
            for paper, score in top_papers:
                self.add_processed_paper(paper.get_short_id(), paper.title, score)
            
            logger.info("AI Papers Agent completed successfully!")
            
            # Print setup instructions if this is the first run
            self._print_setup_instructions()
            
        except Exception as e:
            logger.error(f"Error in main execution: {e}")
            raise
    
    def _print_setup_instructions(self):
        """Print GitHub Pages setup instructions"""
        logger.info("\n" + "="*60)
        logger.info("🎉 SUCCESS! Your AI papers digest has been generated!")
        logger.info("="*60)
        logger.info("\nTo enable GitHub Pages:")
        logger.info("1. Go to your repository on GitHub")
        logger.info("2. Click Settings → Pages")
        logger.info("3. Source: Deploy from a branch")
        logger.info("4. Branch: main")
        logger.info("5. Folder: /docs")
        logger.info("6. Click Save")
        logger.info("\nYour site will be available at:")
        logger.info("https://your-username.github.io/ai-papers-agent/")
        logger.info("\nRSS feed will be at:")
        logger.info("https://your-username.github.io/ai-papers-agent/feed.xml")
        logger.info("="*60)

if __name__ == "__main__":
    agent = AIPapersAgent()
    agent.run()
