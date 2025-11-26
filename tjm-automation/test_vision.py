from botcity.core import DesktopBot
import os

# 1. Setup the bot
bot = DesktopBot()

# 2. Define the path clearly
path_to_icon = r"resources\notepad_icon.png"

# 3. Check if file exists (Good for debugging)
if not os.path.exists(path_to_icon):
    print("ERROR: File not found! Check your folder.")
else:
    print("File exists. Scanning screen...")

    # --- YOUR CODE LINE ---
    # We look for the icon for 2 seconds
    notepad = bot.find("Notepad.png", matching=0.9, waiting_time=2000)

    if notepad:
        print(f"SUCCESS! Found Notepad at: {notepad}")
        bot.click()
    else:
        print("FAILURE: Could not find the icon on the screen.")