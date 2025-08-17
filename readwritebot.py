import pyautogui
import pytesseract
from PIL import Image
import time

# Global region variables
first_region  = (75, 460, 1360, 153) # The main loop
looping_region = (75, 500, 1360, 108) # Don't care if no looping 

def get_typing_text(region):

    screenshot = pyautogui.screenshot(region=region)
    screenshot = screenshot.convert('L')
    text = pytesseract.image_to_string(screenshot, config='--psm 6')
    return text.strip().replace('\n', ' ')

def type_text(text):
    pyautogui.write(text, interval=0.007) # Change interval to adjust typing speed
    return True

def get_duration_choice():
    while True:
        print("⏱ Choose how long the script should run:")
        print("1. 30 seconds")
        print("2. 1 minute")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            return 30
        elif choice == "2":
            return 60
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")

def main():
    duration = get_duration_choice()

    input("👉 Press Enter when ready...")
    print("⏳ You have 3 seconds to focus the input box...")
    time.sleep(3)

    is_first_round = True
    start_time = time.time()

    while True:
        elapsed = time.time() - start_time
        if elapsed >= duration:
            print(f"⏱ Time is up ({duration} seconds). Stopping.")
            break

        # Choose region based on first vs subsequent loops
        region = first_region if is_first_round else looping_region

        if is_first_round:
            pyautogui.press('backspace')
            time.sleep(0.05)

        text = get_typing_text(region)
        print("📖 Detected:", repr(text))

        if not text:
            print("⚠️ No text detected. Stopping early.")
            break

        # Guard before typing
        if time.time() - start_time >= duration:
            print("⛔ Time exceeded before typing started. Aborting.")
            break

        # Print detected text
        type_text(text)

        # Guard after typing
        if time.time() - start_time >= duration:
            print("⛔ Time exceeded after typing. Ending.")
            break

        # Press one extra space to advance so next capture shows two new lines
        pyautogui.press('space')

        # Final guard in case space pushed us over time
        if time.time() - start_time >= duration:
            print("⏱ Timer expired after advancing. Ending.")
            break

        is_first_round = False
        time.sleep(1)

    print(f"✅ Script ended after {round(time.time() - start_time, 2)} seconds.")
    time.sleep(2)

if __name__ == "__main__":
    main()
