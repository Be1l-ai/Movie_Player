# 🚀 Quick Deploy - Copy & Paste

## Step 1: Get OMDB API Key
Visit: https://www.omdbapi.com/apikey.aspx
Choose: FREE (1,000 daily limit)

## Step 2: Deploy to Render

### Option A: Blueprint (Easiest) ✨
1. Go to: https://dashboard.render.com/
2. Click: **New +** → **Blueprint**
3. Select: **MovieForCutie** repository
4. Click: **Apply**
5. Add Environment Variable:
   - Key: `OMDB_API_KEY`
   - Value: [paste your key here]
6. Done! ✅

### Option B: Manual Deploy
1. https://dashboard.render.com/
2. **New +** → **Web Service**
3. Connect **MovieForCutie** repo
4. Settings:
   ```
   Root Directory: movie
   Build: pip install -r requirements.txt
   Start: gunicorn --chdir src main:app
   ```
5. Environment → Add:
   ```
   OMDB_API_KEY = your_key_here
   ```
6. **Create Web Service**

## Your Live URL
After deployment: `https://movieforcutie.onrender.com`

## Auto-Deploy on Push
```bash
git add .
git commit -m "updates"
git push origin main
# Render auto-deploys! ✨
```

## Test Locally
```bash
cd movie
pip install -r requirements.txt
gunicorn --chdir src main:app
# Visit: http://localhost:8000
```
