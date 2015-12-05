"""
convert images to ascii art
"""
__author__ = 'adillon'

from PIL import Image, ImageFont, ImageDraw, ImageStat, ImageOps, ImageChops
import multiprocessing as mp
from time import time


class Font:
    """
    Information about how to map a character to an image of said character
    """

    def __init__(self, name, pt, contrast=1.0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = name
        self._pt = pt
        self._font = ImageFont.truetype(self._name, size=self._pt)
        self._size = self._font.getsize("_")
        raw_images = {}
        self._images = {1.0: raw_images}
        self._avg_values = {}
        for i in range(32, 127):
            c = chr(i)
            image = Image.new("L", self._size)
            draw = ImageDraw.Draw(image)
            for j in range(3):
                draw.text((0, 0), c, font=self._font, fill=1.0)
            raw_images[c] = image
            self._avg_values[c] = ImageStat.Stat(image).mean[0]
        self._max_value = max(self._avg_values.values())
        self._contrast = contrast
        self.contrast = contrast

    @property
    def width(self):
        return self._size[0]

    @property
    def height(self):
        return self._size[1]

    @property
    def contrast(self):
        return self._contrast

    @contrast.setter
    def contrast(self, val):
        if val > 1.0 or val < 0 or not isinstance(val, (float, int)):
            raise ValueError("contrast must be a number in the range 0-1, "
                             "got %s instead" % val)
        self._contrast = val
        if val not in self._images:
            images = {}
            self._images[val] = images
            for c, image in self._images[1.0].items():
                avg = self._avg_values[c] * (255.0 / self._max_value)
                blk = (1 - val) * avg
                wit = 255 - (1 - val) * (255-avg)
                new_img = ImageOps.colorize(image.copy(), [blk]*3, [wit]*3)
                images[c] = ImageOps.grayscale(new_img)

    def match(self, patch):
        diffs = {}
        for c, im in self._images[self._contrast].items():
            diff_im = ImageChops.difference(patch, im)
            diffs[c] = ImageStat.Stat(diff_im).mean[0]
        return min(diffs, key=diffs.get)


class Converter:
    def __init__(self,
                 font,
                 size=None,
                 contrast=0.85,
                 auto_contrast=True,
                 equalize=False,
                 invert=False):
        self._font = font
        self.size = size
        self.contrast = contrast
        self.auto_contrast = auto_contrast
        self.equalize = equalize
        self.invert = invert

    @property
    def contrast(self):
        return self._font.contrast

    @contrast.setter
    def contrast(self, val):
        self._font.contrast = val

    def convert(self, image):
        image = self.prep(image)
        image_width, image_height = image.size
        workers = mp.Pool(initializer=worker_init, initargs=(self._font, image))
        rows = []
        for y in range(0, image_height, self._font.height):
            row = [(x, y, x+self._font.width, y+self._font.height)
                   for x in range(0, image_width, self._font.width)]
            rows.append(row)
        yield from workers.imap(match, rows)

    def prep(self, image):
        image = image.convert('L')
        if self.size:
            image = ImageOps.fit(image, self.size, method=Image.BICUBIC)
        if self.auto_contrast:
            image = ImageOps.autocontrast(image)
        if self.equalize:
            image = ImageOps.equalize(image)
        if self.invert:
            image = ImageOps.invert(image)
        return image


FONT = None
IMAGE = None
def worker_init(font, image):
    global FONT
    global IMAGE
    FONT = font
    IMAGE = image

def match(row):
    return "".join(FONT.match(IMAGE.crop(box)) for box in row)

# The following will eventually be replaced by a GUI
import argparse
import os
import ast

parser = argparse.ArgumentParser()

parser.add_argument("input")
parser.add_argument("-c", "--contrast",
                    type=float,
                    help=("the contrast ration of the font as a percentage."
                          "High contrast implies more emphasis on the shape of"
                          "characters, while low contrast implies higher"
                          "emphasis on the brightness of characters"),
                    default=0.85)
parser.add_argument("-f", "--font",
                    default="Andale Mono")
parser.add_argument("-p", "--pt",
                    help="the point size of the desired font",
                    type=int,
                    default=14)
parser.add_argument("-s", "--size",
                    help=("the desired size (in pixels) of the result as a "
                          "tuple of '(width, height)'."))

parser.add_argument("-o", "--output_path",
                    help=("optional path where you want the result saved"
                          "(defaults to a .txt file at the same location"
                          "as the input path)"))

def main(converter, image_path, output_path=None):
    image = Image.open(image_path)
    start = time()
    results = []
    for row in converter.convert(image):
        print(row)
        results.append(row)
    result = "\n".join(results)
    print("finished in %s seconds" % (time()-start))
    output_path = output_path or os.path.splitext(image_path)[0] + ".txt"
    with open(output_path, 'w') as f:
        f.write(result)


if __name__ == "__main__":
    args = parser.parse_args()
    font = Font(args.font, args.pt, args.contrast)
    converter = Converter(font, contrast=args.contrast)
    if args.size:
        converter.size = ast.literal_eval(args.size)
    main(converter, args.input, args.output_path)
