import requests
import ssl
ssl.match_hostname = lambda cert, hostname: True
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import csv

url = r'https://cms.keepkeep.com/admin/musics'

headers = { 'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1YWQ5NWNmZjc4ZGRhNTMxMDU2M2RhN2UiLCJ1c2VybmFtZSI6IlBlbmdfSGkiLCJhdmF0YXIiOiJodHRwczovL3N0YXRpYzEua2VlcGNkbnMuY29tL2F2YXRhci8yMDE4LzA0LzIwLzExLzZlMmZkZjE0MjA3ZTYxNjFlY2VmZTM3YTIwYzU3ODI2MjA5MWM5Y2MuanBnIiwibG9naW5UeXBlIjoiZW1haWwiLCJnZW5kZXIiOiJNIiwiaXNzIjoiaHR0cDovL3d3dy5nb3Rva2VlcC5jb20vIiwiZXhwIjoxNTI5MDQ4NzY3LCJpYXQiOjE1MjY0NTY3Njd9.b6rCa5eG2n1CXQg_s503LF8feVu3Rwmp9DoAUsna-xg',
  'Connection': 'keep-alive',
  'Cookie': 'authorization=Bearer%20eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1YWQ5NWNmZjc4ZGRhNTMxMDU2M2RhN2UiLCJ1c2VybmFtZSI6IlBlbmdfSGkiLCJhdmF0YXIiOiJodHRwczovL3N0YXRpYzEua2VlcGNkbnMuY29tL2F2YXRhci8yMDE4LzA0LzIwLzExLzZlMmZkZjE0MjA3ZTYxNjFlY2VmZTM3YTIwYzU3ODI2MjA5MWM5Y2MuanBnIiwibG9naW5UeXBlIjoiZW1haWwiLCJnZW5kZXIiOiJNIiwiaXNzIjoiaHR0cDovL3d3dy5nb3Rva2VlcC5jb20vIiwiZXhwIjoxNTMwNDE5MTg3LCJpYXQiOjE1Mjc4MjcxODd9.o1ZGs0X5D7iMFEWkoIPeuLMHZDFSRjLuzXewTklSCyQ; cms:session=eyJsZGFwVXNlcm5hbWUiOiJqaXBlbmciLCJwYXNzd29yZCI6IiIsIl9leHBpcmUiOjE1Mzc0MjMzOTg2MzAsIl9tYXhBZ2UiOjg2NDAwMDAwMDB9; cms:session.sig=OU4H2XKpH1byq2hPIhBk0zMZ1Hc; _ga=GA1.2.421585138.1530245172; x-request-id=0c81d8fea93b5f3d1377dd14856190ac; ldapUsername=jipeng; ldapUsername.sig=DJmre-4yb96uuqRoJWIFRr-6-vA',
  'Host': 'cms.keepkeep.com',
  'Referer': 'https://cms.keepkeep.com/music/list',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
  'x-lcid': 'en-US' }

s = requests.Session()
s.headers.update(headers)

with open('Training Music - Premium Music Playlist.csv', encoding='utf-8') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)

    for row in f_csv:
        temp_dict = {}
        temp_dict['name'] = row[1]
        temp_dict['author'] = row[3]
        temp_dict['hash'] = row[8]
        temp_dict['size'] = row[6]
        temp_dict['url'] = row[12]
        print(temp_dict)

        r = requests.post(url, json=temp_dict,  verify=False)
        print(r.text)