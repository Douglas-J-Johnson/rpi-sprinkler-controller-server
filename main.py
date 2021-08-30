from bottle import *
import RPi.GPIO as GPIO
import socket

# Specify GPIO pins using BCM numbering and their initial states
relay_pins = {'CH1': 5, 'CH2': 6, 'CH3': 13, 'CH4': 16, 'CH5': 19, 'CH6': 20, 'CH7': 21, 'CH8': 26}
relay_states = {'CH1': 1, 'CH2': 1, 'CH3': 1, 'CH4': 1, 'CH5': 1, 'CH6': 1, 'CH7': 1, 'CH8': 1}

# Set mode to use BCM (Broadcom) pin numbering
GPIO.setmode(GPIO.BCM)

# For each GPIO pin set up the pin as an output pin and set pin to initial state
for channel in relay_pins.keys():
  GPIO.setup(relay_pins[channel], GPIO.OUT)
  GPIO.output(relay_pins[channel], relay_states[channel])

# Set up routes and functions
# Get status of all relays
@get("/relays")
def get_relays():
   global relay_states

# Set status of all relays
@post('/relays')
def set_relays():
  global relay_states

  for channel in relay_states.keys():
    relay_states[channel] = int(request.POST.get(channel))
    GPIO.output(relay_pins[channel], relay_states[channel])

# Set up server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
localhost = s.getsockname()[0]

run(host=localhost, port="8000")
