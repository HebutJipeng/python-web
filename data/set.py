import os

for root, dirs, files in os.walk('./triple'):
    myset = set()
    for file in files:
        f = open('./triple/' + file, 'r', encoding='utf-8')
        lines = f.readlines()
        for line in lines:
            tmp = line.strip().split('\t')
            if tmp[0].startswith(('m', 'g')):
                myset.add(tmp[0])
            if tmp[2].startswith(('m', 'g')):
                myset.add(tmp[2])
        print(file + 'done')
    with open('./set.csv', 'w', encoding="utf-8") as fw:
        fw.write('id,object\n')
        for idx, s in enumerate(myset):
            fw.write(str(idx) + ',' + s+'\n')
        print('done')

