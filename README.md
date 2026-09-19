# IoT Data Dashboard

This project visualizes simulated IoT sensor data and defines an alert rule for high temperature.

## Features

- Simulated temperature readings
- Simulated humidity readings
- Temperature visualization using Python
- High-temperature alert detection

## Alert Rule

An alert is triggered when:

**Temperature >= 35°C**

When the temperature reaches or exceeds 35°C, the dashboard prints:

`ALERT: High temperature detected!`

## Files

- `dashboard.py` - Creates the chart and checks the alert threshold.
- `sensor_data.csv` - Contains simulated IoT sensor readings.
- `README.md` - Project documentation.

## How to Run

Install the required Python libraries:

```bash
pip install pandas matplotlib
