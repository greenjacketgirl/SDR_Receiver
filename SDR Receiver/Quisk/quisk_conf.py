# OpenRadio v1.1 Quisk Configuration File
# 
# IMPORTANT: To be able to control the OpenRadio board from within Quisk,
# you will need to compile and upload the 'openradio_quisk' firmware, which
# is available from: https://github.com/darksidelemm/open_radio_miniconf_2015
#
# You will also need to install the pyserial package for python.
#

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from os import path
import sys
import wx

# SOUND CARD SETTINGS
#
sample_rate = 48000					# name_of_sound_capt hardware sample rate in Hertz
if sys.platform == "win32":
  name_of_sound_capt = "Primary"
  name_of_sound_play = "Primary"
elif sys.platform == "darwin":
  name_of_sound_capt = "pulse"
  name_of_sound_play = "pulse"
else:
  name_of_sound_capt = "pulse"		# Name of soundcard capture hardware device.
  name_of_sound_play = "pulse"
channel_i = 1 					# Soundcard index of in-phase channel:  0, 1, 2, ...
channel_q = 0						# Soundcard index of quadrature channel:  0, 1, 2, ...

# SERIAL PORT SETTINGS
# Set this as appropriate for your OS.
if path.exists("/dev/cu.wchusbserial1410"):
  openradio_serial_port = "/dev/cu.wchusbserial1410"
elif path.exists("/dev/cu.wchusbserial1410"):
  openradio_serial_port = "/dev/cu.wchusbserial1410"
openradio_serial_rate = 57600


# OpenRadio Frequency limits.
# These are just within the limits set in the openradio_quisk firmware.
openradio_lower = 100001
openradio_upper = 29999999

# OpenRadio Hardware Control Class
#
import serial,time
from quisk_hardware_model import Hardware as BaseHardware

class Hardware(BaseHardware):
  def open(self):
    # Called once to open the Hardware
    # Open the serial port.
    self.or_serial = serial.Serial(openradio_serial_port,openradio_serial_rate,timeout=3)
    print("Opened Serial Port.")
    # Wait for the Arduino Nano to restart and boot.
    time.sleep(2)
    # Poll for version. Should probably confirm the response on this.
    version = str(self.get_parameter("VER"))
    print("This should be the version printed next.")
    print(version)
    # Return an informative message for the config screen
    t = version + ". Capture from sound card %s." % self.conf.name_of_sound_capt
    return t

  def close(self):      
    # Called once to close the Hardware
    self.or_serial.close()

  def ChangeFrequency(self, tune, vfo, source='', band='', event=None):
    # Called whenever quisk requests a frequency change.
    # This sends the FREQ command to set the centre frequency of the OpenRadio,
    # and will also move the 'tune' frequency (the section within the RX passband
    # which is to be demodulated) if it falls outside the passband (+/- sample_rate/2).
    print("Setting VFO to %d." % vfo)
    if(vfo<openradio_lower):
      vfo = openradio_lower
      print("Outside range! Setting to %d" % openradio_lower)

    if(vfo>openradio_upper):
      vfo = openradio_upper
      print("Outside range! Setting to %d" % openradio_upper)

    success = self.set_parameter("FREQ",str(vfo))

    print("sample_rate =")
    print(sample_rate)
    # If the tune frequency is outside the RX bandwidth, set it to somewhere within that bandwidth.
    if(tune>(vfo + sample_rate/2) or tune<(vfo - sample_rate/2)):
      vfo = tune -10000  #We don't care so much about the VFO.
      print("Bringing tune frequency back into the RX bandwidth.")

    if success:
      print("Frequency change succeeded!")
    else:
      print("Frequency change failed.")

    return tune, vfo

#
# Serial comms functions, to communicate with the OpenRadio board
#

  def get_parameter(self,string):
    string = string + "\n"
    self.or_serial.write(string.encode())
    return self.get_argument()
    #return string.encode()
        
  def set_parameter(self,string,arg):
    string = string+","+arg+"\n"
    self.or_serial.write(string.encode())
    if self.get_argument() == arg:
      return True
    else:
      return False
    
  def get_argument(self):
    data1 = self.or_serial.readline()
    # Do a couple of quick checks to see if there is useful data here
    if len(data1) == 0:
       return -1
        
    # Maybe we didn't catch an OK line?
    if data1.startswith(b'OK'):
       data1 = self.or_serial.readline()
        
    # Check to see if we have a comma in the string. If not, there is no argument.
    if data1.find(b',') == -1:
       return -1
    
    data1 = data1.split(b',')[1].rstrip(b'\r\n')
    print("data1 =")
    print(data1)
    
    # Check for the OK string
    data2 = self.or_serial.readline()
    if data2.startswith(b'OK'):
       return data1
