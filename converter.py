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

def convert_temperature(value, unit_from, unit_to):
    if unit_from == "C" and unit_to == "K":
        result = celsius_to_kelvin(value)
        return result
    elif unit_from == "K" and unit_to == "C":
        result = kelvin_to_celsius(value)
        return result
    elif unit_from == "C" and unit_to == "F":
        result = celsius_to_fahrenheit(value)
        return result
    elif unit_from == "F" and unit_to == "C":
        result = fahrenheit_to_celsius(value)
        return result
    elif unit_from == "K" and unit_to == "F":
        result = kelvin_to_fahrenheit(value)
        return result
    elif unit_from == "F" and unit_to == "K":
        result = fahrenheit_to_kelvin(value)
        return result
    else:
        print("Geçersiz birimler. Lütfen Celsius (C), Kelvin (K) veya Fahrenheit (F) kullanın.")

# Kullanıcıdan giriş alınması
value = float(input("Dönüştürülecek sıcaklık değerini girin: "))
unit_from = input("Başlangıç birimini girin (C, K, F): ")
unit_to = input("Dönüşüm birimini girin (C, K, F): ")

# Sıcaklık dönüşümünün yapılması
result = convert_temperature(value, unit_from, unit_to)
if result is not None:
    print(f"{value} {unit_from} = {result} {unit_to}")