print("Temperature conversion tool")

tempf = float(input("What is the temperature in Fahrenheit"))

tempc = (tempf - 32) * 5 / 9

print(tempf, "degrees Fahrenheit is", round(tempc), "degrees Celsius")
