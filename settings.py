import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MP_IP = os.environ.get("MP_IP")
MP_PORT = int(os.environ.get("MP_PORT"))

LAT = float(os.environ.get("LAT"))
LON = float(os.environ.get("LON"))


