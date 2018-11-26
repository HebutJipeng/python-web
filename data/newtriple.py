FILE_NAME = './newtriple'

f = open(FILE_NAME + '.txt', 'r', encoding="utf-8")
f1 = open(FILE_NAME + '_desc.csv', 'w', encoding="utf-8")
f2 = open(FILE_NAME + '_node.csv', 'w', encoding="utf-8")

lines = f.readlines()


def description(line):
    f1.write(line)


def node(line):
    par = line.strip().split('\t')
    part_line = par[0] + ',' + par[1] + ',' + par[2] + '\n'
    f2.write(part_line)


for line in lines:
    pa = line.split('\t')
    if pa[0].startswith(('m.', 'g.')) and pa[2].startswith(('m.', 'g.')):
        node(line)
    else:
        description(line)
print('done')


