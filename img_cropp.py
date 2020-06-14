from PIL import Image

left = int(input("From left: "))
right = int(input("From right: "))
up = int(input("From up: "))
down = int(input("From down: "))
img_path = str(input("Your path: "))

open_img = Image.open(img_path)
cropped_img= open_img.crop((left,up,right,down))

cropped_img.save('r1')
