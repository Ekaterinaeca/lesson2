import math

def square(side):
    area = side * side
    if not isinstance(area, int):
        return math.ceil(area)
    return area

# Пример использования
side = 5.5
print(square(side))  # Output: 21