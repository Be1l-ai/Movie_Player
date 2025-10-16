# MovieForCutie - Render Deployment Guide 🎬

## Quick Deploy to Render

### Option 1: Deploy with Blueprint (Recommended) ✨

1. **Push your code to GitHub** (already done!)
   ```bash
   git add .
   git commit -m "Add Render deployment configuration"
   git push origin main
   ```

2. **Go to Render Dashboard**
   - Visit: https://dashboard.render.com/
   - Click **"New +"** → **"Blueprint"**

3. **Connect Repository**
   - Select **"MovieForCutie"** repository
   - Render will automatically detect `render.yaml`
   - Click **"Apply"**

4. **Set Environment Variables**
   - In the Render dashboard, go to your service
   - Navigate to **"Environment"** tab
   - Add: `OMDB_API_KEY` = `your_actual_api_key`

5. **Deploy!** 🚀
   - Render will automatically build and deploy
   - Your app will be live at: `https://movieforcutie.onrender.com`

---

### Option 2: Manual Web Service Setup

1. **Create New Web Service**
   - Go to https://dashboard.render.com/
   - Click **"New +"** → **"Web Service"**

2. **Connect Repository**
   - Select your **MovieForCutie** repo
   - Click **"Connect"**

3. **Configure Service**
   ```
   Name: movieforcutie
   Region: Oregon (US West)
   Branch: main
   Root Directory: movie
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn --chdir src main:app
   Plan: Free
   ```

4. **Add Environment Variables**
   - Click **"Advanced"** → **"Add Environment Variable"**
   - Key: `OMDB_API_KEY`
   - Value: Your OMDB API key from https://www.omdbapi.com/apikey.aspx

5. **Create Web Service**
   - Click **"Create Web Service"**
   - Wait for deployment (2-3 minutes)

---

## Files Created for Deployment 📁

- **`requirements.txt`** - Python dependencies
- **`render.yaml`** - Render Blueprint configuration
- **`runtime.txt`** - Python version specification
- **`.env.example`** - Environment variables template
- **`RENDER_DEPLOY.md`** - This deployment guide

---

## Environment Variables Required 🔑

| Variable | Description | Required |
|----------|-------------|----------|
| `OMDB_API_KEY` | API key from OMDb | ✅ Yes |

Get your free API key: https://www.omdbapi.com/apikey.aspx

---

## Troubleshooting 🔧

### Build Fails
```bash
# Check requirements.txt is in the correct location
ls -la movie/requirements.txt

# Verify Python version
cat movie/runtime.txt
```

### Application Crashes
- Check logs in Render dashboard: **"Logs"** tab
- Verify `OMDB_API_KEY` is set correctly
- Ensure all dependencies are in `requirements.txt`

### Static Files Not Loading
- Verify `static/` folder is in `movie/src/`
- Check Flask static folder configuration

### Health Check Failing
- Test endpoint: `https://your-app.onrender.com/health`
- Should return: `{"status": "healthy", "message": "MovieForCutie is running!"}`

---

## Local Testing Before Deploy 🧪

```bash
# Navigate to movie directory
cd movie

# Install dependencies
pip install -r requirements.txt

# Create .env file from example
cp .env.example .env
# Edit .env and add your OMDB_API_KEY

# Run with Gunicorn (same as production)
gunicorn --chdir src main:app --bind 0.0.0.0:5000

# Test in browser
# Visit: http://localhost:5000
```

---

## Automatic Deployments 🔄

Render automatically redeploys when you push to `main` branch:

```bash
git add .
git commit -m "Update features"
git push origin main
# ✅ Render will automatically deploy!
```

---

## Custom Domain (Optional) 🌐

1. Go to your service settings in Render
2. Click **"Settings"** → **"Custom Domain"**
3. Add your domain (e.g., `movieforcutie.com`)
4. Update DNS records as instructed by Render

---

## Monitoring 📊

- **Logs**: Real-time in Render dashboard
- **Metrics**: CPU, Memory usage in dashboard
- **Health Check**: `/health` endpoint

---

## Free Tier Limitations ⚠️

- Service spins down after 15 minutes of inactivity
- First request after spin-down takes ~30 seconds
- 750 hours/month free compute time

### Upgrade to Paid Plan for:
- No spin-down
- Faster performance
- More compute resources

---

## Support 💬

- **Render Docs**: https://render.com/docs
- **OMDb API Docs**: https://www.omdbapi.com/
- **Flask Docs**: https://flask.palletsprojects.com/

---

## Deployment Checklist ✅

- [ ] Push code to GitHub
- [ ] Get OMDB API key
- [ ] Create Render account
- [ ] Connect GitHub repository
- [ ] Configure environment variables
- [ ] Deploy service
- [ ] Test live URL
- [ ] Check health endpoint
- [ ] Test movie search functionality

---

**Made with 💖 for Akiii** 
**(˶ᵔ ᵕ ᵔ˶)**
