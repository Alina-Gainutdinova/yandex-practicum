# подключите библиотеку datetime под именем dt
import datetime as dt
start_moment = dt.datetime(2022, 2, 26) # Напишите код здесь
current_moment = dt.datetime(2022, 3, 17)  # и здесь

total_time = current_moment - start_moment  # и здесь

print(total_time)