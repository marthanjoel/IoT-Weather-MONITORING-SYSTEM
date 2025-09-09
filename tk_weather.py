import tkinter as tk
import random
import time

def update_values():
    # Simulate temperature and humidity readings
    temperature = round(random.uniform(20, 35), 2)
    humidity = round(random.uniform(40, 80), 2)

    temp_label.config(text=f"🌡️ Temperature: {temperature} °C")
    hum_label.config(text=f"💧 Humidity: {humidity} %")

    # Refresh every 2 seconds
    root.after(2000, update_values)

# Tkinter window setup
root = tk.Tk()
root.title("Weather Monitoring System")
root.geometry("400x200")
root.config(bg="lightblue")

title_label = tk.Label(root, text="🌦️ IoT Weather Monitoring System", 
                       font=("Arial", 14, "bold"), bg="lightblue")
title_label.pack(pady=10)

temp_label = tk.Label(root, text="", font=("Arial", 12), bg="lightblue")
temp_label.pack(pady=5)

hum_label = tk.Label(root, text="", font=("Arial", 12), bg="lightblue")
hum_label.pack(pady=5)

# Start updating values
update_values()

root.mainloop()
