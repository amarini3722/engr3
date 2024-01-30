# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_hcsr04
import neopixel

NUMPIXELS = 1  # NumberOfLEDs
SPEED = 0.05  # HowFastItRotatesThroughTHeRainbow
BRIGHTNESS = 1.0  # HowBrightItIs
PIN = board.NEOPIXEL
pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        print((sonar.distance,))
        if sonar.distance < 5:
            for pixel in range(len(pixels)):  # CreatesTheFirstPeramitorForTheFirstColor
                pixels.show()
        if sonar.distance > 5 and sonar.distance < 20:
            for pixel in range(len(pixels)):  # CreatesTheSecondPeramitorForTheSecondColor
                pixels[pixel] = (255-(sonar.distance - 5 / 15 * 255), 0, (sonar.distance - 5 / 15 * 255))
                pixels.show()
             
        if sonar.distance > 20 and sonar.distance < 35:
            for pixel in range(len(pixels)):  # CreatesTheThirdPeramitorForTheThirdColor
                pixels[pixel] = ( 0, (sonar.distance - 5 / 15 * 255), 255-(sonar.distance - 5 / 15 * 255))
                pixels.show()
        if sonar.distance > 35:
            for pixel in range(len(pixels)):  # CreatesTheForthPeramitorForTheFourthColor
                pixels[pixel] = ( 0, 255, 0)
                pixels.show()  
    except RuntimeError:
        print("Retrying!") #IfThereIsAErrorItWillSendAMessageToTheTerminal
    time.sleep(0.1)