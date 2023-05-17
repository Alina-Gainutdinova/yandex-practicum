user_query = 'как стать бэкенд-разработчиком'
query = '%20'.join(user_query.split(' '))


url = 'https://yandex.ru/search/?text=' + query # ваш код здесь

print(url)