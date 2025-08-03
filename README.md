# AI Papers Agent 🤖📚

**Automated weekly AI papers digest based on social media buzz - completely free!**

This intelligent agent automatically discovers and ranks AI research papers by their **social media engagement** over the past 7 days, then publishes the top 5 most discussed papers to your Substack. Unlike traditional academic ranking systems, this focuses on what the AI community is actually talking about right now.

## ✨ Key Features

- 🔥 **Trending Focus**: Ranks papers by social media buzz in the last 7 days
- 📊 **Multi-Platform Tracking**: Monitors Twitter/X, Reddit, Hacker News, and GitHub
- 📈 **Engagement Metrics**: Counts mentions, replies, likes, upvotes, and stars
- 🕒 **Age Agnostic**: Papers can be any age - only recent discussion matters
- 📧 **Auto-Publishing**: Sends beautifully formatted digests to Substack
- 🚫 **Duplicate Prevention**: Never repeats previously featured papers
- 💰 **100% Free**: Runs entirely on free services and APIs
- ⏰ **Automated**: Runs every Friday at 6 PM UTC via GitHub Actions

## 🚀 How It Works

1. **Paper Discovery**: Fetches papers from arXiv across AI/ML categories
2. **Social Media Scraping**: Searches for mentions across all platforms in last 7 days
3. **Engagement Scoring**: Calculates weighted scores based on mentions, replies, and likes
4. **Intelligent Ranking**: Sorts papers by total social engagement score
5. **Content Generation**: Creates summaries and formats beautiful email
6. **Auto-Publishing**: Sends to Substack and updates processed papers database

## 📊 Engagement Scoring System

Papers are ranked using social media engagement from the **last 7 days only**:

### Platform Weights & Metrics:
- **Twitter/X (Weight: 3.0)**
  - Mentions × 10 + Replies × 5 + Likes × 2
- **Reddit (Weight: 2.5)**  
  - Posts × 15 + Comments × 3 + Upvotes × 1
- **Hacker News (Weight: 2.0)**
  - Mentions × 20 + Comments × 4 + Points × 2
- **GitHub (Weight: 1.5)**
  - Repositories × 25 + Forks × 5 + Stars × 1

### Why This Approach?
- 📈 **Real-time relevance** - captures what's hot right now
- 🗣️ **Community-driven** - reflects actual researcher interest
- 🔄 **Discussion-focused** - values engagement over citations
- ⚡ **Trend detection** - spots viral papers early

## 🛠️ Prerequisites

- GitHub account
- Gmail account with 2FA enabled
- Substack publication

## ⚙️ Setup Instructions

### 1. Fork the Repository
Click the "Fork" button to create your own copy.

### 2. Configure Gmail App Password
1. Enable 2FA on Gmail: [Google Account Security](https://myaccount.google.com/security)
2. Generate App Password: Security → App passwords
3. Save the 16-character password

### 3. Get Your Substack Email
1. Substack Dashboard → Settings → Publication details
2. Copy the email address (format: `yourname-123abc@substack.com`)

### 4. Set GitHub Secrets
Go to Settings → Secrets and variables → Actions, add:

```
GMAIL_EMAIL = your_gmail@gmail.com
GMAIL_PASSWORD = your_16_character_app_password  
SUBSTACK_EMAIL = yourname-123abc@substack.com
```

### 5. Test Your Setup
1. Actions → Weekly AI Papers → Run workflow
2. Check logs for any errors
3. Verify Substack receives the digest

🎉 **Done!** Your agent runs automatically every Friday.

## 📄 Sample Output

```
🤖 Top 5 AI Papers This Week
Week of August 02, 2025

Papers ranked by social media engagement in the last 7 days

🥇 #1. GPT-5: The Next Generation of Language Models
Authors: OpenAI Research Team, et al.
🔥 Social Engagement Score: 1,247.3

This groundbreaking paper introduces GPT-5, featuring unprecedented 
reasoning capabilities and multimodal understanding. The model 
demonstrates significant improvements in mathematical reasoning...

🥈 #2. Quantum Neural Networks: A New Paradigm  
Authors: Chen, Kumar, Williams, et al.
🔥 Social Engagement Score: 892.1

Researchers present a novel approach combining quantum computing 
with neural networks, achieving exponential speedups on certain
machine learning tasks...
```

## 🔧 Customization Options

### Change ArXiv Categories
Edit categories in `ai_papers_agent.py`:
```python
self.categories = [
    "cs.AI",    # Artificial Intelligence
    "cs.LG",    # Machine Learning  
    "cs.CV",    # Computer Vision
    "cs.CL",    # Natural Language Processing
    "cs.NE",    # Neural Networks
    "stat.ML"   # Statistics ML
]
```

### Modify Engagement Weights
Adjust platform weights in `calculate_social_score()`:
```python
score = (
    twitter_engagement * 3.0 +    # Twitter weight
    reddit_engagement * 2.5 +     # Reddit weight  
    hn_engagement * 2.0 +         # HN weight
    github_engagement * 1.5       # GitHub weight
)
```

### Change Schedule
Update `.github/workflows/weekly-papers.yml`:
```yaml
schedule:
  - cron: '0 18 * * 5'  # Friday 6 PM UTC
  # - cron: '0 12 * * 1'  # Monday noon UTC  
```

### Adjust Number of Papers
Change the slice in `run()` method:
```python
top_papers = ranked_papers[:5]  # Top 5 papers
# top_papers = ranked_papers[:10]  # Top 10 papers
```

## 🏗️ Technical Architecture

- **Runtime**: Python 3.9+ on GitHub Actions
- **Data Sources**: 
  - arXiv API for paper metadata
  - Nitter instances for Twitter data
  - Reddit API for discussions
  - Hacker News Algolia API
  - GitHub API for repository mentions
- **Database**: SQLite for duplicate prevention
- **Email**: Gmail SMTP to Substack
- **Rate Limiting**: Built-in delays to avoid blocking

## 📦 Dependencies

Core libraries used:
- `arxiv` - arXiv API client for paper fetching
- `requests` - HTTP requests for social media APIs
- `beautifulsoup4` - HTML parsing for web scraping
- `lxml` - Fast XML/HTML parsing
- `sqlite3` - Database for tracking processed papers
- `smtplib` - Email sending via Gmail
- `urllib3` - URL handling and encoding

## 🐛 Troubleshooting

### Common Issues

**No papers with engagement found**
- Social media platforms may be rate limiting
- Try running at different times
- Check if search terms are working

**Gmail authentication errors**  
- Verify 2FA is enabled
- Regenerate App Password
- Check email/password in secrets

**Substack not receiving emails**
- Confirm Substack email format is correct
- Check spam folder
- Verify publication email in Substack settings

**Social media scraping failures**
- Some platforms may block requests
- Agent will continue with available data
- Check logs for specific error messages

### Performance Metrics
- **Processing Time**: 15-25 minutes per run
- **Papers Analyzed**: 100-200 per week  
- **Social Platforms Checked**: 4 (Twitter, Reddit, HN, GitHub)
- **Success Rate**: ~90% (depends on platform availability)
- **Engagement Detection**: Real-time (last 7 days)

## 🎯 What Makes This Different

Traditional academic paper ranking focuses on:
- Citation counts (slow to accumulate)
- Journal prestige (gatekeeping)  
- Author reputation (bias toward established researchers)

**Our social engagement ranking captures:**
- ✅ Real-time community interest
- ✅ Practical impact and applicability  
- ✅ Discussion and debate volume
- ✅ Cross-platform viral potential
- ✅ Developer and practitioner adoption

This gives you papers that are **actually making waves** in the AI community right now.

## 🤝 Contributing

Contributions welcome! Ideas for enhancement:

**Data Sources:**
- YouTube mentions and comments
- LinkedIn professional discussions  
- Discord server mentions
- Slack workspace discussions

**Analytics:**
- Trending topic detection
- Sentiment analysis of discussions
- Geographic engagement mapping
- Influencer mention tracking

**Features:**
- Multiple digest formats (daily, monthly)
- Custom topic filtering  
- Personalized paper recommendations
- RSS feed generation

## 📈 Roadmap

- [ ] Add sentiment analysis of social mentions
- [ ] Include paper reproducibility scores
- [ ] Track engagement trends over time
- [ ] Support for multiple languages
- [ ] Integration with academic Twitter lists
- [ ] Paper discussion summary generation

## 📝 License

MIT License - Feel free to use, modify, and distribute!

## 🙏 Acknowledgments

- **arXiv** for open access to research papers
- **Social Media Platforms** for providing engagement data
- **GitHub Actions** for free automated hosting
- **Nitter Community** for privacy-focused Twitter access
- **AI Research Community** for creating amazing work to showcase

---

## 🔍 FAQ

**Q: Why focus on social media engagement over citations?**
A: Citations take months/years to accumulate. Social engagement shows immediate impact and community interest, helping you discover important papers as they emerge.

**Q: What if a paper has no social media mentions?**  
A: Papers with zero engagement are filtered out. The digest only includes papers that are actively being discussed.

**Q: Can I run this more frequently than weekly?**
A: Yes! Edit the cron schedule, but be mindful of rate limits on social media platforms.

**Q: Does this work for papers older than a week?**
A: Absolutely! Paper age doesn't matter - only whether it's getting social engagement in the last 7 days.

---

**Built with ❤️ for discovering trending AI research**

⭐ Star this repo if it helps you stay current with AI trends!

*Last updated: August 2025*
