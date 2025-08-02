# AI Papers Agent Setup Guide

## 🚀 Complete Setup Instructions

Follow these steps to get your free AI papers agent running on GitHub Actions.

## Step 1: Create Repository

1. **Create a new GitHub repository**
   - Go to GitHub and create a new public repository
   - Name it something like `ai-papers-agent`
   - Initialize with a README

2. **Upload the files**
   - Create the following files in your repository:
     - `main.py` (the main script)
     - `requirements.txt` (Python dependencies)
     - `.github/workflows/weekly-papers.yml` (GitHub Actions workflow)
   - Create an empty `published_papers.db` file (will be used by the script)

## Step 2: Set Up Gmail App Password

1. **Enable 2-Factor Authentication on Gmail**
   - Go to your Google Account settings
   - Security → 2-Step Verification → Turn on

2. **Generate App Password**
   - Go to Google Account → Security → App passwords
   - Select "Mail" and your device
   - Copy the 16-character password (save this!)

## Step 3: Find Your Substack Email

1. **Get your Substack publication email**
   - Go to your Substack dashboard
   - Settings → Publication details
   - Look for "Email address" - it looks like `yourname-123abc@substack.com`
   - Copy this email address

## Step 4: Get Hugging Face Token (Optional but Recommended)

1. **Create free Hugging Face account**
   - Go to https://huggingface.co/join
   - Sign up for free

2. **Generate access token**
   - Go to Settings → Access Tokens
   - Create new token with "Read" permissions
   - Copy the token (starts with `hf_`)

## Step 5: Configure GitHub Secrets

1. **Go to your repository on GitHub**
   - Click Settings → Secrets and variables → Actions

2. **Add the following secrets:**

   **Required secrets:**
   ```
   GMAIL_EMAIL = your_gmail@gmail.com
   GMAIL_PASSWORD = your_16_character_app_password
   SUBSTACK_EMAIL = yourname-123abc@substack.com
   ```

   **Optional (for better summaries):**
   ```
   HF_TOKEN = hf_your_hugging_face_token
   ```

## Step 6: Test the Setup

1. **Manual test run**
   - Go to Actions tab in your repository
   - Click "Weekly AI Papers" workflow
   - Click "Run workflow" → "Run workflow"
   - Watch the logs to ensure it works

2. **Check for issues**
   - Look for any error messages in the Actions log
   - Verify that `published_papers.db` was created/updated
   - Check your email to see if Substack received the post

## Step 7: Customize (Optional)

### Adjust the Schedule
Edit `.github/workflows/weekly-papers.yml`:
```yaml
schedule:
  # Run every Friday at 6 PM UTC
  - cron: '0 18 * * 5'
```

Change the cron expression:
- `0 18 * * 5` = Friday 6 PM UTC
- `0 21 * * 4` = Thursday 9 PM UTC
- `0 14 * * 6` = Saturday 2 PM UTC

### Modify Categories
In `main.py`, edit the `categories` list:
```python
categories = ["cs.AI", "cs.LG", "cs.CV", "cs.CL", "cs.NE", "stat.ML"]
```

Available arXiv categories:
- `cs.AI` - Artificial Intelligence
- `cs.LG` - Machine Learning  
- `cs.CV` - Computer Vision
- `cs.CL` - Computation and Language
- `cs.NE` - Neural Networks
- `cs.RO` - Robotics
- `stat.ML` - Statistics Machine Learning

### Adjust Scoring Weights
In the `calculate_paper_score()` function, modify weights:
```python
social_score = (
    twitter_data['mentions'] * 5 +      # Increase for more Twitter weight
    twitter_data['engagement'] * 0.1 +
    reddit_score * 2 +                  # Increase for more Reddit weight
    hn_score * 3 +                      # Hacker News weight
    github_stars * 0.8                  # GitHub implementation weight
)
```

## Troubleshooting

### Common Issues

**Gmail Authentication Error:**
- Make sure 2FA is enabled
- Use App Password, not regular password
- Check that GMAIL_EMAIL and GMAIL_PASSWORD secrets are set correctly

**No Papers Found:**
- Check if arXiv is accessible
- Verify the date range (script looks for past 7 days)
- Try running manually to see error messages

**Scraping Errors:**
- Some websites may be temporarily down
- Rate limiting is built in, but some sites may block requests
- The script will continue with partial data

**Substack Not Receiving Email:**
- Double-check your Substack email address
- Check spam folder
- Verify email was sent (check GitHub Actions logs)
- Try sending a test email to your Substack address

**GitHub Actions Failed:**
- Check the Actions tab for error logs
- Verify all secrets are set correctly
- Make sure repository has Actions enabled

### Debug Mode

To run with more verbose output, you can temporarily add debug prints:

```python
# Add this at the top of main.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Manual Testing

You can test locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export GMAIL_EMAIL="your_email@gmail.com"
export GMAIL_PASSWORD="your_app_password"
export SUBSTACK_EMAIL="your_substack_email@substack.com"
export HF_TOKEN="your_hf_token"

# Run the script
python main.py
```

## Expected Behavior

**Weekly Execution:**
1. Script runs every Friday at 6 PM UTC
2. Fetches papers from past 7 days
3. Analyzes social media mentions
4. Scores and ranks papers
5. Generates summaries
6. Sends formatted email to Substack
7. Updates database to prevent duplicates

**Email Format:**
- HTML-formatted with attractive styling
- Top 5 papers with rankings
- Author lists, publication dates, and links
- AI-generated or rule-based summaries
- Trending indicators and scores

**Database:**
- SQLite database tracks published papers
- Prevents same paper from appearing twice
- Automatically managed by GitHub Actions

## Cost Breakdown

**Completely Free:**
- ✅ GitHub Actions: 2,000 minutes/month free
- ✅ Gmail SMTP: Free
- ✅ arXiv API: Free
- ✅ Hugging Face API: Free tier
- ✅ Web scraping: Free
- ✅ SQLite: Free

**Monthly cost: $0** 🎉

## Support

If you run into issues:

1. Check the GitHub Actions logs first
2. Verify all secrets are correctly set
3. Test with a manual workflow run
4. Check that your Gmail app password works
5. Ensure your Substack email address is correct

The script includes extensive error handling and will continue running even if some data sources are temporarily unavailable.

## Next Steps

Once everything is working:

1. **Monitor the first few runs** to ensure quality
2. **Adjust scoring weights** based on your preferences  
3. **Customize the email template** if desired
4. **Share your Substack** with the AI community!

Your AI papers agent is now ready to automatically discover and publish the week's most interesting AI research! 🤖📚
