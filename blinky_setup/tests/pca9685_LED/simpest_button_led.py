from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio
import time

# Initialize I2C bus
i2c = busio.I2C(SCL, SDA)

# Initialize PCA9685
pca = PCA9685(i2c, address=0x42)
pca.frequency = 1000  # Set PWM frequency to 1kHz for smoother LED operation

# LED channel (0-15)
LED_CHANNEL = 0

def set_brightness_percentage(channel: int, percentage: float) -> None:
    """
    Set LED brightness as a percentage (0-100)
    """
    # PCA9685 has 16-bit resolution (0-65535)
    duty_cycle = int((percentage / 100.0) * 65535)
    pca.channels[channel].duty_cycle = duty_cycle

try:
    while True:
        # Fade up
        for brightness in range(101):  # 0 to 100
            set_brightness_percentage(LED_CHANNEL, brightness)
            if brightness == 0:
                print("LED at minimum brightness (0%)")
            elif brightness == 100:
                print("LED at maximum brightness (100%)")
            time.sleep(0.005)  # 0.5 seconds up (0.005 * 100 steps)
            
        # Fade down
        for brightness in range(100, -1, -1):  # 100 to 0
            set_brightness_percentage(LED_CHANNEL, brightness)
            if brightness == 0:
                print("LED at minimum brightness (0%)")
            elif brightness == 100:
                print("LED at maximum brightness (100%)")
            time.sleep(0.005)  # 0.5 seconds down (0.005 * 100 steps)

except KeyboardInterrupt:
    # Clean up
    pca.deinit()
