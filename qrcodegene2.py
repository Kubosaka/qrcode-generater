import qrcode
from PIL import Image
import csv
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
        #qrコード生成
        qr = qrcode.QRCode(
            version=1,
            box_size=6,
            border=4,
        )
        qr.add_data(a)
        img = qr.make_image(image_factory=StyledPilImage,embeded_image_path="./datafile/NUTMEG.jpeg")
        #文字列を'/'で分割
        a=a.split('/')
        #qrコードの保存
        img.save(f"./qrfile2/{a[-1]}.png")
        #変数の更新
        i+=1
        