from picamera2 import Picamera2
import os
from time import sleep

def capture_image():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    image_path = os.path.join(script_dir, "code.png")


    picam2 = Picamera2()
    picam2.start()
    picam2.capture_file(image_path)
    picam2.stop()

    return image_path

if __name__ == "__main__":
    capture_image()