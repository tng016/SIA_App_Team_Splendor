import time
import picamera
import numpy as np

with picamera.PiCamera() as camera:
    camera.resolution = (1024,768)
    camera.framerate = 30
    camera.start_preview()
    time.sleep(2)
    output = np.empty((1024 * 768 * 3,), dtype = np.uint8)
    camera.capture_sequence([
        'image1.jpg',
        'image2.jpg',
        'image3.jpg',
        'image4.jpg',
        output
        ])
    output = output.reshape(1024,768,3)
    mean = np.mean(np.mean(output, axis=0),axis = 0)
    print(mean)