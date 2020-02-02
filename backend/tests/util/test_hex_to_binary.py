from backend.util.hex_to_binary import hex_to_bin

def test_hex_to_binary():
    number = 123
    hex_num = hex(number)[2:]
    binary = hex_to_bin(hex_num)
    orig_num = int(binary,2)

    assert orig_num == number