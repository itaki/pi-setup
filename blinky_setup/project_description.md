# Blinky the Shop Bot

## Objective:
 
Make a node-red flow that runs on a raspberry pi and various pieces of hardware to control a shop, specifically, dust collection. To determine what tools are on and off it uses a collection of buttons and current sensors. Then it uses PWM and GPIO expansion boards with servos and relays to turn on dust collectors, lights, fans, and open and close gates.

## Software Considerations
- Node-RED 
- Javascript 
- Python
- I2C

## Hardward Considerations 
- Raspberry Pi 4 with 4GB ram
- MCP23017 GPIO expanders for buttons, relays, and LEDS
- ADS1x15 AD converters for ACS712 current sensors
- PCA9685 PWM driver for servos, LEDs, and RGBLEDs 

## Extra nodes in Node-RED
- @joe-ab1do/mcp-pcf-aio 
- node-red-contrib-ads1x15_i2c
- node-red-contrib-pca9685
- node-red-node-pi-gpio
- node-red-dashboard