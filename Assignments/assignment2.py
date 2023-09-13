# part 1

# 1. Python is a **high-level** programming language known for its simplicity and readability.

# 2. In Python, you can use the print() function to display information in the **console**.

# 3. A **variable** is a named container for storing data that can change during program execution.

# 4. In Python, variable names are case-**sensitive**.

# 5. The three fundamental data types in Python are **integers**, **list**, and **strings**.

# 6. To declare a variable in Python, you simply provide a name and assign a **value** to it.

# 7. The + operator is used for **adding** two numbers in Python.

# 8. The * operator is used for **multiplying** two numbers in Python.

# 9. The str function can be used to convert a **value** to a string data type.

# 10. To perform integer division (floor division) in Python, you can use the **//** operator.









# part 2

# Program 1: Convert Dollar to Local Currency

# Get the dollar amount from the user
dollars = float(input("Enter the amount in dollars: "))

# Define the exchange rate (replace with your local currency's exchange rate)
exchange_rate = 6.99

# Convert dollars to local currency
local_currency = dollars * exchange_rate

# Display the result
print(f"{dollars} dollars is equal to {local_currency} in local currency.")





# Program 2: Convert Temperature (Celsius to Fahrenheit and Vice Versa)
# Program to Convert Fahrenheit to Celsius

# Input the temperature in Celsius from the user and convert it to a float
celsius_temperature = float(input("Enter the temperature value: "))

# Convert the Celsius temperature to Fahrenheit using the formula (Celsius * 9/5) + 32
fahrenheit = float(celsius_temperature) * 9/5 + 32

# Display the result in Fahrenheit and its equivalent in Celsius
print(f"{fahrenheit} Fahrenheit is equal to {celsius_temperature} Celsius")

# Program to Convert Celsius To Fahrenheit

# Input the temperature in Fahrenheit from the user and convert it to a float
fahrenheit_temperature = float(input("Enter the temperature value: "))

# Convert the Fahrenheit temperature to Celsius using the formula (Fahrenheit - 32) * 5/9
celsius = (float(fahrenheit_temperature) - 32) * 5/9

# Display the result in Celsius and its equivalent in Fahrenheit
print(f"{celsius} Celsius is equal to {fahrenheit_temperature} Fahrenheit")


     
# Program 3: Convert Hours to Seconds

# Get the number of hours from the user
hours = float(input("Enter the number of hours: "))

# Convert hours to seconds
seconds = hours * 3600  # 1 hour = 3600 seconds

# Display the result
print(f"{hours} hours is equal to {seconds} seconds.")

