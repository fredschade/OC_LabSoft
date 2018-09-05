#to send a file of gcode to the printer
# import sys
# 
# sys

# print(pwd)

import atexit
import os
import sys
sys.path.append(os.getcwd())
# sys.path.append("/usr/local/lib/python3.5")
import time

from printrun.printcore import printcore
from printrun import gcoder



def send_gcode(file, printer):
  # time.sleep(1)
  gcode=[i.strip() for i in open(file)] # or pass in your own array of gcode lines instead of reading from a file
  gcode = gcoder.LightGCode(gcode)
  printer.startprint(gcode)
  while (printer.printing):
      time.sleep(0.1)







atexit.register(close_connections)
