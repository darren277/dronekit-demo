include .env

init:
	pip install -r requirements.txt
	pip install dronekit-sitl -UI
	pip install mavproxy
	pip install -U wxPython
	pip install matplotlib

start-sitl:
	dronekit-sitl copter --home=$(LAT),$(LON),0,180

mavproxy:
	mavproxy.py --master tcp:127.0.0.1:$(SITL_PORT) --sitl 127.0.0.1:5501 --out 127.0.0.1:14550 --out $(MP_IP):$(MP_PORT) --moddebug 3

run:
	python app.py --connect udp:$(MP_IP):$(MP_PORT)
