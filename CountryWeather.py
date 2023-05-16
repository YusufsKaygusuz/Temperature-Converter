import requests

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin

def get_istanbul_temperature():
    url = "http://api.openweathermap.org/data/2.5/weather?q=Istanbul,tr&appid=YOUR_API_KEY"
    response = requests.get(url)
    data = response.json()
    temperature_kelvin = data["main"]["temp"]
    return temperature_kelvin

# İstanbul'un anlık sıcaklık değerini alınması
temperature_kelvin = get_istanbul_temperature()

# Sıcaklık birimlerine dönüşümün yapılması
temperature_celsius = kelvin_to_celsius(temperature_kelvin)
temperature_fahrenheit = kelvin_to_fahrenheit(temperature_kelvin)

# Sonuçların ekrana yazdırılması
print(f"Istanbul sıcaklık:")
print(f"Celsius (C): {temperature_celsius}°C")
print(f"Kelvin (K): {temperature_kelvin} K")
print(f"Fahrenheit (F): {temperature_fahrenheit}°F")
