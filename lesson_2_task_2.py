def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

# Пример использования
year = 2025
is_leap = is_year_leap(year)
print(f'Год {year}: {is_leap}')