import os
import requests
import json
import time
from botcity.core import DesktopBot
from urllib3 import request


PROJECT_DIR = os.path.join(os.path.expanduser("~"), "Desktop", "tjm-project")
ICON_LABEL = "Notepad" 
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080


def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def ground_and_launch(bot, icon_label):
    print(f"Searching for '{icon_label}'...")
    
    for threshold in [0.95, 0.9, 0.8]:
        found = bot.find(icon_label, matching=threshold, waiting_time=1000)
        
        if found:
            print(f"   > Icon grounded! (Threshold: {threshold})")
            
            # Click Center
            cx = found[0] + found[2] / 2
            cy = found[1] + found[3] / 2
            bot.mouse_move(cx, cy)
            bot.click_at(cx, cy)
            bot.wait(200)
            
            # Launch
            bot.enter()
            
            # --- SAFETY FOCUS CLICK ---
            print("   > Waiting for Notepad to open...")
            bot.wait(400) 
            
            # Click center of screen to FORCE focus on Notepad
            bot.click_at(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            bot.wait(500)
            return True
            
    print("   > Icon not found.")
    return False

def write_save_clear(bot, title, body, post_id):
    """
    Writes content, Saves As, Clears.
    """
    content = f"Title: {title}\n\n{body}"

    # 1. Paste Content
    bot.paste(content)
    bot.wait(100) 
    
    # 2. Save As (Ctrl + Shift + S)
    bot.type_keys(["ctrl", "shift", "s"])
    bot.wait(100) # Wait for dialog
    
    # Define Path
    filename = f"post_{post_id}.txt"
    full_path = os.path.join(PROJECT_DIR, filename)
    
    # Delete old file
    if os.path.exists(full_path):
        try:
            os.remove(full_path)
        except:
            pass 

    # Type Path & Enter
    bot.paste(full_path)
    bot.wait(500)
    bot.enter()
    bot.wait(100) 
    
    # 3. Clear Screen
    bot.type_keys(["ctrl", "a"])
    bot.wait(100)
    bot.type_keys(["backspace"])
    bot.wait(500)



def main():
    bot = DesktopBot()
    ensure_directory(PROJECT_DIR)
    
    # 1. Launch Notepad
    print("Minimizing windows...")
    bot.type_keys(["win", "d"])
    bot.wait(1000)
    
    if not ground_and_launch(bot, ICON_LABEL):
        print("CRITICAL: Failed to launch Notepad. Exiting.")
        return

    print("Starting processing loop (1 to 10)...")

    # 2. THE LOOP
    for i in range(1, 11):
        print(f"--- Processing Post ID: {i} ---")
        
        
        try:

            response = requests.get(f"https://dragonball-api.com/api/characters/{i}" , timeout=10)
            print("Response: ", response )
            response.raise_for_status() # Check for HTTP errors
            print("Response Status: ", response)
            print("Response JSON: ", response.json())   
            
    
            post = response.json()
            title, body = post["name"], post["id"]
            time.sleep(10)
            
            
            # --- AUTOMATION ACTION ---
            write_save_clear(bot, title, body, i)
            print(f"   > Saved post_{i}.txt")
            
            bot.type_keys(["alt", "f4"])
            ground_and_launch(bot, ICON_LABEL)
            bot.wait(100)
            
        except requests.exceptions.RequestException as e:
            print(f"[Error] Failed to fetch posts: {e}")
            continue
        
        
        except Exception as e:
            print(f"   > Error on post {i}: {e}")
            continue

    # 3. Cleanup
    print("All tasks completed. Closing Notepad.")
    bot.type_keys(["alt", "f4"])


if __name__ == '__main__':
    main()