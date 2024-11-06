# 371
# TC : O(1)
# SC : O(1)
"""
1. Understand how 2's compliment bits actually stored in memory.
2. Use `XOR`, `AND` and `shift` to simulate add operation.
3. After bit operation, MSB remains as MSB, non-MSB remain as non-MSB.
3. If there is a negative number exist,
when using `AND` and `shift` operation to simulate the carry out process,
python will actually keep that carry out bit. So it's possible that the simulation procees won't stop.
4. So using fixed length 32-bits mask to check if we should stop the process.
"""


#import struct
#bits = struct.unpack('I', struct.pack('i', x))[0]
#bit_string = f'{bits:032b}'

def getSum(a: int, b: int) -> int:
    MASK = 0xFFFFFFFF  # Mask to keep 32 bits

    while (b&MASK) != 0:
        a, b = a^b, (a&b)<<1

    return (a&MASK) if b > 0 else a
