import os

for root, dirs, files in os.walk('../8-3'):
 for file in files:
  open_file = open(file, 'r', encoding='utf-8')
  lines = open_file.readlines()
  max_length = 0
  for line in lines:
   l_l = len(line.split(' '))
   max_length = l_l > max_length and l_l or max_length

  print(file, ' max-length: ', max_length)

