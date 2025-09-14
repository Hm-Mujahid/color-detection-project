# 🎨 AI Box Color Detection

This project detects the **color of a box in an image** using **OpenCV + NumPy**.  
It finds the **average color** of a region (box) in an image and matches it to the nearest color name.  

---

## 📌 Features
- 🖼 Detects box color from an image  
- 🎯 Matches color to nearest known name (Red, Green, Blue, Yellow, etc.)  
- ⚡ Simple & lightweight (only OpenCV + NumPy)  
- 🛠 Easy to run and extend  

---

## 📂 Project Structure

color-detection-project/
│-- box_color_detector.py # Main Python script
│-- requirements.txt # Python dependencies
│-- .gitignore # Ignore unnecessary files
│-- README.md # Project documentation
└── box.png # Example input image



---

## 🚀 Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Hm-Mujahid/color-detection-project.git
cd color-detection-project

2️⃣ Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the script
python box_color_detector.py box.png

🖼 Example Output

Output:

Detected Box Color: Red
Average BGR value: (48, 60, 236)

📌 Requirements

Python 3.x

OpenCV

NumPy

Install with:

pip install -r requirements.txt

📜 License

This project is licensed under the MIT License.
Feel free to use, modify, and share!

🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss.

⭐ Acknowledgements

Built with ❤️ using Python, OpenCV, and NumPy


---

