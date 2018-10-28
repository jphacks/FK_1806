#!/usr/bin/python 

import pigpio
import time
import sys
import cgi
import os

UNDER_SERVO_PIN = 4
TOP_SERVO_PIN = 23
MIN_PULSE_WIDTH = 500
MAX_PULSE_WIDTH = 2400
MIDDLE_PULSE_WIDTH = (MIN_PULSE_WIDTH + MAX_PULSE_WIDTH) / 2

def fileRead(filename):
    file = open(filename, 'r')
    string = file.read()
    return string

def fileWrite(filename, text):
    file = open(filename, 'w')
    file.write(text)

def initServo():
    current = fileRead('current.txt')
    if current != "500":
        return
    elif current == "500":
        pi = pigpio.pi()
        pi.set_servo_pulsewidth(UNDER_SERVO_PIN, MIDDLE_PULSE_WIDTH)
        fileWrite('current.txt', str(MIDDLE_PULSE_WIDTH))
        time.sleep(1)

pi = pigpio.pi()
initServo()

form = cgi.FieldStorage()

if form["key"].value == "1":
    pi.set_servo_pulsewidth(UNDER_SERVO_PIN, MIN_PULSE_WIDTH)
    time.sleep(1)
    pi.set_servo_pulsewidth(TOP_SERVO_PIN, MIDDLE_PULSE_WIDTH - 500)
    fileWrite('current.txt', str(MIN_PULSE_WIDTH))
    os.system('sudo ./send.sh. send')
elif form["key"].value == "2":
    pi.set_servo_pulsewidth(UNDER_SERVO_PIN, MIDDLE_PULSE_WIDTH)
    time.sleep(1)
    pi.set_servo_pulsewidth(TOP_SERVO_PIN, MIDDLE_PULSE_WIDTH)
    fileWrite('current.txt', str(MIDDLE_PULSE_WIDTH))
    os.system('sudo ./send.sh. send')
elif form["key"].value == "3":
    pi.set_servo_pulsewidth(UNDER_SERVO_PIN, MAX_PULSE_WIDTH)
    time.sleep(1)
    pi.set_servo_pulsewidth(TOP_SERVO_PIN, MIDDLE_PULSE_WIDTH + 500)
    fileWrite('current.txt', str(MAX_PULSE_WIDTH))
    os.system('sudo ./send.sh. send')
