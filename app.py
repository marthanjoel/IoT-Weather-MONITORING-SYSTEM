import tkinter as tk
import random
import time

def update_weather():
    # Simulate weather data
    temp = random.randint(18, 35)        # Temperature in Celsius
    humidity = random.randint(30, 90)    # Humidity percentage
    pressure = random.randint(950, 1050) # Atmospheric pressure hPa

    temp_label.config(text=f"🌡 Temperature: {temp} °C")
    humidity_label.config(text=f"💧 Humidity: {humidity} %")
    pressure_label.config(text=f"⏲ Pressure: {pressure} hPa")

    # refresh every 2 seconds
    root.after(2000, update_weather)

# Create window
root = tk.Tk()
root.title("IoT Weather Monitoring System")
root.geometry("400x250")
root.configure(bg="lightblue")

title_label = tk.Label(root, text="IoT Weather Station", font=("Arial", 18, "bold"), bg="lightblue")
title_label.pack(pady=15)

temp_label = tk.Label(root, text="", font=("Arial", 14), bg="lightblue")
temp_label.pack(pady=5)

humidity_label = tk.Label(root, text="", font=("Arial", 14), bg="lightblue")
humidity_label.pack(pady=5)

pressure_label = tk.Label(root, text="", font=("Arial", 14), bg="lightblue")
pressure_label.pack(pady=5)

# Start updates
update_weather()

# Run GUI loop
root.mainloop()
