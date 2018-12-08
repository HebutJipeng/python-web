import json
import demjson

with open('./WebQSP.test.json', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())
    print(data)

