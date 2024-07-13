import cv2
import subprocess
import os

# Function to capture image from laptop camera
def capture_image():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    if ret:
        cv2.imwrite('captured_image.jpg', frame)
    camera.release()

# Function to transfer image to phone using adb
def transfer_image_to_phone():
    subprocess.run(['adb', 'push', 'captured_image.jpg', '/phone/Pictures/'])

# Function to save transferred image to phone's gallery
def save_image_to_gallery():
    subprocess.run(['adb', 'shell', 'am', 'broadcast', '-a', 'android.intent.action.MEDIA_SCANNER_SCAN_FILE', '--ez', 'android.intent.extra.SHOW_UI', 'true', '-d', 'file:///sdcard/Pictures/captured_image.jpg'])

# Function to run scrcpy
def run_scrcpy():
    scrcpy_path = "C:\\Users\\SMRITI\\Downloads\\scrcpy-win64-v2.4\\scrcpy.exe"
    try:
        # Run scrcpy using subprocess
        subprocess.run([scrcpy_path])
    except FileNotFoundError:
        print("scrcpy executable not found. Please check the path.")

# Main function
def capture_and_save_image():
    capture_image()
    transfer_image_to_phone()
    save_image_to_gallery()
    os.remove('captured_image.jpg')  # Remove the local image file after transferring
    run_scrcpy()  # Start scrcpy after capturing and saving image

# Run the process
capture_and_save_image()