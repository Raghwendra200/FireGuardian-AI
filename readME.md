# FireGuardian AI

**AI-Powered Real-Time Fire Detection System using YOLOv8 and OpenCV**

---

## 🚀 Project Overview

FireGuardian AI is an advanced, real-time fire detection application built with Streamlit, YOLOv8, and OpenCV. It processes live webcam feeds or uploaded video files to identify fire instances and overlay bounding boxes and confidence scores on the video stream, plus a real-time FPS counter.

---

## 🔥 Key Features

* **Real-Time Detection**: Processes video frames in real-time to detect fire hazards.
* **Dual Input Sources**: Supports live webcam feeds and uploaded video files (`.mp4`, `.avi`, `.mov`).
* **Confidence Overlay**: Displays detection confidence percentages.
* **FPS Display**: Monitors and shows processing frame rate for performance insights.
* **Intuitive UI**: Modern, responsive Streamlit interface with clear instructions and control buttons.
* **Custom Styling**: Branded header, tagline, and footer for a professional look.

---

## 📂 Repository Structure

```
FireGuardian/
├── app.py                # Main Streamlit application
├── fire.pt               # Pre-trained YOLOv8 model weights
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── assets/               # (Optional) Icons, logos, CSS files
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/FireGuardian.git
   cd FireGuardian
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure model file**:

   * Place `fire.pt` in the project root (provided in `weights/` or download from \[link]).

---

## ▶️ Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

In the UI:

1. Select **Webcam** or **Upload Video**.
2. Click **Start Detection** to begin.
3. View live fire detection with bounding boxes, confidence scores, and FPS.
4. Click **Stop Detection** to end.

---

## 🛠️ Configuration

* **Video Resize**: Adjust `(width, height)` in `cv2.resize(frame, (720, 540))` to change display ratio.
* **Confidence Threshold**: Modify `if conf > 0.5:` to increase/decrease sensitivity.
* **Custom CSS**: Edit the CSS in `st.markdown(..., unsafe_allow_html=True)` for theme tweaks.

---

## 🌐 Deployment

* **Streamlit Cloud**: Push repo to GitHub and connect in Streamlit Cloud. Ensure `requirements.txt` and `fire.pt` are included.
* **Docker**:

  ```Dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY . /app
  RUN pip install --no-cache-dir -r requirements.txt
  EXPOSE 8501
  ENTRYPOINT ["streamlit", "run", "app.py"]
  ```

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

*Developed by Raghwendra Pratap Singh*
