import math
import random

# a positional number system way of doing it
# works up to base 10
def convert_denary(base, number):
    integer = [int(digit) for digit in str(number)]
    total = 0

    for i, digit in enumerate(integer[::-1]):
        total += int(digit) * (base ** i)

    return total

print(convert_denary(2, 111))


# division method
def denary_to_base(base, number):
    n = number
    converted = []

    while n != 0:
        remainder = n % base
        n = n // base
        converted.append(remainder)

    return "".join([str(x) for x in converted[::-1]])
    

print(denary_to_base(2, 11))


# fractional components
def convert_denary_fractional(base, number):
    integer, fractional = str(number).split(".")
    sum = 0

    for i, digit in enumerate(integer[::-1]):
        sum += int(digit) * (base ** i)

    for i, digit in enumerate(fractional, start = 1):
        sum += int(digit) * (base ** -i)

    return sum


print(convert_denary_fractional(2, 101.1))

# signed magnitude is good as it is simple, however it makes arithmetic hard 
# it essentially suggests that the MSB is a sign bit
def convert_denary_signed_magnitude(base, number):
    integer = [int(digit) for digit in str(number)]
    sign = integer.pop(0)
    total = 0

    for i, digit in enumerate(integer[::-1]):
        total += int(digit) * (base ** i)

    return total if sign == 0 else -total

print(convert_denary_signed_magnitude(2, 100001))

def convert_to_ones_complement(number, bits):
    base_two = denary_to_base(2, abs(number))
    remaining = bits - len(base_two)
    trailing = [0 for _ in range(remaining)]
    trailing.extend(int(digit) for digit in base_two)

    if number < 0:
        for i in range(len(trailing)): trailing[i] = 1 - trailing[i]

    return "".join([str(x) for x in trailing])

def convert_to_twos_complement(number, bits):
    base_two = denary_to_base(2, abs(number))
    remaining = bits - len(base_two)
    trailing = [0 for _ in range(remaining)]
    trailing.extend(int(digit) for digit in base_two)

    if number < 0:
        for i in range(len(trailing) - 1, -1, -1):
            if trailing[i] == 1: # once a one is found, start flipping all the bits after
                break
            trailing[i] = 0

        # flips all the bits
        for i in range(i - 1, -1, -1):
            trailing[i] = 1 - trailing[i]

    return "".join([str(x) for x in trailing])


print(convert_to_ones_complement(-14, 5))
print(convert_to_ones_complement(14, 5))
print(convert_to_twos_complement(-14, 5))
print(convert_to_twos_complement(14, 5))