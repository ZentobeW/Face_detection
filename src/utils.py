import os
import time
from collections import deque
import cv2

class EmotionSmoother:
    def __init__(self, maxlen=10):
        self.emotion_history = deque(maxlen=maxlen)

    def smooth(self, emotion):
        self.emotion_history.append(emotion)
        if len(self.emotion_history) < 3:
            return emotion
        return max(set(self.emotion_history), key=self.emotion_history.count)


def save_screenshot(frame):
    os.makedirs("screenshots", exist_ok=True)
    filename = f"screenshots/emotion_{int(time.time())}.jpg"
    cv2.imwrite(filename, frame)
    print(f"Screenshot disimpan: {filename}")
