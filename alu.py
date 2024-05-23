from machine import Pin
import utime

delay = 0.05
# Define input and output pins
input_pins = [Pin(i, Pin.IN) for i in range(16, 24)]  # Input pins 16-23
output_pins = [Pin(i, Pin.OUT) for i in range(12, 16)]  # Output pins 12-15 (to 7-segment decoder)
control_pins = [Pin(i, Pin.OUT) for i in range(9, 12)]  # Control pins 9-11 (for each 7-segment display)

def binary_to_decimal(binary_value):
    """Converts an 8-bit binary value to a decimal integer."""
    decimal = 0
    for i, bit in enumerate(reversed(binary_value)):
        decimal += bit * (2**i)
    return decimal

def separate_digits(decimal_value):
    """Separates the digits of a decimal integer into a list."""
    digits = [0, 0, 0]  # Initialize list with default values
    str_value = str(decimal_value)
    for i, digit_char in enumerate(reversed(str_value)):
        if i > 2:  # Limit to 3 digits
            break
        digits[2 - i] = int(digit_char)
    return digits


def decimal_to_bcd(decimal_digit):
    """Converts a decimal digit (0-9) to its 4-bit BCD representation."""
    binary_string = bin(decimal_digit)[2:]  # Convert to binary string
    bcd = [0] * (4 - len(binary_string)) + [int(bit) for bit in binary_string]  # Pad with leading zeros if necessary
    return bcd


while True:
    # 1. Read input binary value
    binary_value = [pin.value() for pin in input_pins]
    print(binary_value)

    # 2. Convert binary to decimal
    decimal_value = binary_to_decimal(binary_value)

    # 3. Separate digits
    digits = separate_digits(decimal_value)

    # 4. Display each digit on the 7-segment displays
    defult_bcd = [0,0,0,0]

    for c_pin, digit in zip(control_pins, digits):

        for pin in control_pins:
            pin.value(0)

        c_pin.value(1)
        bcd_value = decimal_to_bcd(digit)
        for i, bit in enumerate(bcd_value):
            output_pins[i].value(int(bit))
            
        utime.sleep(delay)