import time as time
from picamera import PiCamera
import numpy as np

def set_cam_param(camera):
    camera.iso = 100
    #wait for gain
    time.sleep(2)
    #fix values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
 
if __name__ == "__main__":
    cam_res_x, cam_res_y = 1024,768
    camera = PiCamera(resolution = (cam_res_x,cam_res_y), framerate = 30)
    #Set ISO
    set_cam_param(camera)
    #take pics
    output = np.empty((cam_res_x * cam_res_y*  3,), dtype = np.uint8)
    output1 = np.empty((cam_res_x * cam_res_y*  3,), dtype = np.uint8)
    output2 = np.empty((cam_res_x * cam_res_y*  3,), dtype = np.uint8)
    output3 = np.empty((cam_res_x * cam_res_y*  3,), dtype = np.uint8)
    output4 = np.empty((cam_res_x * cam_res_y*  3,), dtype = np.uint8)
    start_time = time.time()
    camera.capture_sequence([
        output1,
        output2,
        output3,
        output4,
        output
        ],use_video_port = True)
    output = output.reshape(cam_res_x,cam_res_y,3)
    print(output1)
    print(output1.shape)
    mean = np.mean(np.mean(output1, axis=0),axis = 0)
    print(mean)
    print('total time: %s' %(time.time() - start_time))
    
##    for i in range(10):
##        output = np.empty((1280 * 720 * 3,), dtype = np.uint8)
##        camera.capture(output, 'rgb')
##        output = output.reshape(1280,720,3)
##        mean = np.mean(np.mean(output, axis=0),axis = 0)
##        print('total time: %s' %(time.time() - start_time)) 
    ##    output = output[:100,:100,:]
        #print(output.shape)
##        print(output)
        #print(np.mean(np.mean(output, axis=0),axis = 0))
    
        

