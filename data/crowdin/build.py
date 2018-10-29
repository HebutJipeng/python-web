import os
import json

LANGUAGES = [
    'de', 'es-ES', 'fr', 'hi', 'id', 'it', 'ja', 'ko', 'pt-BR', 'ru', 'th', 'zh-CN', 'zh-TW'
]

SOURCE_PATH = './strings/'
MAP_PATH = './outmap/'
FINAL_PATH = './finalfile/'

files = os.listdir(MAP_PATH)


def resolve(lang):
    url_path = SOURCE_PATH + lang + '/source.json'
    with open(url_path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        data_keys = data.keys()
        for item in files:
            current_file = item.split('.')[0]
            with open(MAP_PATH + item, 'r', encoding='utf-8') as ff:
                template = ff.read()
                for key in data_keys:
                    if (current_file in key):
                        template = template.replace('*#' + key + '#*', data[key])
                output(current_file, lang, json.loads(template))


def output(name, lang, template):
    path = FINAL_PATH + lang
    if not os.path.exists(path):
        os.makedirs(path)
    with open(FINAL_PATH + lang + '/' + name + '.json', 'w') as f:
        json.dump(template, f)


for lang in LANGUAGES:
    resolve(lang)

print('done!')





