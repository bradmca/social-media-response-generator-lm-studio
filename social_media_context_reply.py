import time
import requests
import pyperclip
import keyboard
import subprocess
import sys
import os
import json
from pathlib import Path

# --- Configuration ---
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
MODEL_NAME = "meta-llama-3.1-8b-instruct"
LM_STUDIO_CLI = "lms"  # Command for LM Studio CLI

# Global variable to store the original post
current_post_context = ""

SYSTEM_PROMPT = """
You are a professional social media networking assistant.
You will be provided with a 'Original Post' (context) and a 'User Comment'.
Your goal is to write a reply to the comment that is relevant to the original post.

Guidelines:
- Keep replies concise (under 3 sentences).
- Use British spelling (e.g. 'analyse', 'colour', 'behaviour').
- Be friendly but professional.
- Address the specific point the commenter made.
- Do not output the context, just the reply.
"""

def check_lm_studio_running():
    """Check if LM Studio is running and accessible."""
    try:
        response = requests.get(f"{LM_STUDIO_URL.replace('/chat/completions', '/models')}", timeout=2)
        return response.status_code == 200
    except:
        return False

def start_lm_studio():
    """Attempt to start LM Studio."""
    print("🚀 Attempting to start LM Studio...")
    
    # Try to start LM Studio using the lms CLI
    try:
        # First check if lms command is available
        subprocess.run([LM_STUDIO_CLI, "--version"], capture_output=True, check=True, timeout=5)
        print("✅ LM Studio CLI found")
        
        # Start the server
        print("Starting LM Studio server...")
        subprocess.Popen([LM_STUDIO_CLI, "server", "start"], 
                        creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == 'nt' else 0)
        
        # Wait for server to be ready
        print("Waiting for server to start...")
        for i in range(30):  # Wait up to 30 seconds
            time.sleep(1)
            if check_lm_studio_running():
                print("✅ LM Studio server started successfully!")
                return True
            print(f".", end="", flush=True)
        
        print("\n⚠️ Server started but not yet accessible. Continuing anyway...")
        return True
        
    except subprocess.CalledProcessError:
        print("❌ LM Studio CLI not found. Please ensure LM Studio is installed.")
        print("   You can download it from: https://lmstudio.ai/")
        return False
    except FileNotFoundError:
        print("❌ LM Studio CLI not found in PATH.")
        print("   Please ensure LM Studio is installed and the CLI is in your PATH.")
        return False
    except Exception as e:
        print(f"❌ Error starting LM Studio: {e}")
        return False

def load_model():
    """Load the specified model in LM Studio."""
    print(f"📦 Loading model: {MODEL_NAME}")
    
    try:
        # Check if model is already loaded
        result = subprocess.run([LM_STUDIO_CLI, "ps"], capture_output=True, text=True, timeout=10)
        if MODEL_NAME in result.stdout:
            print(f"✅ Model {MODEL_NAME} is already loaded")
            return True
        
        # Load the model
        subprocess.run([LM_STUDIO_CLI, "load", MODEL_NAME], check=True, timeout=30)
        print(f"✅ Model {MODEL_NAME} loaded successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error loading model: {e}")
        print(f"   Please ensure you have downloaded '{MODEL_NAME}' in LM Studio")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def get_loaded_model_name():
    """Get the actual model name from LM Studio's API."""
    try:
        response = requests.get(f"{LM_STUDIO_URL.replace('/chat/completions', '/models')}", timeout=5)
        response.raise_for_status()
        models = response.json().get('data', [])
        
        # Find the loaded model (usually the first one)
        if models:
            for model in models:
                if model.get('object') == 'model':
                    # Return the model ID as it should be used in requests
                    return model.get('id')
        
        return None
    except:
        return None

def initialize_lm_studio():
    """Initialize LM Studio, start server, and load model."""
    if not check_lm_studio_running():
        if not start_lm_studio():
            print("\n⚠️ Could not start LM Studio automatically.")
            print("   Please start LM Studio manually and ensure the server is running on port 1234")
            input("Press Enter to continue anyway...")
            return
    
    # Wait a bit more for the server to be fully ready
    time.sleep(2)
    
    # Try to load the model
    if not load_model():
        print("\n⚠️ Could not load the model automatically.")
        print("   You can still use the script, but you'll need to load the model manually in LM Studio")

def save_post_context():
    """Reads clipboard and saves it as the Context/Original Post."""
    global current_post_context
    text = pyperclip.paste()
    
    if not text or len(text.strip()) < 5:
        print("Clipboard text is too short to be a post.")
        return

    current_post_context = text
    # Visual feedback in console
    print("\n" + "="*30)
    print("✅ ORIGINAL POST SAVED TO MEMORY")
    print(f"Preview: {current_post_context[:60]}...")
    print("Now you can copy comments and press Ctrl+Alt+R")
    print("="*30 + "\n")

def generate_reply_with_context():
    """Reads clipboard (comment), combines with saved context, sends to AI."""
    global current_post_context
    
    comment_text = pyperclip.paste()
    
    if not comment_text or len(comment_text.strip()) < 2:
        print("Clipboard is empty or too short!")
        return

    # Check if we actually have a post saved
    if not current_post_context:
        print("⚠️ WARNING: No Original Post saved! Reply might be generic.")
        print("Tip: Copy your post and press Ctrl+Alt+C first.")
    
    print(f"\n--- Generating reply for comment: ---\n{comment_text[:50]}...")

    # Get the actual model name from LM Studio
    actual_model_name = get_loaded_model_name()
    if not actual_model_name:
        print("⚠️ Warning: Could not detect loaded model. Using default model name.")
        actual_model_name = MODEL_NAME
    else:
        print(f"Using model: {actual_model_name}")

    # Construct the user prompt with both pieces of information
    user_message = (
        f"ORIGINAL POST CONTEXT:\n{current_post_context}\n\n"
        f"USER COMMENT TO REPLY TO:\n{comment_text}"
    )

    payload = {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7,
        "max_tokens": 150,
        "stream": False,
        "model": actual_model_name
    }

    try:
        response = requests.post(LM_STUDIO_URL, json=payload)
        response.raise_for_status()
        
        result = response.json()
        reply = result['choices'][0]['message']['content'].strip()
        
        pyperclip.copy(reply)
        print(f"\n>>> REPLY COPIED TO CLIPBOARD <<<\n{reply}\n")
        
    except requests.exceptions.HTTPError as e:
        print(f"\n❌ HTTP Error: {e}")
        if e.response.status_code == 400:
            try:
                error_detail = e.response.json()
                print(f"Error details: {error_detail}")
            except:
                print(f"Response text: {e.response.text}")
        print("Please check the model name and LM Studio configuration.")
    except Exception as e:
        print(f"Error: {e}")
        print("Please ensure LM Studio is running with the model loaded.")

# --- Main Execution ---
if __name__ == "__main__":
    print("🤖 Social Media Context Reply Bot")
    print("="*40)
    
    # Initialize LM Studio automatically
    initialize_lm_studio()
    
    print("\n--- Hotkeys ---")
    print("1. Highlight your Post text -> Copy -> Press 'Ctrl+Alt+C' (Save Context)")
    print("2. Highlight a Comment -> Copy -> Press 'Ctrl+Alt+R' (Generate Reply)")
    print("\nPress 'Esc' to quit")
    print("="*40 + "\n")

    # Hotkey to save the "Parent" post
    keyboard.add_hotkey('ctrl+alt+c', save_post_context)

    # Hotkey to generate the reply to a comment
    keyboard.add_hotkey('ctrl+alt+r', generate_reply_with_context)

    keyboard.wait('esc')
else:
    # --- Hotkeys ---
    print("Social Media Context Bot is running...")
    print("1. Highlight your Post text -> Copy -> Press 'Ctrl+Alt+C' (Save Context)")
    print("2. Highlight a Comment -> Copy -> Press 'Ctrl+Alt+R' (Generate Reply)")

    # Hotkey to save the "Parent" post
    keyboard.add_hotkey('ctrl+alt+c', save_post_context)

    # Hotkey to generate the reply to a comment
    keyboard.add_hotkey('ctrl+alt+r', generate_reply_with_context)

    keyboard.wait('esc')