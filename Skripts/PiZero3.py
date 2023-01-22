#!/usr/bin/python3
##################################
# MLX90640 Demo with Jetson Nano
##################################
#mix of scripts...  https://makersportal.com/blog/2020/6/8/high-resolution-thermal-camera-with-raspberry-pi-and-mlx90640#interpolation & https://habr.com/en/post/441050/
#script for the thermal camera MLX90640

import time,board,busio
import numpy as np
import adafruit_mlx90640
import datetime as dt
import cv2
import socket, threading, os

host, port = '172.19.181.3', 442
file_name = '/home/pi/testimage.jpg'

i2c = busio.I2C(board.SCL, board.SDA, frequency=1200000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_16_HZ # set refresh rate

mlx_shape = (24,32)

print ('---')

frame = np.zeros((24*32,)) # setup array for storing all 768 temperatures

Tmax = 30
Tmin = -5

def td_to_image(f):
    norm = np.uint8((f + 40)*6.4)
    norm.shape = (24,32)
    return norm

time.sleep(4)
t0 = time.time()

class transfer :
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        
        def __init__(self):
            self.mysocket.bind((host, port))
            self.mysocket.listen(5)
            while True:
                print("Server is listening...")
                conn, addr = self.mysocket.accept()
                print("__________________________")
                # waiting for data frame
                mlx.getFrame(frame) # read MLX temperatures into frame var
                img16 = (np.reshape(frame,mlx_shape)) # reshape to 24x32 
                #img16 = (np.fliplr(img16))
                
                ta_img = td_to_image(img16)
                # Image processing
                img = cv2.applyColorMap(ta_img, cv2.COLORMAP_JET)
                img = cv2.resize(img, (2592,1944), interpolation = cv2.INTER_CUBIC)
                img = cv2.flip(img, 1)
                cv2.imwrite(file_name, img)
                print('Saving image ', file_name)
                t0 = time.time()
                try:
                    with open(file_name, 'rb') as file:
                        data = file.read(1024)
                        conn.send(data)
                        while data != bytes(''.encode()):
                            #print(data)
                            data = file.read(1024)
                            conn.send(data)
                        print(' File sent successfully.')
                    conn.close()
                except socket.error:
                    conn.close()
                except IOError:
                    conn.close()

Transfer = transfer()
# just in case
cv2.destroyAllWindows()

