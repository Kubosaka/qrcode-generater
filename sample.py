import qrcode
from PIL import Image

img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("./qrfile/some_file.png")
