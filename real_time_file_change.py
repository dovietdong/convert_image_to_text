import os
import asyncio
import cv2
import pyperclip
from PIL import Image
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\DoVietDong\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

class ImageFileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            print("Image file changed:", event.src_path)
            if os.path.exists(event.src_path):
                try:
                    image = Image.open('./image/capture.png')
                    text = pytesseract.image_to_string(image, lang='vie')
                    print(text)
                    pyperclip.copy(text)
                    print('copy success')
                    os.remove(event.src_path)
                except Exception as e:
                    # Xử lí ngoại lệ
                    print("Caught exception: ", e)
                

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = ImageFileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
