import re

ff = open('./dottt.csv', 'w', encoding="utf-8")
with open('./dot.csv', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        a = line.split(',')
        print(re.escape(a[0]))

