# ✅ Railway Deployment Checklist

## Before You Start
- [ ] Have a GitHub account (or create one at github.com)
- [ ] Have your KenPom API key ready
- [ ] Have all your files ready (download from Claude)

## Files to Upload to GitHub
- [ ] index.html
- [ ] app.py
- [ ] requirements.txt
- [ ] gamelog.json
- [ ] teamid.json
- [ ] rosters.json
- [ ] Procfile
- [ ] runtime.txt
- [ ] .gitignore
- [ ] README.md
- [ ] **logos folder with all .webp files** ⚠️ DON'T FORGET THIS!

## GitHub Setup
- [ ] Create new repository named "grimm-basketball"
- [ ] Upload all files (including logos folder)
- [ ] Verify all files are visible in the repo

## Railway Deployment
- [ ] Sign up at railway.app with GitHub
- [ ] Create new project
- [ ] Deploy from GitHub repo
- [ ] Select "grimm-basketball" repository
- [ ] Wait for initial deployment to complete

## Configuration
- [ ] Go to Variables tab in Railway
- [ ] Add variable: `KENPOM_API_KEY`
- [ ] Paste your KenPom API key as the value
- [ ] Save and wait for redeploy

## Get Your URL
- [ ] Go to Settings tab
- [ ] Click "Generate Domain"
- [ ] Copy the URL
- [ ] Test it by visiting in your browser

## Testing
- [ ] Visit your URL
- [ ] Check Standings page loads with data
- [ ] Check Managers page shows rosters
- [ ] Check Schedule page shows games
- [ ] Click KenPom → Load Rankings (should work without entering API key)
- [ ] Verify team logos appear

## Share with League
- [ ] Send URL to all league managers
- [ ] Tell them: "Just visit this URL - no setup needed!"

---

## If Something Goes Wrong

**Site shows "Application Error":**
1. Check Railway "Deployments" tab
2. Click latest deployment
3. View logs to see what failed
4. Common issues:
   - Missing files in GitHub
   - Forgot to upload logos folder
   - Environment variable not set

**KenPom won't load:**
1. Verify `KENPOM_API_KEY` is set in Railway Variables
2. Check your KenPom subscription is active
3. Look at Railway logs for API errors

**Logos not showing:**
1. Make sure logos folder is in GitHub repo
2. Check file names match team IDs (e.g., `113.webp`)
3. Files should be .webp format

---

## 🎉 You're Done!

Once all checkboxes are checked, your league is live!

Share this URL format with managers:
`https://your-app-name.up.railway.app`

They just visit it and everything works automatically!
