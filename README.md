# 🔄 Android ROM Source Tracker

> **Automatically track and visualize recent commits across Custom Android ROM repositories**

A GitHub Actions-powered tool that monitors source code changes across multiple Custom ROM projects.  
It provides developers and enthusiasts with an up-to-date view of development activity.

## ⚙️ How It Works

- All ROM data is stored in `roms_config.yaml`  
- GitHub Actions automatically:
  - Sync repositories  
  - Process commit data  
  - Update the web interface  
- Fully self-maintaining—no manual intervention needed

## 📊 Data Updates

- **Frequency:** Every 24 hours  
- **Commit window:** Last 90 days for each repo  
- **Update time:** 00:00 UTC daily

## 🚫 AOSP Source Exclusion

This tracker **excludes AOSP repositories** to save storage and stay within GitHub Runner limits.

## 🔧 Adding a New ROM

To track a new ROM:

1. Add it to `roms_config.yaml`  
2. Submit a pull request  

**Example entry:**
- `id`: `my-rom`  
- `display_name`: `My Custom ROM`  
- `manifest_url`: `https://github.com/my-rom/manifest.git`  
- `branches`: `main`, `development`
