from datetime import datetime
from random import random, randrange

random_num = random()
print(f'Random number between 0 and 1: {random_num:.2f}')

random_num = randrange(1, 10)
print(f'Random number between 1 and 10: {random_num}')

random_year = randrange(1990, 2025)
random_month = randrange(1, 12)
random_day = randrange(1, 30)
random_date = datetime(random_year, random_month, random_day)
print(f'Random date: {random_date}')