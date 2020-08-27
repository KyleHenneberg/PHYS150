#Kyles SOS
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
  # note the new line: "a" is a variable that takes the values that are
  # listed in square brackets.  This loop is sometimes called a "foreach"
  for a in [1,1,1,2,2,2,1,1,1]:
        print("SOS")
        led.value = True
        time.sleep(a/2)
        led.value = False
        time.sleep(a/2)
