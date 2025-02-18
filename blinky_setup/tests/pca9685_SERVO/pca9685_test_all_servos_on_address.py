import board
import busio
import adafruit_pca9685
import time
from adafruit_servokit import ServoKit
# i2c = busio.I2C(board.SCL, board.SDA)
# hat = adafruit_pca9685.PCA9685(i2c)
min = 90
max = 90
pin_range = [0, 1]
while True:


    for gate in range(pin_range[0], pin_range[1]):
        kit.servo[gate].angle = min 
    time.sleep(.5)
    for gate in range(pin_range[0], pin_range[1]):
        kit.servo[gate].angle = max
    time.sleep(.5)
