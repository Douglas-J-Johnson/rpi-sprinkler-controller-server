from bottle import *
import RPi.GPIO as GPIO
import socket
import json

# Specify GPIO pins using BCM numbering and their initial states
# --------------------------------------------------------------------------------------------------
relay_pins = {'CH1': 5, 'CH2': 6, 'CH3': 13, 'CH4': 16, 'CH5': 19, 'CH6': 20, 'CH7': 21, 'CH8': 26}
relay_states = {'CH1': 1, 'CH2': 1, 'CH3': 1, 'CH4': 1, 'CH5': 1, 'CH6': 1, 'CH7': 1, 'CH8': 1}

# Set up Raspberry Pi Pins
# --------------------------------------------------------------------------------------------------
# Set mode to use BCM (Broadcom) pin numbering
GPIO.setmode(GPIO.BCM)
# Suppress warning
# RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
# for BCM PIN 5
GPIO.setwarnings(False)

# For each GPIO pin set up the pin as an output pin and set pin to initial state
for channel in relay_pins.keys():
  GPIO.setup(relay_pins[channel], GPIO.OUT)
  GPIO.output(relay_pins[channel], relay_states[channel])

# Set up routes and functions
# --------------------------------------------------------------------------------------------------
# Get status of all relays
def validate_relay_states():
  global relay_pins, relay_states

  pin = 0
  actual_relay_state = 0
  expected_relay_state = 0

  for channel in relay_pins.keys():
    pin = relay_pins[channel]
    actual_relay_state = GPIO.input(pin)
    expected_relay_state = relay_states[channel]

    if (actual_relay_state != expected_relay_state):
      print(f'Relay state mimatch for relay channel {channel}, BCM pin {relay_pins}')
      print(f'Actual state is {actual_relay_state}, expected {expected_relay_state}')
      print('Using actual state value')

    relay_states[channel] = actual_relay_state

@get("/relays")
def get_relays():
  global relay_states

  validate_relay_states()

  response.headers['Content-Type'] = 'application/json'
  print(json.dumps(relay_states))
  return json.dumps(relay_states)

# Set status of all relays
@post('/relays')
def set_relays():
  global relay_states

  for channel in relay_states.keys():
    relay_states[channel] = int(request.POST.get(channel))
    GPIO.output(relay_pins[channel], relay_states[channel])

  validate_relay_states()

  response.headers['Content-Type'] = 'application/json'
  print(json.dumps(relay_states))
  return json.dumps(relay_states)

# Set up server
# --------------------------------------------------------------------------------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
localhost = s.getsockname()[0]

run(host=localhost, port="8000")
