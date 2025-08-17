# ReadWrite Bot

ReadWrite Bot reads text from a chosen area of your screen using OCR, then types it into an input field at a controllable speed.  
It works great for sites like Monkeytype for re-transcribing visible text, and it can also echo text from any app or window you select.

---

## Requirements

- **Python** 3.9 or newer  
- **Tesseract OCR** installed and on PATH  
  - macOS with Homebrew:  
    ```bash
    brew install tesseract
    ```
- Python packages listed in `requirements.txt`

---

## Quick Start

TL:DR
git clone then go to the path then 

mac:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Windows:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt



1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/readwrite-bot.git
   cd readwrite-bot
   
2. **Create and activate a virtual environment**
   On mac :
   
   python3 -m venv venv
   source venv/bin/activate

   On Windows :
   
   venv\Scripts\activate
3. **Install dependecies**
   pip install -r requirements.txt

4. **Run the bot**
python readwritebot.py

Notes :
Choose the run duration when prompted
Click the target input field, then press Enter in the terminal to start

Here is how to use the tool with a demo video.  
There is also a written version down below the video.

## Demo Video

### Region Finder Demo (With Loop)
Use this when the text continuously changes (for example, MonkeyType).  
⚠️ **Important:** It is against the Terms of Service of MonkeyType to use bots or automation. This demo is for **educational purposes only**.  

[<video src="RegionFinder_Demo.mov" controls></video>](https://github.com/user-attachments/assets/61cb3fc3-c64f-4ae1-9dc6-d9bf10f01d09)

### Monkey Type Demo (Educational Purposes Only)
Example of looping input.  
⚠️ **Again, do not use this to automate MonkeyType in practice.**  

[<video src="MonkeyType_Demo.mov" controls></video>](https://github.com/user-attachments/assets/bae0adea-09de-4ac6-abdd-ed3a65177076)

### Region Finder Demo (Without Loop)
Use this when the text is static or read once through (like a Wikipedia page).  
- By default, this is for one pass (no loop). (so the second region is not required to be filled/updated in the code) 
- A loop **can** be used, but you would need to adjust your screen manually to keep the content aligned.  

### Writing Demo
Demonstrates another use case of the tool for writing.  

[<video src="Region.Word.mov" controls></video>](https://github.com/user-attachments/assets/eb3439fc-646f-4310-a525-862e04ccbf75)

### Demo Video (YouTube)
For a hosted YouTube demo:

[![Watch the demo](https://img.youtube.com/vi/TZuHUH2W9KQ/0.jpg)](https://youtu.be/TZuHUH2W9KQ)

---

📖 **Note:** Each of these demos has a written explanation provided below to make the usage clearer.

## Choosing and Setting the Screen Region

The bot needs to know where on your screen the words appear.  
Use the included **region finder** helper script to capture the correct rectangle.

### 1. Run the Region Finder
```bash
python region_finder.py
```
### **2. Follow the on-screen prompts:**
Move your mouse to the top left of the words area, wait for it to record the position

Move your mouse to the bottom right of the words area, wait for it to record the position

It will print a tuple (left, top, width, height)

Put these values into the globals at the top of readwritebot.py:
```bash
first_region  = (LEFT, TOP, WIDTH, HEIGHT)      # first pass, all 3 lines
looping_region = (LEFT, TOP_OFFSET, WIDTH, HEIGHT_2LINES)  # subsequent passes, bottom 2 lines
```

Notes :
The `looping_region` is mainly useful when the text on the screen is continuously changing, such as in Monkeytype where new words appear as you type.  
If you are re-transcribing static text — for example, from a Word document or any other source that does not change — you can ignore this setting.

### ** Configure Typing Speed**
Speed is controlled by the interval argument in pyautogui.write:
```bash
pyautogui.write(text, interval=0.07)
```
Smaller interval → faster typing

Larger interval → slower typing

0.007 ≈ 300-400 WPM (depends on the number of screenshot required, so depends on the region size)

### **Typical Code Locations to Edit**
**Regions**

At the top of readwritebot.py:
```bash
first_region   = (x, y, w, h)
looping_region = (x, y, w, h)
```
**Speed**

In type_text:
```bash
pyautogui.write(text, interval=...)
```
**One extra space per loop (optional)**

Near the end of the main loop :

```bash
pyautogui.press('space')
```
