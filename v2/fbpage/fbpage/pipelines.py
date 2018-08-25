# -*- coding: utf-8 -*-
import json
import codecs


class FbpagePipeline(object):
  def __init__(self):
    self.file = codecs.open('fbpage.json', 'a', encoding='utf-8')

  def process_item(self, item, spider):
    line = json.dumps(dict(item), ensure_ascii=False) + '\n'
    self.file.write(line)
    return item