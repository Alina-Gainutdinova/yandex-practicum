import datetime as dt

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

def what_time(city):
    # Напишите код тела функции;
    # она должна вернуть текущее время в городе city
    now_time = dt.datetime.utcnow()
    city_time = dt.timedelta(hours = UTC_OFFSET[city])
    total_time = now_time + city_time
    return total_time
        

print(what_time('Екатеринбург'))