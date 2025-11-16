# 🚀 QUICK START - Deploy GRIMM to Railway

## Files Ready for Deployment ✅

All the files you need are ready! Here's what each one does:

- **index.html** - Your website (auto-loads data from server)
- **app.py** - Flask server (API key stored server-side)
- **requirements.txt** - Python packages needed
- **gamelog.json** - Game results and spreads
- **teamid.json** - Team ID mappings  
- **rosters.json** - Manager rosters and lineups
- **logos/** folder - Team logos (you need to include this!)
- **Procfile** - Tells Railway how to start the app
- **runtime.txt** - Specifies Python 3.11
- **.gitignore** - Keeps unnecessary files out of GitHub
- **README.md** - Full documentation

## 3-Minute Deployment Steps

### 1️⃣ Create GitHub Repository
- Go to https://github.com
- Click "+" → "New repository"
- Name: `grimm-basketball`
- Click "Create repository"

### 2️⃣ Upload Your Files
- Click "uploading an existing file"
- **IMPORTANT:** Upload ALL files including the `logos` folder!
- Commit changes

### 3️⃣ Deploy to Railway
- Go to https://railway.app
- Login with GitHub
- Click "New Project" → "Deploy from GitHub repo"
- Select `grimm-basketball`
- Wait for deployment (~2 minutes)

### 4️⃣ Add Your KenPom API Key
- In Railway, click your project
- Go to "Variables" tab
- Click "New Variable"
- Name: `KENPOM_API_KEY`
- Value: [paste your KenPom API key]
- Click "Add"

### 5️⃣ Get Your URL
- Go to "Settings" tab
- Scroll to "Domains"
- Click "Generate Domain"
- Copy the URL (like: `https://grimm-basketball-production.up.railway.app`)

### 6️⃣ Share with League!
- Send the URL to your league managers
- They can visit and see everything - no setup needed!

---

## ⚡ Key Changes Made

**For League Managers (they don't need to):**
- ❌ Upload any files
- ❌ Enter API keys
- ❌ Configure anything
- ✅ Just visit the URL and everything works!

**How it works:**
- JSON files load automatically from the server
- KenPom API key stored as environment variable (secure!)
- All data persists even after browser refresh
- You update data by updating files in GitHub

---

## 🔄 To Update Game Data Later

1. Go to your GitHub repo
2. Click the file (e.g., `gamelog.json`)
3. Click pencil icon to edit
4. Make changes
5. Commit
6. Railway auto-redeploys in ~2 minutes

---

## 📁 Don't Forget!

**CRITICAL:** Make sure you upload your `logos` folder with all the .webp files!
- The folder should contain files like: `1.webp`, `4.webp`, `11.webp`, etc.
- Without logos, team images won't display (but everything else will work)

---

See README.md for full documentation and troubleshooting!
