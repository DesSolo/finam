from influxdb import InfluxDBClient
from api import ExportFinam
import config


def to_iso_time(item):
    year = item['date'][0:4]
    mont = item['date'][4:6]
    day = item['date'][6:8]
    return f"{year}-{mont}-{day}T{item['time']}Z"


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


if __name__ == '__main__':
    influx_client = InfluxDBClient(
        config.INFLUX_HOST,
        config.INFLUX_PORT,
        config.INFLUX_USERNAME,
        config.INFLUX_PASSWORD,
        config.INFLUX_DATABASE
    )
    exporter = ExportFinam(config.USER_AGENT)
    for target in config.TARGETS.split(','):
        em, name = map(lambda x: x.strip(), target.split(':'))
        payload = to_influx(exporter.export(em, name))
        influx_client.write_points(payload, time_precision='ms')
