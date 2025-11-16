# GRIMM - College Basketball Fantasy League

A fantasy college basketball league tracker where managers draft teams and compete based on game results against the spread.

## 🚀 Deploying to Railway.app

### Step 1: Prepare Your Files

You need these files in a folder (you already have them):
- `index.html` - The website frontend
- `app.py` - Flask backend server
- `requirements.txt` - Python dependencies
- `gamelog.json` - Game results and spreads
- `teamid.json` - Team ID mappings
- `rosters.json` - Manager rosters and weekly lineups
- `logos/` folder - Team logos (*.webp files)
- `Procfile` - Tells Railway how to run the app
- `runtime.txt` - Specifies Python version

### Step 2: Create a GitHub Repository

1. Go to https://github.com and sign in (or create account)
2. Click the "+" in top right → "New repository"
3. Name it: `grimm-basketball` (or whatever you want)
4. Choose "Public" (easier) or "Private" (more secure)
5. Click "Create repository"

### Step 3: Upload Your Files to GitHub

**Option A: Use GitHub Web Interface (Easiest)**
1. On your new repository page, click "uploading an existing file"
2. Drag and drop ALL your files into the upload area
   - Make sure to include the `logos` folder with all the .webp files!
3. Scroll down and click "Commit changes"

**Option B: Use GitHub Desktop (If you prefer)**
1. Download GitHub Desktop from https://desktop.github.com/
2. Clone your repository
3. Copy all your files into the repository folder
4. Commit and push

### Step 4: Deploy to Railway

1. Go to https://railway.app/
2. Click "Login" → Sign in with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your `grimm-basketball` repository
6. Railway will automatically detect it's a Flask app and start deploying!

### Step 5: Configure Environment Variables

1. In Railway, click on your deployed project
2. Go to the "Variables" tab
3. Click "New Variable"
4. Add:
   - **Variable name:** `KENPOM_API_KEY`
   - **Value:** [Your KenPom API Key]
5. Click "Add"

The app will automatically redeploy with the API key.

### Step 6: Get Your URL

1. In Railway, go to the "Settings" tab
2. Scroll to "Domains"
3. Click "Generate Domain"
4. Railway will give you a URL like: `https://grimm-basketball-production.up.railway.app`

**That's your website URL!** Share it with your league managers.

---

## 📝 Updating Game Data

When you need to update scores, rosters, or other data:

### Method 1: Through GitHub (Recommended)
1. Go to your GitHub repository
2. Click on the file you want to update (e.g., `gamelog.json`)
3. Click the pencil icon (Edit)
4. Make your changes
5. Scroll down and click "Commit changes"
6. Railway will automatically redeploy with the new data (takes ~2 minutes)

### Method 2: Re-upload
1. In GitHub, click "Add file" → "Upload files"
2. Upload your updated JSON files
3. Commit changes
4. Railway auto-redeploys

---

## 🎯 How It Works for League Managers

Your league managers just need to:
1. Visit the URL you give them
2. Click around - everything loads automatically
3. No uploads, no API keys, no setup needed!

Features they can access:
- **Standings** - Season and weekly standings
- **Managers** - View all rosters and lineups
- **Schedule** - See weekly matchups
- **KenPom** - View team rankings (just click "Load Rankings")

---

## 🔧 Troubleshooting

**"Application Error" when visiting the site:**
- Check Railway logs (click on your project → "Deployments" → click latest deployment → "View Logs")
- Make sure all files uploaded correctly to GitHub
- Verify `KENPOM_API_KEY` environment variable is set

**KenPom rankings won't load:**
- Check that `KENPOM_API_KEY` is set correctly in Railway Variables
- Make sure your KenPom subscription is active
- Check Railway logs for errors

**Logos not showing:**
- Make sure the `logos` folder with all .webp files is in your GitHub repo
- File names should match the team IDs (e.g., `113.webp` for Houston)

**Data not updating:**
- After uploading new files to GitHub, wait 1-2 minutes for Railway to redeploy
- Check Railway "Deployments" tab to see if it's still deploying
- Try clearing your browser cache and refreshing

---

## 💰 Cost

Railway free tier includes:
- $5 of usage per month
- This app should easily stay within free tier
- If you exceed, they'll email you

---

## 📧 Need Help?

If you run into issues:
1. Check Railway logs first
2. Make sure all files are in GitHub
3. Verify environment variables are set
4. Railway has great documentation at https://docs.railway.app/

Good luck with your league! 🏀
