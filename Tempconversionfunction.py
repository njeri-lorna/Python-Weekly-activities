# Define the function
def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Ask the user to enter temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Call the function
fahrenheit = convert_temperature(celsius)

# Display the converted temperature
print("Temperature in Fahrenheit:", format(fahrenheit, ".2f"))
