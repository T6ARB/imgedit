# 🖼️ imgedit - Simple Image Editor CLI

A **simple** command-line image editor written in Python, perfect for quick image edits directly from your terminal (Termux compatible).

---

## 🚀 Features

- 🖼️ Resize images  
- 🔄 Rotate images  
- 📝 Add text overlay  
- ⚫ Convert images to black & white (grayscale)  

---

## ⚙️ Installation

```bash
git clone https://github.com/QK-KV/imgedit.git
cd imgedit
pip install -r requirements.txt
```

---

## 💡 Usage Examples

### Resize image

```bash
python imgedit.py resize -i input.jpg -o output.jpg --width 800 --height 600
```

### Rotate image

```bash
python imgedit.py rotate -i input.jpg -o output.jpg --angle 90
```

### Add text to image

```bash
python imgedit.py add_text -i input.jpg -o output.jpg -t "Hello World" --x 50 --y 100
```

### Convert to black & white

```bash
python imgedit.py bw -i input.jpg -o output.jpg
```

---

## 📂 Fonts

The project includes a sample font (`Arial.ttf`) inside the `fonts/` folder, used for adding text on images.  
You can replace it with any `.ttf` font you prefer.

---

## 📝 Notes

- Make sure the input image path is correct.  
- Output will overwrite if the file already exists.  
- Works on Termux and any system with Python and dependencies installed.
