# Bobbin Counter System Using YOLOv11

This project is a real-time system for counting yarn bobbins in a video stream using the YOLOv11 model. The solution integrates Python, OpenCV, and the Ultralytics YOLO library to detect and track objects with high accuracy.

---

## Features

- **Object Detection:** Utilizes YOLOv11 for accurate bobbin detection in video frames.
- **Object Tracking:** Tracks unique bobbins and avoids duplicate counts.
- **Interactive Visualization:** Displays detection results with bounding boxes, IDs, and counts.
- **Real-Time Processing:** Efficient video processing with OpenCV.
- **Video Output:** Saves the processed video with annotations.

---

## Video Demonstration

Watch the project demonstration below:

[![Bobbin Counter System Demonstration](https://img.youtube.com/vi/1GKLDwXSotw/0.jpg)](https://youtube.com/shorts/1GKLDwXSotw?si=hpT_g8YflVLOkp_u "Bobbin Counter System Demonstration")

### Play the video here:

<iframe width="560" height="315" src="https://www.youtube.com/embed/1GKLDwXSotw" frameborder="0" allowfullscreen></iframe>

---

## How It Works

1. **Setup:**

   - Load the trained YOLOv11 model.
   - Open a video file as the input source.

2. **Processing Each Frame:**

   - Detect bobbins using YOLOv11.
   - Track and identify unique bobbins based on object IDs.
   - Display real-time visualizations with:
     - Bounding boxes for detected objects.
     - A counter showing the total number of unique bobbins.

3. **Save Results:**

   - Annotated video frames are saved as a new video file.

---
