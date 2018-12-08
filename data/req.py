import requests
import json


header2 = {
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate'
   }
r = requests.post('http://192.168.0.115:5002/webfreebase', data=json.dumps({
    'sparql': "PREFIX ns:<http://rdf.freebase.com/ns/> select distinct ?x where { ns:m.05zjh7s ns:people.deceased_person.date_of_death ?x . }"
}), headers=header2)
print(r)
