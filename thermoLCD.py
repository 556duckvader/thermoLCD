#!/usr/bin/python

# Import all the libraries
import Adafruit_CharLCD as LCD
from w1thermsensor import W1ThermSensor
import time

# Raspberry Pi pin configuration:
lcd_rs        = 27  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 22
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2


# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

#Creates the degree symbol
degree = chr(223)

# Define the temperature sensor
sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20,"0214633fa6ff")

while True:
 	# Display it on the LCD
 	lcd.clear()
 	lcd.message("Probe Temp:\n %.2f %sF" % (sensor.get_temperature(W1ThermSensor.DEGREES_F),degree))
	time.sleep(10)
