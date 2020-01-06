from flask import Flask, render_template

import pandas as pd

app = Flask(__name__)

url = 'https://info.finance.yahoo.co.jp/ranking/?kd=4'
dfs = pd.read_html(url)


print(dfs)

header=pd.DataFrame(dfs)
#print(type(header))
#print(header)

#dataframeに変更　2行目以下
record = header.values.tolist()

#print(record)
#print(type(record))


@app.route('/')
def index():
  return render_template('index.html', header=header, record=record)

if __name__ == '__main__':
  app.run()