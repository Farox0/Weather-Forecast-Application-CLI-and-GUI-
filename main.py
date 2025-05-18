import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your API key
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# CLI Version
def get_weather(city):
    response = requests.get(API_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description']}, {data['main']['temp']}°C")
    else:
        print("City not found!")

# GUI Version
def fetch_weather():
    city = city_entry.get()
    response = requests.get(API_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
    if response.status_code == 200:
        data = response.json()
        result = f"Weather: {data['weather'][0]['description']}, {data['main']['temp']}°C"
        messagebox.showinfo("Weather Info", result)
    else:
        messagebox.showerror("Error", "City not found!")

# GUI Setup
app = tk.Tk()
app.title("Weather Forecast")
app.geometry("300x150")

city_label = tk.Label(app, text="Enter City:")
city_label.pack()
city_entry = tk.Entry(app)
city_entry.pack()

fetch_button = tk.Button(app, text="Get Weather", command=fetch_weather)
fetch_button.pack()

app.mainloop()

# CLI Execution
def main():
    import argparse
    parser = argparse.ArgumentParser(description="Weather Forecast CLI")
    parser.add_argument('--city', help="City name for weather forecast")

    args = parser.parse_args()

    if args.city:
        get_weather(args.city)

if __name__ == '__main__':
    main()
