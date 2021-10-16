#!/usr/bin/python
# -*- coding: utf-8 -*-
# Если необходимо выполнить файл
import json
from pprint import pprint

with open('two.json', 'r') as f:         # Для выполнения другого файла - меняем название файла на необходимый.
    task = json.load(f)
    pprint(task)

