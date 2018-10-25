import numpy as np
import picamera
import picamera.array
import time
import requests

class DetectMotion(picamera.array.PiMotionAnalysis):
    def analyse(self,a):
        b = np.sqrt(
            np.square(a['x'].astype(np.float)) +
            np.square(a['y'].astype(np.float))
            ).clip(0,255).astype(np.uint8)
        count = (b>60).sum()
        if count >400:
            print('motion detected')
            camera.capture('./images/motion.jpg')

def send_pic():
    url = "http://2db4d924.ngrok.io/sendImage"
    files = {'file': open('./images/motion.jpg','rb'),
             'Content-Type':'image/jpeg'}
    r = requests.post(url,files = files)
    print(r.status_code == requests.codes.ok)
    
if __name__ == "__main__":
    with picamera.PiCamera() as camera:
        #set_cam_param(camera)
        with DetectMotion(camera) as output:
            camera.resolution = (640,480)
            camera.start_recording('./images/motion.h264',format ='h264',motion_output = output)
            camera.wait_recording(10)
            camera.stop_recording()
    send_pic()
