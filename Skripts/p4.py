# auf dem Raspberry Pi 4: p4.py 

import socket, sys, threading
import time
import os
port = 442

#os.system("sudo rm pi1/*")
#os.system("sudo rm pi2/*")
#os.system("sudo rm pi3/*")

def recv_data(host, filename):
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mysocket.connect((host, port))
        data = mysocket.recv(1024)
        f = open(filename, 'wb')
        while data != bytes(''.encode()):
                #print(data)
                f.write(data)
                data = mysocket.recv(1024)



fileName1 = "pi1/"
fileName2 = "pi2/"
fileName3 = "pi3/"
fileType = ".jpg"
counter = 0

#----------NEW-----------------

i = 0

while True:
	if not os.path.isdir('pi1/' + str(i)):
		fileName1 = 'pi1/' + str(i) + '/'
		fileName2 = 'pi2/' + str(i) + '/'
		fileName3 = 'pi3/' + str(i) + '/'
		os.system("mkdir " + fileName1)
		os.system("mkdir " + fileName2)
		os.system("mkdir " + fileName3)
		break
	i = i + 1

#------------------------------

while True:
        threads = []
        pi1 = fileName1 + str(counter) + fileType
        pi2 = fileName2 + str(counter) + fileType
        pi3 = fileName3 + str(counter) + fileType
        pi1_thread = threading.Thread(target = recv_data, args=("172.19.181.1", pi1, ))
        pi2_thread = threading.Thread(target = recv_data, args=("172.19.181.2", pi2, ))
        pi3_thread = threading.Thread(target = recv_data, args=("172.19.181.3", pi3, ))
        threads.append(pi1_thread)
        threads.append(pi2_thread)
        threads.append(pi3_thread)
        for x in threads:
                x.start()
        for x in threads:
                x.join()
        counter = counter + 1
#       time.sleep(3)



#       while True:
#               if pi1_thread.is_alive() or pi2_thread.is_alive():
#                       time.sleep(1)
#               else:
#                       break
#        time.sleep(2)