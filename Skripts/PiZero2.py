# python script for the Raspberry Pi camera V2 Sony IMX219 NoIR

import socket, threading, os
import time
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5)

host, port = '172.19.181.2', 442
file_name = '/home/pi/testimage.jpg'

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
            camera.resolution = (2592, 1944)
            camera.awb_mode = 'off'
            camera.awb_gains = (0.5, 2.0)
            camera.rotation = 180
            #os.system("raspistill -bm -o testimage.jpg -w 3280 -h 2464")
            camera.capture(file_name)
            size = os.path.getsize(file_name)
            print(' file size : {}'.format(str(size)))
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
