import os

USER_AGENT = os.getenv('USER_AGENT', 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0')
INFLUX_HOST = os.environ['INFLUX_HOST']
INFLUX_PORT = os.getenv('INFLUX_PORT', 8086)
INFLUX_USERNAME = os.getenv('INFLUX_USERNAME', 'root')
INFLUX_PASSWORD = os.getenv('INFLUX_PASSWORD', 'root')
INFLUX_DATABASE = os.environ['INFLUX_DATABASE']
TARGETS = os.environ['TARGETS']
