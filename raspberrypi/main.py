import pigpio
import time

pi = pigpio.pi()

pi.set_servo_pulsewidth(4, 500)
pi.set_servo_pulsewidth(18, 600)
time.sleep(1)
pi.set_servo_pulsewidth(4, 500)
pi.set_servo_pulsewidth(18, 1450)
time.sleep(1)
pi.set_servo_pulsewidth(4, 500)
pi.set_servo_pulsewidth(18, 2350)


