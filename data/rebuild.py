import re

ff= open('./ssset.csv', 'w', encoding="utf-8")
with open('./sset.csv', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    ff.write('id:ID(Node),name\n')
    for line in lines:
        a = re.escape(line.split(',')[0].replace('\n', ''))
        ff.write(a + ',' + a + '\n')
        
# ../bin/neo4j-import --into graph.db --nodes ssset.csv --relationships D: / home / bonc/neo4j/relathionship_uuid_10w.csv - -trim-strings true - -input-encoding UTF-8 - -id-type String - -stacktrace true - -bad-tolerance 10000 - -skip-bad-relationships true - -skip-duplicate-nodes true
# ../bin/neo4j-import --multiline-fields=true --bad-tolerance=1000000 --into graph.db --id-type string --nodes:Node ssset.csv   --relationships:related relation_header.csv,dottriple.csv

