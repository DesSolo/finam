import os

env_values = [
    'LOGGING_LEVEL',
    'SLEEP_INTERVAL',
    'USER_AGENT',
    'INFLUX_HOST',
    'INFLUX_PORT',
    'INFLUX_USERNAME',
    'INFLUX_PASSWORD',
    'INFLUX_DATABASE',
    'TARGETS',
    'DATE_FROM',
    'DATE_TO'
]

LOGGING_LEVEL = int(
    os.getenv("LOGGING_LEVEL", 20)
)
SLEEP_INTERVAL = float(
    os.getenv("SLEEP_INTERVAL", 0.5)
)
CHECK_INTERVAL = float(
    os.getenv("CHECK_INTERVAL", 10)
)

USER_AGENT = os.getenv('USER_AGENT', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0')

INFLUX_HOST = os.environ['INFLUX_HOST']
INFLUX_PORT = os.getenv('INFLUX_PORT', 8086)
INFLUX_USERNAME = os.getenv('INFLUX_USERNAME', 'root')
INFLUX_PASSWORD = os.getenv('INFLUX_PASSWORD', 'root')
INFLUX_DATABASE = os.environ['INFLUX_DATABASE']

TARGETS = os.environ['TARGETS']

DATE_FROM = os.getenv("DATE_FROM")
DATE_TO = os.getenv("DATE_TO")
