
<img width="2816" height="1536" alt="Gemini_Generated_Image_dh9q4hdh9q4hdh9q" src="https://github.com/user-attachments/assets/99a16beb-7765-436c-a71b-d5eeb7f7571d" />

# Local Social Media Context Reply Bot 🤖🇬🇧

**A privacy-focused, undetectable clipboard bridge for generating context-aware social media replies using local LLMs.**

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![LM Studio](https://img.shields.io/badge/Backend-LM%20Studio-purple.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg)

<img width="890" height="517" alt="Screenshot 2026-01-29 121336" src="https://github.com/user-attachments/assets/2f2aa02f-763e-4b26-affb-4b05a3dcb678" />


## 🧐 What is this?

This is a lightweight Python script that acts as a bridge between your clipboard and **LM Studio** running on your local machine. 

Unlike browser extensions or Selenium bots, this tool **does not interact with social media APIs or HTML**. It works entirely through your system clipboard, making it:
1.  **Undetectable:** Social media platforms cannot detect bot activity because *you* are performing the copy/paste actions.
2.  **Private:** No data is sent to the cloud (OpenAI/Anthropic). Everything runs on your local hardware.
3.  **Context-Aware:** It "memorises" your original post so that replies to comments are relevant and specific, not generic.

## ✨ Features

* **Smart Context:** Feeds the original post text to the LLM so it understands *what* the commenter is replying to.
* **British English Default:** Configured to use British spelling and grammar (e.g., 'analyse', 'colour').
* **Clipboard-Based:** Highlight text, press a hotkey, and the reply is magically placed in your clipboard ready to paste.
* **Customisable Tone:** Easily edit the system prompt to match your professional voice.
* **🆕 Automatic LM Studio Management:** Automatically starts LM Studio server and loads the specified model on script launch.

## 🛠️ Prerequisites

1.  **[LM Studio](https://lmstudio.ai/)**: Installed on your machine (version 0.3.5 or later recommended).
2.  **Python 3.x**: Installed on your machine.
3.  **Downloaded Model**: Ensure you have downloaded `openai/gpt-oss-20b` (or your preferred model) in LM Studio.

## 📦 Installation

1.  Clone this repository:
    ```bash
    git clone https://github.com/bradmca/social-media-response-generator-lm-studio.git
    cd social-media-response-generator-lm-studio
    ```

2.  Install the required Python dependencies:
    ```bash
    pip install requests pyperclip keyboard
    ```

## ⚙️ Configuration

The script is configured to automatically:
1. Start the LM Studio server when launched
2. Load the model `openai/gpt-oss-20b` 

**To change the model:**
Edit `social_media_context_reply.py` and modify the `MODEL_NAME` variable:
```python
MODEL_NAME = "your/preferred-model-name"
```

**Manual override:** If LM Studio is already running, the script will detect it and use the existing instance.

## 🚀 How to Use

Run the script in your terminal:

```bash
python social_media_context_reply.py
```

**On first run:**
- The script will automatically detect if LM Studio is running
- If not, it will attempt to start LM Studio and load the specified model
- You'll see progress indicators as it starts up
- If any step fails, follow the on-screen instructions

**Once running:**
1. Highlight your social media post text → Copy → Press `Ctrl+Alt+C` to save it as context
2. Highlight a comment on your post → Copy → Press `Ctrl+Alt+R` to generate a reply
3. The reply will be automatically copied to your clipboard - just paste!

Press `Esc` to quit the script.

## 🔧 Troubleshooting

**LM Studio not found:**
- Ensure LM Studio is installed from https://lmstudio.ai/
- On Windows, the LM Studio CLI should be in your PATH automatically

**Model not loading:**
- Make sure you have downloaded the model in LM Studio first
- Check the model name matches exactly (case-sensitive)
- You can still use the script manually if auto-loading fails

**Server not starting:**
- Check if port 1234 is already in use
- Try starting LM Studio manually once, then run the script again
