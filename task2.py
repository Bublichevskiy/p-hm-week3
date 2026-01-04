import random

def get_number_ticket(min, max, qua):
    if min < 1 or max > 1000 or qua < 1 or qua > (max - min + 1):
        print("Помилка")
        return []

    numbers_set = set()

    while len(numbers_set) < qua:
        numbers = random.randint(min, max)
        numbers_set.add(numbers)

    return sorted(numbers_set)

lottery_numbers = get_number_ticket(1, 49, 6)
if lottery_numbers:
    print("Ваші числа:", lottery_numbers)