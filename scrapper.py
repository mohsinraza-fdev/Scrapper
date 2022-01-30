from bs4 import BeautifulSoup
import requests
from flask import Flask
app = Flask(__name__)
import re


@app.route('/')
def indexx():
    url = "https://www.ziauddinhospital.com/for-patients/find-a-doctor/"
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")

    table = doc.tbody
    contents = table.contents
    count = 0
    l2 = []
    for tr in contents:
        count += 1
        l = []
        for i in tr:
            x = re.findall('<td>(.*?)<', str(i))
            l.append(x)
        if len(l) > 1:
            l2.append({'Name': l[3][0], 'Occupation': l[1][0], 'Timing': l[9][0]})
        if count > 6:
            break
    return {'Data': l2}

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')