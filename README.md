<h1 align="center"><a href="https://github.com/ronknight/get-saved-wifi-password">Get Saved WiFi Password</a></h1>
<h4 align="center">This Python script retrieves and displays the names and passwords of all saved WiFi profiles on a Windows machine.
</h4>

<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://github.com/ronknight/ronknight/stargazers"><img src="https://img.shields.io/github/stars/BEPb/BEPb.svg?logo=github"></a>
<a href="https://github.com/ronknight/ronknight/network/members"><img src="https://img.shields.io/github/forks/BEPb/BEPb.svg?color=blue&logo=github"></a>
  <a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
<a href="https://github.com/ronknight/get-saved-wifi-password/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/ronknight/get-saved-wifi-password/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
<a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>

<p align="center">
  <a href="#requirements">📋 Requirements</a> •
  <a href="#usage">🚀 Usage</a> •
  <a href="#script">📜 Script</a> •
  <a href="#disclaimer">⚠️ Disclaimer</a> •
  <a href="#diagrams">📊 Diagrams</a>
</p>

---

## 📊 Diagrams

Here's a workflow diagram of how the Brand Search application works:

```mermaid
graph TD
    A[Start] --> B[Load Environment Variables]
    B --> C[Get Domain from Command Line]
    C --> D[Fetch Brand Data]
    D --> E{API Key Exists?}
    E -->|No| F[Show Error]
    E -->|Yes| G[Make API Request]
    G --> H{Response Success?}
    H -->|Yes| I[Parse JSON Data]
    I --> J[Save to Output File]
    H -->|No| K[Show Error Message]
    J --> L[End]
    K --> L
    F --> L
```

## 📋 Requirements

- Python 3.6+
- requests
- python-dotenv
- Valid Brandfetch API key

## 🚀 Usage

1. Create a `.env` file with your Brandfetch API key:
```
BRANDFETCH_API_KEY=your_api_key_here
```

2. Run the script with a domain:
```bash
python brand_fetch.py example.com
```

## 📜 Script

The script performs the following operations:
- Loads environment variables from `.env` file
- Takes a domain name as command line argument
- Fetches brand data from Brandfetch API
- Saves the response to a JSON file in the output directory

## ⚠️ Disclaimer

This script requires a valid Brandfetch API key to function. Please ensure you have the necessary API access before using the script.
