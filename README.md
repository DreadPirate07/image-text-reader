# OCR Text Extraction Script

The script extracts text from images using Tesseract OCR and saves it to a text file.
This has been written in Python and uses the `pytesseract` and `Pillow` libraries.

I created this to extract texts from my Reddit screenshots :P

## Requirements

1. **Tesseract OCR**:
    - Install Tesseract OCR and its language data files.
2. **Python Libraries**:
    - `pytesseract`: A Python wrapper for Tesseract OCR.
    - `Pillow`: Python Imaging Library which will be used for opening and manipulating images.

## Installation

### Step 1: Install Tesseract OCR

#### On Arch Linux:
```bash
sudo pacman -S tesseract tesseract-data-eng
```
#### On Ubuntu/Debian
```bash
sudo apt-get install tesseract-ocr
```
#### On macOS (Using homebrew)
```bash
brew install tesseract
```

### Step 2: Install Python Libraries Using pip

```bash
pip install pytesseract pillow
```

## Usage

#### Step 1: create an image directory

```bash
mkdir image
```

#### Step 2 : Copy the images to be scanned inside image directory

#### Step 3 : Run script.py
``` bash
python3 script.py
```