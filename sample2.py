import qrcode
from PIL import Image
import csv

with open('./datafile/namelist.csv') as f:
    reader = csv.reader(f)
    i=1
    for row in reader:
        print(row)
        img = qrcode.make(row)
        img.save(f"./qrfile/some_file{i}.png")
        i+=1
        



