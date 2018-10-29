curl https://api.crowdin.com/api/project/keep-intl/export?key=ccf379c4ab7ee668d2fac3b8858f7581
curl https://api.crowdin.com/api/project/keep-intl/download/all.zip?key=ccf379c4ab7ee668d2fac3b8858f7581 > strings.zip
rm -rf ./finalfile
mkdir strings
unzip strings.zip -d strings
python3 build.py
rm strings.zip
rm -rf ./strings