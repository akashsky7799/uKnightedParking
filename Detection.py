#!/usr/bin/python
# -----------------------
# Import required Python libraries
# -----------------------------------
import RPi.GPIO as GPIO  # import GPIO libararies, Code will not run without actual GPIO
import time
import os
import smtplib
import socket
sensor1 = 14 #GPIO pin for output
sensor2 = 15 #GPIO pin for input
import MySQLdb

def SendSignal(garage, num):
    db = MySQLdb.connect(host='209.131.253.72',    # your host, usually localhost
                     user='testUser',         # your username
                     passwd='12345',  # your password
                     db='uknightparkingdb')        # name of the data base

    cur = db.cursor()
    cur.execute("Update Parking set openspots = openspots +" + str(num) + " where name = '"+garage+"';")
    db.commit()
    db.close()

GPIO.setmode(GPIO.BCM)  #initalize all GPIO
GPIO.setup(sensor1, GPIO.IN, GPIO.PUD_DOWN) # initialize GPIO Pin for input

GPIO.setup(sensor2, GPIO.IN, GPIO.PUD_DOWN)   # initialize GPIO pin for output



while True: 
    if GPIO.input(sensor1):                 #if detects digital high from arduino pin 10
        print("Car is leaving 1 pin %d" % (GPIO.input(sensor1)))  #print status of car going out
        SendSignal('A', 1)  # increment number of spots

    if GPIO.input(sensor2):     #if detects digital high from arduino pin 11
        print("Car is entering %d is" % (GPIO.input(sensor2))) # print status of car coming in. 
        SendSignal('A', -1) # decrement number of spots
    
