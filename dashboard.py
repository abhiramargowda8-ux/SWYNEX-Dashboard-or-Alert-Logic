import pandas as pd
import matplotlib.pyplot as plt

# Load simulated IoT data
data = pd.read_csv("sensor_data.csv")

# Convert timestamp to datetime
data["timestamp"] = pd.to_datetime(data["timestamp"])

# Alert threshold
TEMPERATURE_THRESHOLD = 35

# Check for high temperature readings
alerts = data[data["temperature"] >= TEMPERATURE_THRESHOLD]

# Display alert information
if not alerts.empty:
    print("ALERT: High temperature detected!")
    print(alerts[["timestamp", "temperature"]])
else:
    print("No temperature alerts detected.")

# Create dashboard chart
plt.figure(figsize=(10, 5))

plt.plot(
    data["timestamp"],
    data["temperature"],
    marker="o",
    label="Temperature (°C)"
)

# Show alert threshold
plt.axhline(
    y=TEMPERATURE_THRESHOLD,
    linestyle="--",
    label="Alert Threshold (35°C)"
)

plt.title("Simulated IoT Temperature Dashboard")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
