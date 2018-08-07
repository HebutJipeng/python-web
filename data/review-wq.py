file = open('review-wq.test(1).QandP', 'r', encoding="utf-8")
lines = file.readlines()

def fun(str1, str2):
    a = str2.split('_')
    aa = []
    aaa = []
    for item in a:
        if item == '':
            aa.append(str1)
            continue
        tem = str1.split(item)
        if tem[0] != '':
            aa.append(tem[0])
        if len(tem) != 1:
            str1 = tem[1]

    for i in aa:
        j = i.split(' ')
        for idx, jj in enumerate(j):
            if idx == 0:
                aaa.append({
                    'value': jj,
                    'height': 'B'
                })
            else:
                aaa.append({
                    'value': jj,
                    'height': 'O'
                })
    return aaa

for line in lines:
    line = line.split('\n')[0]
    sen = line.split('\t')
    bb = fun(sen[1], sen[0])
    print(bb)



