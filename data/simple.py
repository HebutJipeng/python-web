import json

with open('simple.train.dat', encoding='utf-8') as inf:
    file_name = 'simple.train'
    file_sen = open(file_name + '.question.txt', 'w', encoding='utf-8')
    file_spa = open(file_name + '.sparql.txt', 'w', encoding='utf-8')

    lines = inf.readlines()

    sparql = 'SELECT DISTINCT ?x WHERE { <e> **&&**  ?x}'

    for line in lines:
        json_line = json.loads(str(line))
        line_sentence = json_line['sentence'][0].replace('_', '<e>')

        path = json_line['paths'][0][0].split(' ')[1]
        line_sparql = sparql.replace('**&&**', path)

        file_sen.write(str(line_sentence) + '\n')
        file_spa.write(str(line_sparql) + '\n')

        print(json_line)
