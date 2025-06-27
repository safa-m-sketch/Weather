import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
import requests
print(requests.__version__)
root = tk.Tk()
root.configure(bg = "#FFE2A3")
root.geometry("400x400")
#insert your own API key here
api_key = ''
label = tk.Label(root, text = "Enter city:", font = ("Courier", 16, "bold"), fg = "#FF8410", bg = "#FFE2A3")
label.pack(pady=5)
city_input = tk.Entry(root, font = ("Courier", 16), width = 20, justify = "center", bg = "#FFFFE4")
city_input.pack(pady=3)

#use labels for parts of output
city_label = tk.Label(root, text="", font=("FreeMono", 30, "bold"), bg="#FFE2A3", fg = "#FF7070")
city_label.pack(pady=(20, 0))

image_label = tk.Label(root, text="", font=("Segoe UI Emoji", 40), bg="#FFE2A3", fg = "#FF7300")
image_label.pack()

overalltemp_label = tk.Label(root, text="", font=("FreeMono", 35), bg="#FFE2A3")
overalltemp_label.pack()

feelslike_label = tk.Label(root, text="", font=("FreeMono", 16), bg="#FFE2A3", fg = "#FF70D4")
feelslike_label.pack()

highlow_label = tk.Label(root, text="", font=("FreeMono", 16), bg="#FFE2A3", fg = "#C670FF")
highlow_label.pack()

# method to determine which image gets outputted on screen (depending on description of the whether clear, cloudy, etc)
def get_image(c):
    description = c.lower()
    if "clear" in description:
        return "☀️"
    elif "cloud" in description:
        return "☁️"
    elif "rain" in description or "drizzle" in description:
        return "🌧️"
    elif "storm" in description or "thunder" in description:
        return "⛈️"
    elif "snow" in description:
        return "🌨️"
    else:
        return "🌤️"

#Checks if it is a city and if not show warning
def presentWeather():
    city = city_input.get()
    if not city:
        messagebox.showwarning("Error", "Enter valid city!")
        return 
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

    # Make sure everything works smoothly before extracing information
    if data.status_code == 200:
        weather_data = data.json()
        if weather_data.get('cod') == '404':
            messagebox.showwarning("Error", "Enter valid city!")
            return
        cur_weather = data.json()['weather'][0]['main']
        overall_temp = round(data.json()['main']['temp'])
        feel_like = round(data.json()['main']['feels_like'])
        min_temp = round(data.json()['main']['temp_min'])
        max_temp = round(data.json()['main']['temp_max'])

    #Outputs
        city_label.config(text = city)
        image_label.config(text = get_image(cur_weather))
        overalltemp_label.config(text = f"{overall_temp}°F")
        feelslike_label.config(text = f"Feels like: {feel_like}°F")
        highlow_label.config(text = f"H: {max_temp}   L: {min_temp}")

    else:
        messagebox.showerror("API Error", f"Status code: {data.status_code}")

#Connect the return key to input area
root.bind("<Return>", lambda event: presentWeather())
root.mainloop()