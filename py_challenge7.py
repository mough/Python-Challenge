from PIL import Image

img = Image.open("oxygen_crop2.jpg")  # had to crop image down to only gray scale bar

#print(img.size)  # returns (608, 9)

pixels = []
y = 4
for x in range(3,608,7):
    pixels.append(img.getpixel((x, y)))

vals = [p[0] for p in pixels]

step2 = []
for x in vals:
    step2.append(chr(x))

step3 = "".join(chr(v) for v in vals)

step4 = [105, 110, 116, 101, 103, 114, 105, 116, 121]

final = []
for x in step4:
    final.append(chr(x))

print("".join([x for x in final]))