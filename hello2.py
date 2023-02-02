import csv
import pandas as pd
import qrcode
from PIL import Image
import csv

df = pd.read_csv('datafile/namelist.csv',header=None)
i=1
for row in df.iteritems():
    print(row)
    img = qrcode.make(row)
    img.save(f"./qrfile/some_file{i}.png")
    i+=1
