def month_to_season(month_num):
    seasons = {1: 'Зима', 2: 'Весна', 3: 'Лето', 7: 'Лето', 4: 'Осень'}
    return seasons[month_num]

print(month_to_season(2)) # Вывод: Весна