from PIL import Image

image = Image.open('image.jpg')

# next 3 lines strip exif
data = list(image.getdata())
image_without_exif = Image.new(image.mode, image.size)
image_without_exif.putdata(data)

image_without_exif.save('image_file_without_exif.jpeg')