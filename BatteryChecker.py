#!/usr/bin/env python
import commands
import pynotify
from threading import Timer
def battery_check():
  batteryInfo = commands.getoutput("acpi")
  colon = batteryInfo.index(':')
  firstComma = batteryInfo.index(',')
  state = batteryInfo[colon+2:firstComma]
  percentageSymbol = batteryInfo.index('%')
  percentage = float(batteryInfo[firstComma+1:percentageSymbol])
  if state.lower() == "discharging" and percentage < 10:
    pynotify.init ("Battery Information")
    Hello = pynotify.Notification ("Battery is critically low!","The battery is now: "+str(percentage)+"%")
    Hello.show ()
  timer = Timer(120.0,battery_check)
  timer.start()
if __name__ == "__main__": battery_check()