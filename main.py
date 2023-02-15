import subprocess
import time
import keyboard
import pyperclip
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\DoVietDong\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def run_file1():
    subprocess.run(["python", "crop_screen.py"])
    # subprocess.run(["python", "real_time_file_change.py"])
    image = Image.open('./image/capture.png')
    text = pytesseract.image_to_string(image, lang='vie')
    print(text)
    pyperclip.copy(text)
    print('copy success')

if __name__ == '__main__':
    keyboard.add_hotkey("ctrl+y", run_file1)

    # Vòng lặp vô hạn để lắng nghe sự kiện gõ phím
    keyboard.wait()

    # TODO xử lí khi gặp exception thì bỏ qua và tiếp tục chạy
    # TODO thêm sự kiện bấm esc thì bỏ qua việc chụp màn hình

    


