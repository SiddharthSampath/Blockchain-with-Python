from backend.util.crypto_hash import crypto_hash
hex_to_bin_dict = {'0' : '0000',
              '1' : '0001',
              '2' : '0010',
              '3' : '0011',
              '4' : '0100',
              '5' : '0101',
              '6' : '0110',
              '7' : '0111',
              '8' : '1000',
              '9' : '1001',
              'a' : '1010',
              'b' : '1011',
              'c' : '1100',
              'd' : '1101',
              'e' : '1110',
              'f' : '1111'}

def hex_to_bin(hex):

    binary = ""
    for char in hex:
        binary += hex_to_bin_dict[char]
    return binary

def main():
    num = 111
    print(f'Initial num is : {num}')
    hex_num = hex(num)
    print(f'Hex num is : {hex_num}')

    binary = hex_to_bin(hex_num[2:])
    print(f'Binary of num : {binary}')

    print(f"Decimal rep is : {int(binary,2)}")

if __name__ == "__main__":
    main()
     