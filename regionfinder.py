import pyautogui
import time 

print("Move your mouse to top-left of the words area... waiting 3s")
time.sleep(3)
top_left = pyautogui.position()
print("Top-left:", top_left)

time.sleep(2)
print("Now move your mouse to bottom-right of the words area... waiting 3s")
time.sleep(3)
bottom_right = pyautogui.position()
print("Bottom-right:", bottom_right)

# Optional: Print the region tuple you need for the main script
region = (
    top_left.x,
    top_left.y,
    bottom_right.x - top_left.x,
    bottom_right.y - top_left.y
)
print("🟩 Region to copy into your script:", region)
