import tkinter as tk
import random
import time

# Function to update sensor values
def update_values():
    temperature = round(random.uniform(20, 35), 1)  # °C
    humidity = round(random.uniform(40, 80), 1)     # %
    pressure = round(random.uniform(1000, 1025), 1) # hPa

    temp_label.config(text=f"🌡️ Temperature: {temperature} °C")
    hum_label.config(text=f"💧 Humidity: {humidity} %")
    pres_label.config(text=f"⛰️ Pressure: {pressure} hPa")

    # Refresh every 2 seconds
    root.after(2000, update_values)

# Create window
root = tk.Tk()
root.title("IoT Weather Monitoring Dashboard")
root.geometry("400x250")
root.configure(bg="#e3f2fd")

# Title
title = tk.Label(root, text="Weather Monitoring System 🌦️", font=("Arial", 16, "bold"), bg="#e3f2fd")
title.pack(pady=10)

# Sensor labels
temp_label = tk.Label(root, text="🌡️ Temperature: -- °C", font=("Arial", 14), bg="#e3f2fd")
temp_label.pack(pady=5)

hum_label = tk.Label(root, text="💧 Humidity: -- %", font=("Arial", 14), bg="#e3f2fd")
hum_label.pack(pady=5)

pres_label = tk.Label(root, text="⛰️ Pressure: -- hPa", font=("Arial", 14), bg="#e3f2fd")
pres_label.pack(pady=5)

# Start updating values
update_values()

# Run GUI
root.mainloop()
