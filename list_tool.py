def find_max(numbers):
    if not numbers:
        raise ValueError("List is empty")
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest