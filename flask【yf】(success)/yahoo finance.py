from flask import Flask, render_template

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

app = Flask(__name__)

import matplotlib.pyplot as plt

from pandas_datareader.data import DataReader #モジュールが変わったため変更
from datetime import datetime

end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)
toyota = DataReader('TM', 'yahoo', start, end)


print(toyota.tail())

dfs=toyota.tail()

header=pd.DataFrame(dfs)
record = header.values.tolist()

@app.route('/')
def index():
  return render_template('index.html', header=header, record=record)

if __name__ == '__main__':
  app.run()

