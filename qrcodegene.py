import qrcode
from PIL import Image
import csv
import random
from qrcode.image.styledpil import StyledPilImage

with open('./datafile/namelist.csv') as f:
    #ファイル読み込み
    reader = csv.reader(f)
    i=1
    for row in reader:
        #rowを文字列に変換
        a=str(row)
        #a=['〇〇']の文字列のため先頭と末尾を削除
        a=a.removeprefix("['")
        a=a.removesuffix("']")
        #qrコード設定
        qr = qrcode.QRCode(
            version=1,
            box_size=6,
            border=4,
        )
        qr.add_data(a)
        #色乱数
        color = str(["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])])
        color=color.removeprefix("['")
        color=color.removesuffix("']")
        #qrコード生成
        img = qr.make_image(fill_color=f"{color}", back_color="white")
        #qrコードの保存
        img.save(f"./qrfile/qrcode{i}.png")
        #変数の更新
        i+=1


        



