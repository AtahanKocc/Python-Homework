"""
Author: Atahan Koc
Description Part: We read the binary string, traverse it string char by char, multiply it by two, and then add the int value of the binary string.
"""

def binary_to_decimal(binary):
    decimal = 0
    for b in binary:
        if b not in ['0', '1']:
            return "Invalid binary number"

        decimal = decimal * 2 + int(b)

    return decimal

print(binary_to_decimal("1001"))
print(binary_to_decimal("123"))
print(binary_to_decimal("0011"))
print(binary_to_decimal("1000"))