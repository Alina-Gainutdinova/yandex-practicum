def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    # Напишите код функции calc_stat()
    N = len(listened)
    summ = 0
    for M in listened:
        summ += M
    M = summ // 60
    return f'Вы прослушали {N} песен общей продолжительностью {M} минут.'
print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))