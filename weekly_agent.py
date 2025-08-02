import feedparser
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta
import time
import random
import json
import urllib.parse

def get_recent_ai_papers_rss(days_back=7):
    """Fetch recent AI papers from arXiv RSS feeds (FREE)"""
    rss_feeds = [
        'http://rss.arxiv.org/rss/cs.AI',
        'http://rss.arxiv.org/rss/cs.LG', 
        'http://rss.arxiv.org/rss/cs.CV',
        'http://rss.arxiv.org/rss/cs.CL',
        'http://rss.arxiv.org/rss/cs.NE',
    ]
    
    papers = []
    cutoff_date = datetime.now() - timedelta(days=days_back)
    
    for feed_url in rss_feeds:
        try:
            print(f"Fetching from {feed_url}")
            feed = feedparser.parse(feed_url)
            
            for entry in feed.entries:
                arxiv_id = re.search(r'(\d+\.\d+)', entry.link)
                if not arxiv_id:
                    continue
                arxiv_id = arxiv_id.group(1)
                
                pub_date = datetime(*entry.published_parsed[:6])
                
                if pub_date >= cutoff_date:
                    title_parts = entry.title.split('. (arXiv:')
                    title = title_parts[0]
                    
                    authors = extract_authors_from_summary(entry.summary)
                    
                    paper = {
                        'title': title.strip(),
                        'authors': authors,
                        'abstract': clean_abstract(entry.summary),
                        'arxiv_id': arxiv_id,
                        'published': pub_date.isoformat(),
                        'pdf_url': f'https://arxiv.org/pdf/{arxiv_id}.pdf',
                        'abs_url': f'https://arxiv.org/abs/{arxiv_id}'
                    }
                    papers.append(paper)
                    
        except Exception as e:
            print(f"Error fetching RSS feed {feed_url}: {e}")
            continue
    
    return papers

def extract_authors_from_summary(summary):
    """Extract authors from arXiv summary"""
    author_match = re.search(r'Authors?:\s*([^<]+)', summary)
    if author_match:
        authors_text = author_match.group(1).strip()
        authors = re.split(r',|\sand\s', authors_text)
        return [author.strip() for author in authors if author.strip()]
    return []

def clean_abstract(summary):
    """Clean abstract from RSS summary"""
    soup = BeautifulSoup(summary, 'html.parser')
    text = soup.get_text()
    
    abstract_match = re.search(r'Abstract:\s*(.+)', text, re.DOTALL)
    if abstract_match:
        return abstract_match.group(1).strip()
    
    return text.strip()

class FreeSocialScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def scrape_reddit_discussions(self, paper_title, arxiv_id):
        """Scrape Reddit using free API"""
        total_score = 0
        subreddits = ['MachineLearning', 'artificial', 'compsci', 'deeplearning']
        
        for subreddit in subreddits:
            try:
                search_queries = [paper_title[:50], arxiv_id]
                
                for query in search_queries:
                    url = f'https://www.reddit.com/r/{subreddit}/search.json'
                    params = {
                        'q': query,
                        'restrict_sr': 'on',
                        't': 'week',
                        'sort': 'relevance',
                        'limit': 10
                    }
                    
                    time.sleep(random.uniform(1, 2))
                    
                    response = self.session.get(url, params=params)
                    if response.status_code == 200:
                        data = response.json()
                        
                        for post in data.get('data', {}).get('children', []):
                            post_data = post.get('data', {})
                            score = post_data.get('score', 0)
                            comments = post_data.get('num_comments', 0)
                            total_score += score + (comments * 2)
                            
            except Exception as e:
                print(f"Reddit scraping error for {subreddit}: {e}")
                continue
        
        return total_score
    
    def scrape_hackernews_mentions(self, paper_title, arxiv_id):
        """Scrape Hacker News using free API"""
        try:
            search_queries = [paper_title[:50], arxiv_id]
            total_score = 0
            
            for query in search_queries:
                url = 'https://hn.algolia.com/api/v1/search'
                params = {
                    'query': query,
                    'tags': 'story',
                    'numericFilters': f'created_at_i>{int((datetime.now() - timedelta(days=7)).timestamp())}'
                }
                
                response = requests.get(url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    
                    for hit in data.get('hits', []):
                        points = hit.get('points', 0)
                        comments = hit.get('num_comments', 0)
                        total_score += points + (comments * 1.5)
            
            return total_score
            
        except Exception as e:
            print(f"HackerNews scraping error: {e}")
            return 0

def get_semantic_scholar_data(arxiv_id):
    """Use Semantic Scholar's free API"""
    try:
        url = f'https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}'
        params = {'fields': 'citationCount,influentialCitationCount'}
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return {
                'citations': data.get('citationCount', 0),
                'influential_citations': data.get('influentialCitationCount', 0)
            }
    except Exception as e:
        print(f"Semantic Scholar API error: {e}")
    
    return {'citations': 0, 'influential_citations': 0}

class FreeContentGenerator:
    def create_template_summary(self, paper):
        """Create summary using templates"""
        sentences = paper['abstract'].split('. ')
        
        if len(sentences) >= 2:
            problem_statement = sentences[0]
            conclusion = sentences[-1] if len(sentences) > 1 else sentences[0]
        else:
            problem_statement = paper['abstract'][:200] + "..."
            conclusion = ""
        
        category = self.guess_category_from_title_abstract(paper)
        
        summary = f"""This paper addresses {problem_statement.lower()}

The research focuses on {category} and presents novel approaches that build upon current state-of-the-art techniques. The authors introduce methodology designed to address key limitations in existing approaches while advancing the field.

{conclusion} This work contributes to the broader understanding of {category} and provides practical insights for researchers working on similar problems."""
        
        return summary
    
    def guess_category_from_title_abstract(self, paper):
        """Guess research category from title and abstract"""
        text = (paper['title'] + ' ' + paper['abstract']).lower()
        
        if any(term in text for term in ['vision', 'image', 'video', 'visual', 'cnn']):
            return 'computer vision and image analysis'
        elif any(term in text for term in ['language', 'text', 'nlp', 'bert', 'gpt']):
            return 'natural language processing'
        elif any(term in text for term in ['reinforcement', 'rl', 'agent', 'policy']):
            return 'reinforcement learning'
        elif any(term in text for term in ['neural', 'deep', 'network', 'learning']):
            return 'machine learning and neural networks'
        else:
            return 'artificial intelligence'
    
    def create_substack_post(self, top_papers):
        """Generate complete Substack post"""
        date_str = datetime.now().strftime("%B %d, %Y")
        
        post_content = f"""# Top 5 AI Papers This Week - {date_str}

Welcome to this week's roundup of the most discussed AI research papers! These papers have been trending across social media platforms based on community engagement and discussion volume.

*Rankings are based on social media mentions, discussions, and community engagement across Reddit, Hacker News, and academic platforms.*

"""
        
        for i, paper in enumerate(top_papers, 1):
            summary = self.create_template_summary(paper)
            
            author_list = paper['authors'][:5]
            authors_text = ', '.join(author_list)
            if len(paper['authors']) > 5:
                authors_text += f" and {len(paper['authors']) - 5} others"
            
            post_content += f"""## {i}. {paper['title']}

**Authors:** {authors_text}

{summary}

**📄 Read the paper:** [arXiv:{paper['arxiv_id']}]({paper['abs_url']}) | [PDF]({paper['pdf_url']})  
**📊 Engagement Score:** {paper.get('popularity_score', 0):.0f}

---

"""
        
        post_content += """## About This Weekly Roundup

This automated digest tracks AI research papers based on:
- Social media discussions and mentions
- Community engagement metrics
- Academic platform activity

**🔔 Subscribe** to get these weekly AI research roundups delivered directly to your inbox!

*This roundup is automatically generated. No papers are repeated across weeks.*"""
        
        return post_content

class FreeAIWeeklyAgent:
    def __init__(self):
        self.scraper = FreeSocialScraper()
        self.content_generator = FreeContentGenerator()
        self.load_featured_papers()
    
    def load_featured_papers(self):
        """Load list of previously featured papers"""
        try:
            with open('featured_papers.json', 'r') as f:
                self.featured_papers = set(json.load(f))
        except FileNotFoundError:
            self.featured_papers = set()
    
    def save_featured_papers(self):
        """Save updated list of featured papers"""
        with open('featured_papers.json', 'w') as f:
            json.dump(list(self.featured_papers), f)
    
    def calculate_engagement_score(self, paper):
        """Calculate engagement score using free methods"""
        print(f"Analyzing: {paper['title'][:50]}...")
        
        reddit_score = self.scraper.scrape_reddit_discussions(
            paper['title'], paper['arxiv_id']
        )
        
        hn_score = self.scraper.scrape_hackernews_mentions(
            paper['title'], paper['arxiv_id']
        )
        
        semantic_data = get_semantic_scholar_data(paper['arxiv_id'])
        
        total_score = (
            reddit_score * 0.4 +
            hn_score * 0.3 +
            semantic_data['citations'] * 10 +
            semantic_data['influential_citations'] * 20
        )
        
        # Recency boost
        days_old = (datetime.now() - datetime.fromisoformat(paper['published'])).days
        recency_multiplier = max(0.5, 1 - (days_old / 7))
        total_score *= recency_multiplier
        
        return total_score
    
    def run_weekly_update(self):
        """Main execution function"""
        print(f"🚀 Starting weekly AI paper discovery - {datetime.now()}")
        
        # Get recent papers
        papers = get_recent_ai_papers_rss(days_back=7)
        print(f"Found {len(papers)} recent papers")
        
        # Filter out previously featured
        new_papers = [p for p in papers if p['arxiv_id'] not in self.featured_papers]
        print(f"📋 {len(new_papers)} new papers")
        
        if len(new_papers) < 5:
            papers = get_recent_ai_papers_rss(days_back=14)
            new_papers = [p for p in papers if p['arxiv_id'] not in self.featured_papers]
        
        # Score papers
        scored_papers = []
        for i, paper in enumerate(new_papers[:20]):  # Limit to 20 for speed
            try:
                score = self.calculate_engagement_score(paper)
                paper['popularity_score'] = score
                scored_papers.append(paper)
                print(f"  {i+1}/20: {score:.1f}")
                time.sleep(random.uniform(1, 2))  # Rate limiting
            except Exception as e:
                print(f"Error scoring paper {i+1}: {e}")
                continue
        
        # Get top 5
        top_papers = sorted(scored_papers, key=lambda x: x['popularity_score'], reverse=True)[:5]
        
        print("\n🏆 TOP 5 PAPERS:")
        for i, paper in enumerate(top_papers, 1):
            print(f"  {i}. {paper['popularity_score']:.1f} - {paper['title']}")
        
        # Generate content
        post_content = self.content_generator.create_substack_post(top_papers)
        
        # Save output
        output_data = {
            'title': f"Top 5 AI Papers This Week - {datetime.now().strftime('%B %d, %Y')}",
            'content': post_content,
            'timestamp': datetime.now().isoformat(),
            'papers': [{
                'title': p['title'],
                'arxiv_id': p['arxiv_id'],
                'score': p['popularity_score']
            } for p in top_papers]
        }
        
        with open('weekly_post.json', 'w') as f:
            json.dump(output_data, f, indent=2)
        
        # Update featured papers
        for paper in top_papers:
            self.featured_papers.add(paper['arxiv_id'])
        self.save_featured_papers()
        
        print("✅ Weekly update completed!")
        return output_data

if __name__ == "__main__":
    agent = FreeAIWeeklyAgent()
    result = agent.run_weekly_update()
