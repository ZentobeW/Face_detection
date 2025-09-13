# Real-Time Emotion Detection

This project provides a real-time emotion detection system using your webcam. It utilizes the `deepface` library to analyze facial expressions and identify emotions, `OpenCV` for video capture and display, and `tensorflow` as the backend. The application draws a bounding box around the detected face, displays the dominant emotion, and provides a list of the top detected emotions with their confidence scores.

## Features

-   **Real-Time Detection**: Analyzes video stream from the webcam in real-time.
-   **Face Bounding Box**: Draws a rectangle around the detected face.
-   **Dominant Emotion Display**: Shows the most prominent emotion detected.
-   **Emotion Smoothing**: Stabilizes the displayed emotion over a series of frames to prevent flickering between emotions.
-   **Top Emotions List**: Displays the top 3 detected emotions and their confidence percentages.
-   **FPS Counter**: Shows the current frames-per-second to monitor performance.
-   **Screenshot Capture**: Save the current frame with all annotations as a JPEG image.

## Requirements

The project requires the following Python libraries:

-   `opencv-python`
-   `deepface`
-   `tensorflow`

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/zentobew/face_detection.git
    cd face_detection
    ```

2.  **Install the dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the emotion detector, execute the `run.py` script from the project's root directory:

```bash
python -m src.run
```

A window will open displaying your webcam feed with the emotion analysis overlay.

### Controls

-   **`q`**: Press 'q' while the video window is active to quit the application.
-   **`s`**: Press 's' to save a screenshot of the current frame. Screenshots are saved in a `screenshots/` directory created in the project root.
