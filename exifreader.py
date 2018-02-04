import os
from PIL import Image
from PIL.ExifTags import TAGS,GPSTAGS
path = os.path.dirname('/Users/baraka62/pictures')
imgpath = '/Users/baraka62/pictures/20160102_223353.jpg'
image=Image.open(imgpath)
image.load()
exifinfo=image._getexif()
#image.show()
if image._getexif():
    for tag, value in exifinfo.items():
        decoded = TAGS.get(tag, tag)
        if decoded == 'Orientation':
            print('%s = %s' % (decoded, value))
            break
else:
    print("no exif")
    image.show()

