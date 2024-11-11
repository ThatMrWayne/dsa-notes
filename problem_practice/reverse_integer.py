# 7
# TC : O(log10(x))
# SC : O(1)


# by calculation
def reverse(x: int) -> int:
    total = 0
    is_neg = True if x < 0 else False
    x = x*-1 if is_neg else x

    while x != 0:
        remainder = x % 10
        total = total*10 + remainder
        x = x//10

    result = total*-1 if is_neg else x
    return result if -2**31 <= result <= 2**31-1 else 0


# naive method
def reverse(x: int) -> int:
    # two's compliment
    if x == 0:
        return 0
    is_neg = False
    if x < 0:
        is_neg = True
        x = x*-1
    l = list(str(x))
    for i in range(len(l)-1, -1, -1):
        if l[i] != '0':
            break
        elif l[i] == '0':
            l.pop()
    l.reverse()
    result = int(''.join(l))
    result = result * -1 if is_neg else result
    return result if -2**31 <= result <= 2**31-1 else 0
