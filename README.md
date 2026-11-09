# Green Screen Photo Editor (`photoshop.py`)

A simple Python program built for **stanCode** coursework that performs green screen background replacement (chroma keying) using the custom `SimpleImage` library and Pillow.

---

## 🌟 Features

- **Chroma Key Background Replacement:** Replaces a green screen background in a portrait (`Emma.jpeg`) with a custom background image (`Shrek.jpg`).
- **Smart Filtering Logic:**
  - **Thresholding:** Detects green pixels based on a calculated color average and threshold multiplier (`THRESHOLD = 1.25`).
  - **Dark Pixel Protection:** Prevents black pixels from being incorrectly replaced (`BLACK = 115`).
  - **Region Masking:** Protects specific areas of the foreground subject (e.g., specific shirt coordinates) from being altered.

---

## 📂 Project Structure

Ensure your project directory is organized as follows before running the script:

```text
├── photoshop.py         # Main script containing the green screen logic
├── simpleimage.py       # stanCode SimpleImage wrapper library
└── images/
    ├── Emma.jpeg        # Foreground portrait with a green screen
    └── Shrek.jpg        # Background image
```

---

## ⚙️ Prerequisites & Dependencies

To run this program, you need:
- **Python 3.x** installed on your system.
- The **Pillow** library (required by `simpleimage.py`). You can install it via pip if you haven't already:
  ```bash
  pip install Pillow
  ```

---

## 🚀 How to Run

1. Open your terminal or command prompt.
2. Navigate to the directory containing your project files.
3. Execute the script using Python:
   ```bash
   python photoshop.py
   ```
4. The modified image will pop up in an external viewer window once processing is complete.

---

## 🛠️ Code Customization

You can tweak the constants at the top of `photoshop.py` to fine-tune the green screen effect:
- `THRESHOLD`: Adjusts how sensitive the program is to green tones.
- `BLACK`: Controls the minimum brightness threshold to protect dark/black pixels.