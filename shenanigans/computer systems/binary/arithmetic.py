# unsigned
def add_trailing_zeros(bin_one, bin_two):
    if len(bin_one) == len(bin_two):
        nums = (bin_one, bin_two)

    if len(bin_one) > len(bin_two):
        trailing = len(bin_one) - len(bin_two)
        zeroes = [0] * trailing
        zeroes.extend(bin_two)
        nums = (bin_one, zeroes)

    if len(bin_one) < len(bin_two):
        trailing = len(bin_two) - len(bin_one)
        zeroes = [0] * trailing
        zeroes.extend(bin_one)
        nums = (zeroes, bin_two)

    return nums

def overflow_unsigned(num, bits):
    length = len(num)
    while length != bits:
        num.pop(0)
        length -= 1

    return num

def bit_addition(digit_one, digit_two, carry):
    nums = [digit_one, digit_two, carry]
    if sum(nums) == 3: return (1, 1)
    if sum(nums) == 2: return (0, 1)
    if sum(nums) == 1: return (1, 0)
    if sum(nums) == 0: return (0, 0)

def bit_subtraction(digit_one, digit_two, borrow):
    result = digit_one - digit_two - borrow

    if result == -1: return (1, 1)
    if result == -2: return (0, 1)
    if result == 0: return (0, 0)
    if result == 1: return (1, 0)


def addition(num_one, num_two, bits):
    bin_one = [int(b) for b in str(num_one)]
    bin_two = [int(b) for b in str(num_two)]
    bin_result = []

    bin_one, bin_two = add_trailing_zeros(bin_one, bin_two)
    bin_one.reverse(), bin_two.reverse()

    carry = 0

    for i, bit in enumerate(bin_one):
        res_bit, carry = bit_addition(bin_one[i], bin_two[i], carry)
        bin_result.append(res_bit)

    if carry: bin_result.append(carry)

    bin_result.reverse()

    if len(bin_result) > bits:
        bin_result = overflow_unsigned(bin_result, bits)

    result = "".join(str(b) for b in bin_result)

    return result


def subtraction(num_one, num_two, bits):
    bin_one = [int(b) for b in str(num_one)]
    bin_two = [int(b) for b in str(num_two)]
    bin_result = []

    bin_one, bin_two = add_trailing_zeros(bin_one, bin_two)

    bin_one.reverse()
    bin_two.reverse()

    borrow = 0

    for i, bit in enumerate(bin_one):
        res_bit, borrow = bit_subtraction(bin_one[i], bin_two[i], borrow)
        bin_result.append(res_bit)

    bin_result.reverse()

    if len(bin_result) > bits:
        bin_result = overflow_unsigned(bin_result, bits)

    result = "".join(str(b) for b in bin_result)

    return result

def multiplication(num_one, num_two, bits):
    bin_one = [int(b) for b in str(num_one)]
    bin_two = [int(b) for b in str(num_two)]
    bin_temps = []
    result = []

    bin_one.reverse()

    for i, bit in enumerate(bin_one):
        if bit == 1:
            zeroes = [0] * i
            zeroes.extend(bin_two)
            bin_temps.append(zeroes)

        if bit == 0:
            continue

        if len(bin_temps) == 2:
            temp = addition("".join(str(b) for b in bin_temps[0]), "".join(str(b) for b in bin_temps[1]), bits)

            bin_temps.pop(0)
            bin_temps.pop(0)
            bin_temps.append([int(b) for b in temp])

    if bin_temps: result = bin_temps[0]

    return "".join(str(b) for b in result)
    