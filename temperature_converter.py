def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


choice = input("Convert to (F)ahrenheit or (C)elsius? ")

if choice == "F":
    celsius = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(celsius)
    print("Temperature in Fahrenheit:", result)

elif choice == "C":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(fahrenheit)
    print("Temperature in Celsius:", result)

else:
    print("Invalid choice")