import sys

sys.path.append('../../..')
from utils import get_data

data = get_data()

general_number = 0
search_number = 0
for i in data:
    general_number += 1
    if i[2] and i[13]:
        search_number += 1
print('Процент проспавших: ' + str(round(search_number / general_number * 100, 1)) + '%')