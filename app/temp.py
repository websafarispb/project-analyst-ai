import sys

def is_lucky(ticket):
    if not ticket.isdigit():
        return False

    digits = [int(char) for char in ticket]
    middle = len(digits) // 2

    first_half = digits[:middle]
    second_half = digits[middle:]

    sum_first = sum(first_half)
    sum_second = sum(second_half)

    return sum_first == sum_second

print(is_lucky("123321"), file=sys.stdout ) # True  (1+2+3 == 3+2+1)
print(is_lucky("123456") , file=sys.stdout) # False (1+2+3 != 4+5+6)
print(is_lucky("000000") , file=sys.stdout) # True  (0+0+0 == 0+0+0)