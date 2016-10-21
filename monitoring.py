#!/usr/bin/env python
# -*- coding: latin-1 -*-

'''
visu en fonction de la charge server

'''



import pyfirmata
import json
import urllib2
import time


#port = 'COM3'            #windows
port = '/dev/cu.wchusbserial401310'   #linux


board = pyfirmata.Arduino(port)

var url = "http://ex.com/monitoring.php"
while True:
    tab = urllib2.urlopen(url).read()
    data = json.loads(tab)
    print data["percent"]
    if data["percent"] < 50.00 :
        board.digital[int(3)].write(int(1))
        board.digital[int(4)].write(int(0))
        board.digital[int(5)].write(int(0))
    elif data["percent"] < 75.00:
        board.digital[int(3)].write(int(0))
        board.digital[int(4)].write(int(0))
        board.digital[int(5)].write(int(1))
    else:
        board.digital[int(3)].write(int(0))
        board.digital[int(4)].write(int(1))
        board.digital[int(5)].write(int(0))
    time.sleep(1)
