import logging
from time import sleep
from influxdb import InfluxDBClient
from api import ExportFinam
import config

logging.basicConfig(
    filename="/dev/stdout",
    level=config.LOGGING_LEVEL,
    format="%(asctime)-15s:%(levelname)s:%(message)s"
)


def to_iso_time(item):
    year = item['date'][0:4]
    mont = item['date'][4:6]
    day = item['date'][6:8]
    return f"{year}-{mont}-{day}T{item['time']}+03:00"


def to_influx(export):
    response = []
    for item in export:
        response.append(
            {
                "measurement": "stock_quotes",
                "tags": {
                    "code": item['ticker']
                },
                "time": to_iso_time(item),
                "fields": {
                    "close": float(item['close'])
                }
            }
        )
    return response


def show_current_config():
    params = []
    for value in config.env_values:
        params.append(
            f"{value}: {getattr(config, value)}"
        )
    return '\n'.join(params)


def run_forever(api_exporter, influx_db_client, targets):
    while True:
        for target in targets:
            em, name = map(lambda x: x.strip(), target.split(':'))
            payload = to_influx(
                api_exporter.export(em, name, config.DATE_FROM, config.DATE_TO)
            )
            result = influx_db_client.write_points(payload, time_precision='ms')
            logging.info("target: %s write: %s success: %s", target, len(payload), result)
            logging.debug("start sleep: %s seconds after single target", config.SLEEP_INTERVAL)
            sleep(config.SLEEP_INTERVAL)
        logging.info("start sleep: %s seconds after all targets", config.SLEEP_INTERVAL)
        sleep(config.CHECK_INTERVAL)


if __name__ == '__main__':
    if config.LOGGING_LEVEL == logging.DEBUG:
        logging.debug(show_current_config())

    influx_client = InfluxDBClient(
        config.INFLUX_HOST,
        config.INFLUX_PORT,
        config.INFLUX_USERNAME,
        config.INFLUX_PASSWORD,
        config.INFLUX_DATABASE
    )
    exporter = ExportFinam(config.USER_AGENT)

    run_forever(
        exporter,
        influx_client,
        config.TARGETS.split(',')
    )
