def hexg(number):
    # Convert the number to hexadecimal
    a = hex(number)[2:].upper()

    # Ensure the hexadecimal string has an even length by adding a leading 0 if necessary
    if len(a) % 2 != 0:
        a = '0' + a
    print("Hexadecimal representation:", a)

    # Split the string into pairs of hex digits (bytes)
    b = [a[i:i+2] for i in range(0, len(a), 2)]
    
    # Find the number of bytes
    n = len(b)
    
    if n <= 2:
        # No rearrangement needed for 1 or 2 bytes
        print("No mid-endian possible, returning original hex.")
        print(''.join(b))
        return
    
    # The first two bytes are the most significant (MSB)
    mid = b[:2]   # The first two bytes
    rest = b[2:]  # The remaining bytes
    
    # Prepare the final result: alternating left and right placement around the middle part
    left = []
    right = []
    
    # Alternating the rest of the bytes
    for i in range(len(rest)):
        if i % 2 == 0:
            left.append(rest[i])
        else:
            right.append(rest[i])
    
    # The final list is left + mid + right
    result = right + mid + left
    
    # Join the result list into a string and print
    print("Mid-endian result:", ''.join(result))

# Input and function call
a = int(input("Enter the decimal value: "))  # Convert input to integer
hexg(a)
