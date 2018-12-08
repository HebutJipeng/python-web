import string

def find_string(s, t):
    try:
        return t in s
    except(ValueError):
        return False

with open('./final_webques.test.QandMidandSparql 1.txt', 'r', encoding='utf-8') as f:
    fisrt = open('./first.txt', 'w', encoding='utf-8')
    third = open('./third.txt', 'w', encoding='utf-8')
    lines = f.readlines()
    for idx, line in enumerate(lines):
        listL = line.split('\t')
        lf = find_string(listL[0], 'first')
        ls = find_string(listL[0], 'second')
        lm = find_string(listL[0], 'most')
        ll = find_string(listL[0], 'last')
        if lf or ls or lm or ll:
            print('第一列: ', idx+1)
            fisrt.write(str(idx+1) + '\t' + line)
        
        lo = find_string(listL[2], 'ORDER')
        if lo:
            print('第三列: ', idx+1)
            third.write(str(idx+1) + '\t' + line)
        # print(lf or ls or lm or ll)
