import cv2
import time
from deepface import DeepFace
from .utils import EmotionSmoother, save_screenshot

class EmotionDetector:
    def __init__(self):
        self.smoother = EmotionSmoother(maxlen=10)

    def run(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Tidak bisa membuka webcam")
            return

        print("=== DEEPFACE EMOTION DETECTION ===")
        print("Tekan 'q' untuk keluar | Tekan 's' untuk screenshot")

        fps_start = time.time()
        frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)

            try:
                result = DeepFace.analyze(frame, actions=["emotion"], enforce_detection=False)
                dominant = result[0]["dominant_emotion"]
                emotions = result[0]["emotion"]

                smoothed = self.smoother.smooth(dominant)

                if "region" in result[0]:
                    region = result[0]["region"]
                    x, y, w, h = region["x"], region["y"], region["w"], region["h"]
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
                    cv2.putText(frame, f"{smoothed}", (x, y-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2)

                sorted_emo = sorted(emotions.items(), key=lambda x: x[1], reverse=True)[:3]
                for i, (emo, score) in enumerate(sorted_emo):
                    cv2.putText(frame, f"{emo}: {score:.1f}%",
                                (20, 60+i*25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

            except Exception:
                cv2.putText(frame, "No face detected", (20,30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)

            frame_count += 1
            if frame_count % 30 == 0:
                fps_end = time.time()
                fps = 30 / (fps_end - fps_start)
                fps_start = fps_end
                cv2.putText(frame, f"FPS: {fps:.1f}", (20,30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255),2)

            cv2.imshow("Emotion Detection", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
            elif key == ord("s"):
                save_screenshot(frame)

        cap.release()
        cv2.destroyAllWindows()
