# rpi-sprinkler-controller-server
## Description
This application allows for control of the Waveshare 8 channel Raspberry Pi controlled relay board.  The board allows you to directly plug a Raspberry Pi with the 40 pin configuration directly into the board and control 8 separate relays.

The `main.py` when executed locally on a Raspberry Pi will initialize a python-bottle server that allows for RESTful access to mapped GPIO pins, and correspondingly, their connected relays.  The simple [rpi-sprinkler-controller-server-test](https://github.com/Douglas-J-Johnson/rpi-sprinkler-controller-server-test) will allow you to test the server via a simple client web application.

The code is adapted from the sample code provided by the manufacturer of the Waveshare 8 relay Raspberry Pi Board.  The general product page and documentation are listed below for reference.  The documentation details additional any additional steps (e.g., additional package downloads) required for the application to run.

[Product Page](https://www.waveshare.com/rpi-relay-board-b.htm)\
[Documentation](https://www.waveshare.com/wiki/RPi_Relay_Board_(B))