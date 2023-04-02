import random
import random

def generate_sum_list(count):
    lst = []
    total = 0
    while total < count:
        value = random.randint(1, count - total)
        lst.append(value)
        total += value
    return lst


print(generate_sum_list(20))