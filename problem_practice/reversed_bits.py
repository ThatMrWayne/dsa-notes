# 190


def reverseBits(n: int) -> int:
    bit_string = f'{n:032b}'
    reverse_bit_str = bit_string[-1::-1]
    return int(reverse_bit_str, 2)
