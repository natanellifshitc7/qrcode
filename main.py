import qrcode
x = input("Address\n")
k = input("Flour\n")

data="Address is ",x+", The flour is",str(k)
img = qrcode.make(data)
type(img)  # qrcode.image.pil.PilImage
img.save("test.png")