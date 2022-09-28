# An experiment with DroneKit

## Instructions

### Environment variables

You will need the Mission Planner IP address and port number.
You will also need the SITL port number.
I have also made the latitude and longitude into environment variables.

Ex:
MP_IP=127.0.0.1
MP_PORT=14551
SITL_PORT=5760
LAT=37.5407
LON=-122.361


### Initialization

To initialize the project, run:
1. `make init`.


### Starting it

In three separate terminals, run the following commands:
1. `make run-sitl`.
2. `make proxy`.
3. `make run`.

