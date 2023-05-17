#try:
    # Здесь написан код, который в некоторых ситуациях
    # может создать исключение (может "выбросить исключение", как говорят разработчики).
    # Программа попробует (try) выполнить этот код.
#except TypeError1:
    # Здесь описываем, что следует делать,
    # если будет "выброшено" исключение типа TypeError1.
#except TypeError2:
      # А здесь разработчик описывает, как быть, если перехвачено
    # исключение типа TypeError2.
# вот функция, которая может выбросить исключение
def calc_share(apples, friends):
    # от строки откусываем число и приводим к типу int
    friends_number = int(friends.split()[0])
    return apples/friends_number

# есть 17 яблок
apples = 17

# будем считать, сколько достанется каждому другу
# вызовем функцию calc_share() для разных наших знакомых,
# с различным числом друзей
for friends in ['7 друзей', '2 друга', '0 друзей', 'один враг']:
        try:
                print('Каждому достанется по', calc_share(apples, friends), 'яблока')
        except ZeroDivisionError:
                print('На ноль делить нельзя.')
        except ValueError:
                print(f'Из строки "{friends}" не получилось достать число.')