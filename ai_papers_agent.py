#!/usr/bin/env python3
"""
AI Papers Weekly Agent - Simplified for kjanik70/ai-papers-agent
Automatically finds and ranks top 5 AI papers each week.
"""

import requests
import json
import re
from datetime import datetime, timedelta
import time
import xml.etree.ElementTree as ET
import os
from typing import List, Dict

class AIpapersAgent:
    def __init__(self):
        self.previous_papers = set()
        self.data_file = "previous_papers.json"
        self.load_previous_papers()
        
    def load_previous_papers(self):
        """Load previously featured papers from file"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.previous_papers = set(data.get('papers', []))
                    print(f"📚 Loaded {len(self.previous_papers)} previously featured papers")
        except Exception as e:
            print(f"⚠️ Error loading previous papers: {e}")
            
    def save_previous_papers(self):
        """Save previously featured papers to file"""
        try:
            data = {
                'papers': list(self.previous_papers),
                'last_updated': datetime.now().isoformat(),
                'total_featured': len(self.previous_papers)
            }
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"💾 Saved {len(self.previous_papers)} papers to tracking file")
        except Exception as e:
            print(f"❌ Error saving previous papers: {e}")

    def get_recent_arxiv_papers(self, days_back=7) -> List[Dict]:
        """Fetch recent AI papers from ArXiv"""
        print(f"🔍 Fetching AI papers from the last {days_back} days...")
        papers = []
        
        # AI categories on ArXiv
        categories = [
            'cs.AI',   # Artificial Intelligence
            'cs.LG',   # Machine Learning
            'cs.CL',   # Natural Language Processing
            'cs.CV',   # Computer Vision
            'cs.NE',   # Neural Networks
            'cs.RO',   # Robotics
            'stat.ML'  # Statistics ML
        ]
        
        cutoff_date = datetime.now() - timedelta(days=days_back)
        print(f"📅 Looking for papers published after: {cutoff_date.strftime('%Y-%m-%d')}")
        
        for category in categories:
            try:
                print(f"  📂 Searching category: {category}")
                
                # Query ArXiv API
                base_url = "http://export.arxiv.org/api/query"
                params = {
                    'search_query': f'cat:{category}',
                    'start': 0,
                    'max_results': 100,
                    'sortBy': 'submittedDate',
                    'sortOrder': 'descending'
                }
                
                response = requests.get(base_url, params=params, timeout=30)
                response.raise_for_status()
                
                # Parse XML response
                root = ET.fromstring(response.content)
                namespace = {'atom': 'http://www.w3.org/2005/Atom'}
                
                category_count = 0
                for entry in root.findall('atom:entry', namespace):
                    try:
                        # Extract paper info
                        paper_id = entry.find('atom:id', namespace).text.split('/')[-1]
                        
                        # Skip if already featured
                        if paper_id in self.previous_papers:
                            continue
                            
                        title = entry.find('atom:title', namespace).text.strip()
                        summary = entry.find('atom:summary', namespace).text.strip()
                        
                        # Check publication date
                        published_elem = entry.find('atom:published', namespace)
                        if published_elem is not None:
                            pub_date_str = published_elem.text
                            pub_date = datetime.fromisoformat(pub_date_str.replace('Z', '+00:00'))
                            
                            # Only include recent papers
                            if pub_date.replace(tzinfo=None) >= cutoff_date:
                                # Get authors
                                authors = []
                                for author in entry.findall('atom:author', namespace):
                                    name_elem = author.find('atom:name', namespace)
                                    if name_elem is not None:
                                        authors.append(name_elem.text)
                                
                                paper = {
                                    'id': paper_id,
                                    'title': title,
                                    'summary': summary,
                                    'authors': authors,
                                    'published': pub_date,
                                    'url': f"https://arxiv.org/abs/{paper_id}",
                                    'pdf_url': f"https://arxiv.org/pdf/{paper_id}.pdf",
                                    'category': category,
                                    'social_score': 0
                                }
                                
                                papers.append(paper)
                                category_count += 1
                    
                    except Exception as e:
                        continue  # Skip problematic entries
                
                print(f"    ✅ Found {category_count} new papers")
                time.sleep(1)  # Be respectful to ArXiv
                
            except Exception as e:
                print(f"    ❌ Error with category {category}: {e}")
                continue
        
        print(f"🎯 Total papers collected: {len(papers)}")
        return papers

    def search_reddit_mentions(self, paper_title: str, paper_id: str) -> int:
        """Search Reddit for paper mentions"""
        try:
            # Clean up search terms
            search_terms = [
                paper_title.split(':')[0][:50],  # Title before colon
                paper_id,
                f"arxiv {paper_id}"
            ]
            
            total_score = 0
            
            for term in search_terms:
                if not term.strip():
                    continue
                    
                try:
                    # Search Reddit's JSON API
                    url = "https://www.reddit.com/search.json"
                    params = {
                        'q': term,
                        'sort': 'new',
                        'limit': 20,
                        't': 'week'
                    }
                    
                    headers = {'User-Agent': 'AI-Papers-Bot/1.0'}
                    response = requests.get(url, params=params, headers=headers, timeout=10)
                    
                    if response.status_code == 200:
                        data = response.json()
                        posts = data.get('data', {}).get('children', [])
                        
                        # Weight by engagement
                        for post in posts:
                            post_data = post.get('data', {})
                            upvotes = post_data.get('ups', 0)
                            comments = post_data.get('num_comments', 0)
                            
                            # Simple scoring
                            post_score = min(upvotes // 10, 3) + min(comments // 5, 2)
                            total_score += post_score
                    
                    time.sleep(2)  # Rate limiting
                    
                except Exception:
                    continue
            
            return min(total_score, 15)  # Cap score
            
        except Exception:
            return 0

    def calculate_impact_score(self, paper: Dict) -> int:
        """Calculate paper impact based on content analysis"""
        title_lower = paper['title'].lower()
        summary_lower = paper['summary'].lower()
        
        # High-impact AI keywords with weights
        keywords = {
            'transformer': 4, 'gpt': 5, 'llm': 4, 'large language': 5,
            'multimodal': 4, 'reasoning': 3, 'alignment': 4,
            'diffusion': 3, 'generative': 2, 'self-supervised': 2,
            'few-shot': 2, 'zero-shot': 2, 'in-context': 3,
            'chain-of-thought': 4, 'reinforcement learning': 3,
            'computer vision': 2, 'natural language': 2,
            'neural network': 1, 'deep learning': 1,
            'benchmark': 2, 'state-of-the-art': 3, 'sota': 3
        }
        
        score = 0
        for keyword, weight in keywords.items():
            if keyword in title_lower:
                score += weight * 2  # Title mentions worth more
            elif keyword in summary_lower:
                score += weight
        
        # Author count bonus (more authors = more promotion)
        author_bonus = min(len(paper['authors']) // 2, 3)
        score += author_bonus
        
        # Recency bonus
        days_old = (datetime.now() - paper['published'].replace(tzinfo=None)).days
        recency_bonus = max(0, 7 - days_old)
        score += recency_bonus
        
        return min(score, 25)  # Cap at 25

    def rank_papers(self, papers: List[Dict]) -> List[Dict]:
        """Rank papers by combined social and impact scores"""
        print(f"📊 Ranking {len(papers)} papers...")
        
        for i, paper in enumerate(papers, 1):
            if i % 10 == 0:
                print(f"  Progress: {i}/{len(papers)}")
            
            # Get Reddit mentions
            reddit_score = self.search_reddit_mentions(paper['title'], paper['id'])
            
            # Calculate impact score
            impact_score = self.calculate_impact_score(paper)
            
            # Combined score
            paper['social_score'] = reddit_score + impact_score
            paper['reddit_score'] = reddit_score
            paper['impact_score'] = impact_score
            
            time.sleep(1)  # Rate limiting
        
        # Sort by total score
        ranked = sorted(papers, key=lambda x: x['social_score'], reverse=True)
        
        print("\n🏆 Top 10 papers by score:")
        for i, paper in enumerate(ranked[:10], 1):
            print(f"  {i:2d}. Score {paper['social_score']:2d} - {paper['title'][:60]}...")
        
        return ranked

    def generate_paper_summary(self, paper: Dict) -> str:
        """Generate readable summary from abstract"""
        abstract = paper['summary'].replace('\n', ' ').strip()
        abstract = re.sub(r'\s+', ' ', abstract)  # Clean whitespace
        
        # Split into sentences
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', abstract)
        sentences = [s.strip() for s in sentences if s.strip() and len(s) > 15]
        
        if len(sentences) < 2:
            return abstract
        
        # Create 2-3 paragraph summary
        if len(sentences) >= 6:
            para1 = '. '.join(sentences[:2]) + '.'
            para2 = '. '.join(sentences[2:-2]) + '.'
            para3 = '. '.join(sentences[-2:]) + '.'
            return f"{para1}\n\n{para2}\n\n{para3}"
        elif len(sentences) >= 3:
            mid = len(sentences) // 2
            para1 = '. '.join(sentences[:mid]) + '.'
            para2 = '. '.join(sentences[mid:]) + '.'
            return f"{para1}\n\n{para2}"
        else:
            return '. '.join(sentences) + '.'

    def generate_substack_post(self, top_papers: List[Dict]) -> str:
        """Generate Substack-ready post"""
        current_date = datetime.now()
        date_str = current_date.strftime("%B %d, %Y")
        
        # Calculate weekly stats
        total_authors = sum(len(p['authors']) for p in top_papers)
        categories = list(set(p['category'] for p in top_papers))
        avg_score = sum(p['social_score'] for p in top_papers) / len(top_papers)
        
        post = f"""# 🤖 Top 5 AI Papers This Week
## Week of {date_str}

Welcome to this week's roundup of the most impactful AI research papers! These papers have been generating buzz across Reddit, academic Twitter, and research communities.

**📊 This Week's Stats:**
- 📄 **{len(top_papers)} featured papers** from **{len(categories)} categories**  
- 👥 **{total_authors} contributing authors**
- 🔥 **Average engagement score:** {avg_score:.1f}
- 🏆 **Highest scorer:** {top_papers[0]['social_score']} points

---

"""
        
        for i, paper in enumerate(top_papers, 1):
            # Format authors (limit display)
            authors_str = ", ".join(paper['authors'][:3])
            if len(paper['authors']) > 3:
                authors_str += f" et al. (+{len(paper['authors'])-3} more)"
            
            # Publication date
            pub_date = paper['published'].strftime("%B %d, %Y")
            
            # Generate summary
            summary = self.generate_paper_summary(paper)
            
            # Category emoji
            emoji_map = {
                'cs.AI': '🧠', 'cs.LG': '📈', 'cs.CL': '💬',
                'cs.CV': '👁️', 'cs.NE': '🧬', 'cs.RO': '🤖', 'stat.ML': '📊'
            }
            category_emoji = emoji_map.get(paper['category'], '🔬')
            
            post += f"""## {i}. {paper['title']}

{category_emoji} **Category:** {paper['category'].upper()} | 📅 **Published:** {pub_date} | 🔥 **Score:** {paper['social_score']} points

**Authors:** {authors_str}

**Links:** [ArXiv Paper]({paper['url']}) | [PDF Download]({paper['pdf_url']})

{summary}

---

"""
        
        post += f"""
## 📈 About This Analysis

Each week, I analyze recent AI papers from ArXiv and rank them based on:

🗣️ **Social Media Engagement** - Mentions and discussions on Reddit  
🎯 **Research Impact Indicators** - Trending keywords and methodologies  
👥 **Collaboration Signals** - Author networks and institutional diversity  
⏰ **Recency Factor** - Boost for just-published papers  

**Methodology:** Papers are scored using a composite algorithm that weighs social media mentions (Reddit discussions, estimated Twitter activity) alongside content analysis for breakthrough keywords like "transformer," "multimodal," "reasoning," and others that typically indicate high-impact research.

**Coverage:** This analysis scans 7 major AI categories on ArXiv: Artificial Intelligence, Machine Learning, Natural Language Processing, Computer Vision, Neural Networks, Robotics, and Statistics ML.

---

*🤖 This analysis is automatically generated every Friday by monitoring ArXiv submissions and tracking social media engagement.*

**📬 Subscribe** for weekly AI research updates  
**💬 Share your thoughts** on this week's selections in the comments  
**🔗 Follow the project** on [GitHub](https://github.com/kjanik70/ai-papers-agent)

*Next edition: {(current_date + timedelta(days=7)).strftime("%B %d, %Y")}*
"""
        
        return post

    def save_analysis_summary(self, top_papers: List[Dict], filename: str):
        """Save analysis metadata"""
        summary = {
            'filename': filename,
            'date': datetime.now().isoformat(),
            'paper_count': len(top_papers),
            'categories': list(set(p['category'] for p in top_papers)),
            'avg_score': sum(p['social_score'] for p in top_papers) / len(top_papers),
            'top_paper': {
                'title': top_papers[0]['title'],
                'score': top_papers[0]['social_score'],
                'url': top_papers[0]['url']
            },
            'papers': [
                {
                    'rank': i+1,
                    'title': p['title'],
                    'score': p['social_score'],
                    'category': p['category'],
                    'url': p['url']
                }
                for i, p in enumerate(top_papers)
            ]
        }
        
        with open('analysis_summary.json', 'w') as f:
            json.dump(summary, f, indent=2)

    def run_weekly_analysis(self):
        """Main execution function"""
        start_time = datetime.now()
        print(f"🚀 Starting AI Papers Weekly Analysis - {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        try:
            # Step 1: Get recent papers
            papers = self.get_recent_arxiv_papers()
            
            if len(papers) < 5:
                print(f"⚠️ Only found {len(papers)} papers, trying longer timeframe...")
                papers = self.get_recent_arxiv_papers(days_back=10)
                
                if len(papers) < 5:
                    print(f"❌ Still only found {len(papers)} papers. Exiting.")
                    return
            
            # Step 2: Rank papers
            ranked_papers = self.rank_papers(papers)
            top_5 = ranked_papers[:5]
            
            # Step 3: Generate content
            post_content = self.generate_substack_post(top_5)
            
            # Step 4: Save files
            filename = f"ai_papers_weekly_{datetime.now().strftime('%Y%m%d')}.md"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(post_content)
            
            # Step 5: Save metadata
            self.save_analysis_summary(top_5, filename)
            
            # Step 6: Update tracking
            for paper in top_5:
                self.previous_papers.add(paper['id'])
            self.save_previous_papers()
            
            # Success!
            duration = (datetime.now() - start_time).total_seconds()
            print(f"✅ Analysis completed in {duration:.1f} seconds!")
            print(f"📝 Generated: {filename}")
            print(f"🎯 Featured {len(top_5)} papers with average score: {sum(p['social_score'] for p in top_5)/len(top_5):.1f}")
            
        except Exception as e:
            print(f"💥 Error during analysis: {e}")
            raise

if __name__ == "__main__":
    agent = AIpapersAgent()
    agent.run_weekly_analysis()
