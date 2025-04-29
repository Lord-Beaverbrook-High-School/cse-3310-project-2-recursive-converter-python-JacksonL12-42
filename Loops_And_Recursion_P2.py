# Accepts base-10 and converts to base-2 as a string.
def dectoBin(base10):
    # Base case: if base-10 is 0, return 0
    if base10 == 0:
        return "0"
    # Base case: if base-10 is 1, return 1
    elif base10 == 1:
        return "1"
    else:
        # Recursive case: get the remainder and quotient of base-10 divided by 2
        remainder = base10 % 2
        quotient = base10 // 2
        # If the quotient is 0,return the remainder
        if quotient == 0:
            return str(remainder)
        # If quotient is not 0, recursively call the function with the quotient and append the remainder
        else:
            return dectoBin(quotient) + str(remainder)
#print("Dec to bin method:", dectoBin(456))

# Accepts base-10 and converts to base-16 as a string.
def dectoHex(base10):
    # Define the base-16 digits
    digits = "0123456789ABCDEF"
    # Base case: if base-10 is 0, return 0
    if base10 == 0:
        return "0"
    # Recursive case: get the remainder and quotient of base-10 divided by 16
    elif base10 < 16:
        # If base-10 is less than 16, return the base-16 digit
        return digits[base10]
    else:
        # Recursive call with the quotient, and append the remainder's digit
        return dectoHex(base10 // 16) + digits[base10 % 16]
#print("Dec to hex method:", dectoHex(45678))

# Accepts base-2 and converts to base-10 as a string.
def bintoDec(base2):
    # Base case: if the string is empty, return 0
    if base2 == "":
        return 0
    # Recursive case: convert the binary digit to base 10 and add to the result of the recursive call
    else:
        # Convert the final binary digit to base 10
        decimal_digit = int(base2[-1])
        # Recursively call with the base-2 string excluding the last digit
        return decimal_digit + 2 * bintoDec(base2[:-1])

#print("Bin to dec method:", bintoDec("101010101"))

# Accepts base-16 and converts to base-10 as a string.
def hextoDec(base16):
    # Base case: empty string
    if base16 == "":
        return '0'
    # Dictionary mapping hex digits to decimal values
    hex_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11,
        'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    # Recursive case
    if len(base16) == 1:
        # Return decimal value of single base-16 digit as a string
        return str(hex_map[base16])
    else:
        # Calculate decimal value of first base-16 digit
        first_digit_value = hex_map[base16[0]] * (16 ** (len(base16) - 1))
        # Recursively convert remaining base-16
        remaining_value = int(hextoDec(base16[1:]))
        # Return value of first digit and remaining value as a string
        return str(first_digit_value + remaining_value)

#print("Hex to dec method:", hextoDec("1C2A3"))

def main():
    print("Testing of hextoDec method converting base-16 to base-10 using the input:\"1C2A3\"")
    print("Hex to dec method:", hextoDec("1C2A3"))
    print("When input has length of one, using 'C' should be = 12: ",hextoDec("C"))
    print ("When input has length more than one, using 'C2A' should be = 3114: ", hextoDec("C2A"))
    print("Testing of dectoHex method converting base-10 to base-16 using the input:45678")
    print("Dec to Hex method:", dectoHex(45678))
    print("When input has length of one, using '9' should be = 9: ",hextoDec("9"))
    print ("When input has length more than one, using '3114' should be = C2A: ", dectoHex(3114))
    print("Testing of bintoDec method converting base-2 to base-10 using the input:\"101010101\"")
    print("Bin to dec method:", bintoDec("101010101"))
    print("When input has length of one, using '1' should be = 1: ",bintoDec("1"))
    print ("When input has length more than one, using '1011' should be = 3F3: ", dectoHex(1011))
    print("Testing of dectoBin method converting base-10 to base-2 using the input:456")
    print("Dec to bin method:", dectoBin(456))
    print("When input has length of one, using '1' should be = 1: ",dectoBin(1))
    print ("When input has length more than one, using '101' should be = 1011: ", dectoHex(101))

# Descriptions of how the code is working is in methods as well as inspiration.
main()