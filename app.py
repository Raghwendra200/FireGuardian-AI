import streamlit as st
import cv2
from ultralytics import YOLO
import tempfile
import math
import cvzone
import time

# Set Streamlit page configuration
st.set_page_config(
    page_title="🔥 FireGuardian AI",
    layout="wide"
)

# Inject custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .title {
        font-size: 3rem;
        font-weight: bold;
        color: #d62828;
        text-align: center;
        margin-bottom: 0.3rem;
    }
    .tagline {
        font-size: 1.25rem;
        font-weight: 500;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .footer {
        font-size: 0.9rem;
        text-align: center;
        margin-top: 2rem;
        color: #888;
    }
    </style>
""", unsafe_allow_html=True)

# Project Title and Tagline
st.markdown('<div class="title">🔥 FireGuardian AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="tagline">Real-Time Intelligent Fire Detection using YOLOv8 and OpenCV</div>',
    unsafe_allow_html=True
)

# Load YOLO model
with st.spinner("🚀 Initializing YOLOv8 Fire Detection Model..."):
    model = YOLO("fire.pt")
    classnames = ['fire']

# Input Source
st.subheader("🎥 Select Video Source")
source = st.radio("", ['Webcam', 'Upload Video'], horizontal=True)

cap = None
if source == 'Upload Video':
    video_file = st.file_uploader("📁 Upload a video", type=['mp4', 'avi', 'mov'])
    if video_file:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(video_file.read())
        cap = cv2.VideoCapture(tfile.name)
elif source == 'Webcam':
    cap = cv2.VideoCapture(0)

# Layout for video and controls
video_col, control_col = st.columns([4, 1])
frame_placeholder = video_col.empty()

with control_col:
    st.markdown("### 🧠 How to Use")
    st.markdown("""
        - Choose a video source  
        - Click "Start Detection" to begin  
        - Watch live detection and FPS  
        - Click "Stop Detection" to end  
    """)
    start_button = st.button("▶️ Start Detection", use_container_width=True)
    stop_button = st.button("⏹️ Stop Detection", use_container_width=True)

# Detection logic
prev_time = 0
detection_running = False

if start_button and cap is not None and cap.isOpened():
    detection_running = True

try:
    while detection_running and cap.isOpened():
        success, frame = cap.read()
        if not success:
            st.warning("⚠️ Cannot read video stream.")
            break

        frame = cv2.resize(frame, (720, 540))
        results = model(frame, stream=True)

        for r in results:
            for box in r.boxes:
                conf = float(box.conf[0])
                class_id = int(box.cls[0])

                if conf > 0.5:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    label = f"{classnames[class_id]} {math.ceil(conf * 100)}%"
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    cvzone.putTextRect(frame, label, [x1, y1 - 10], scale=1, thickness=2)

        # FPS calculation
        curr_time = time.time()
        fps = int(1 / (curr_time - prev_time)) if curr_time != prev_time else 0
        prev_time = curr_time
        cv2.putText(frame, f'FPS: {fps}', (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display in Streamlit
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(
            frame,
            channels="RGB",
            use_container_width=True
        )

        if stop_button:
            detection_running = False
            st.success("✅ Detection stopped.")
            break

finally:
    if cap:
        cap.release()

# Footer
st.markdown(
    '<div class="footer">Made with ❤️ using Streamlit, OpenCV, and YOLOv8 | Project: FireGuardian AI</div>',
    unsafe_allow_html=True
)
