def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def convert_temperature(value, input_unit, output_unit):
    input_unit = input_unit.lower()
    output_unit = output_unit.lower()
    
    # Convert input to Celsius first
    if input_unit == 'c':
        celsius = value
    elif input_unit == 'f':
        celsius = fahrenheit_to_celsius(value)
    elif input_unit == 'k':
        celsius = kelvin_to_celsius(value)
    else:
        return None  # Invalid input unit
    
    # Convert Celsius to output unit
    if output_unit == 'c':
        return celsius
    elif output_unit == 'f':
        return celsius_to_fahrenheit(celsius)
    elif output_unit == 'k':
        return celsius_to_kelvin(celsius)
    else:
        return None  # Invalid output unit

def main():
    print("Temperature Conversion Program")
    while True:
        try:
            value = float(input("Enter temperature value: "))
            input_unit = input("Enter input unit (C, F, K): ").strip()
            output_unit = input("Enter output unit (C, F, K): ").strip()
            
            result = convert_temperature(value, input_unit, output_unit)
            
            if result is None:
                print("Invalid unit entered. Please enter C, F, or K.")
                continue
            
            print(f"{value} {input_unit.upper()} is {result:.2f} {output_unit.upper()}")
            
            cont = input("Convert another temperature? (y/n): ").strip().lower()
            if cont != 'y':
                print("Exiting the program.")
                break
        except ValueError:
            print("Invalid input. Please enter numeric temperature value.")

if __name__ == "__main__":
    main()
