# Object Detection with YOLOv8

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Ultralytics YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange.svg)](https://github.com/ultralytics/ultralytics)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A professional **object detection pipeline** using **YOLOv8** for videos and webcams.  
Automatically detects people, vehicles, and everyday objects, and exports annotated videos.

---

## 📁 Project Structure

```
Object_Detection_Yolo/
│
├── .venv/                      # Python virtual environment
│
├── videos/                     # Input & output videos
│   ├── cars.mp4
│   ├── mart.mp4
│   ├── people.mp4
│   ├── queue.mp4
│   └── queue_stamped.mp4       # Example YOLO output
│
├── Yolo_Weights/               # Model weights (YOLOv8n.pt)
│
└── Yolo with WebCam/
    ├── Yolo_Video.py           # Detect objects in one video
    ├── run_yolo_videos.py      # Batch process all videos
    └── Yolo_WebCam.py          # Live webcam detection
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/Object_Detection_Yolo.git
cd Object_Detection_Yolo
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv .venv
.\.venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, you can install manually:

```bash
pip install ultralytics opencv-python numpy torch torchvision
```

> 💡 **GPU users:**  
> If your NVIDIA GPU supports CUDA 12.1+, install:
> ```bash
> pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
> ```

---

## 🎯 How to Use

### ▶️ Run YOLOv8 on One Video
Automatically loads `../videos/queue.mp4` and saves annotated output.

```bash
python "Yolo with WebCam/Yolo_Video.py"
```

Output:
```
../videos/queue_stamped.mp4
```

---

### ⚙️ Batch Process All Videos
Process all `.mp4` files in the `videos/` folder:

```bash
python "Yolo with WebCam/run_yolo_videos.py" --all
```

To create a ZIP of all outputs:
```bash
python "Yolo with WebCam/run_yolo_videos.py" --all --zip
```

Serve files locally for easy download:
```bash
python "Yolo with WebCam/run_yolo_videos.py" --all --zip --serve
```
Then visit [http://localhost:8000](http://localhost:8000) in your browser.

---

### 📸 Run Live Object Detection from Webcam

```bash
python "Yolo with WebCam/Yolo_WebCam.py"
```

---

## ⚡ Performance Tips

| Mode | Description | Speed |
|------|--------------|--------|
| YOLOv8n | Small, fast (default) | ✅ Recommended |
| YOLOv8s/m/l/x | Larger models | ⚠️ Slower |
| ONNXRuntime | CPU-optimized | 🚀 2× faster |
| CUDA (GPU) | NVIDIA only | ⚡ Real-time FPS |

---

## 📦 Model Weights

Download the pretrained YOLOv8n weights (≈12 MB):

👉 [Download YOLOv8n.pt](https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt)

Place it inside:
```
Object_Detection_Yolo/Yolo_Weights/
```

---

## 🧠 Troubleshooting

- **Runs only on CPU** → GPU unsupported or older (e.g., MX230).  
- **Slow inference** → Use smaller image size:  
  ```python
  model(frame, imgsz=480)
  ```
- **Missing dependencies** →  
  ```bash
  pip install ultralytics opencv-python numpy torch torchvision
  ```
- **Wrong paths in PyCharm** → Run from project root or check `../videos/` references.

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).  
You’re free to modify, use, and distribute it for research or educational purposes.

---

## ❤️ Credits

Built with:
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [OpenCV](https://opencv.org/)
- [PyTorch](https://pytorch.org/)

---

### 👨‍💻 Author
**Asiya Akhtar**  
💼 GitHub: [@Asiya-Akhtar](https://github.com/Asiya-Akhtar)  
📧 Email: asiyaakhtar17@gmail.com
