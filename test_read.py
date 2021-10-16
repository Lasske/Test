# Если необходимо прочесть файл
from pprint import pprint

with open('one.json') as f:       # Для прочтения другого файла - меняем название файла на необходимый.
    f = f.read()
pprint(f)
