from collections import Counter
from random import randint

lst = [randint(1,10) for i in range(10)]
print(lst)

count_lst = Counter(lst)
print(count_lst)