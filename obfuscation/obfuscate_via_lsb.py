from bitstring import BitArray
from PIL import Image

LSB_PAYLOAD_LENGTH_BITS = 32

def obfuscate_via_lsb(data, input_file, output_file):
    data = BitArray(uint=len(data) * 8, length=LSB_PAYLOAD_LENGTH_BITS).bin + BitArray(bytes=data.encode()).bin

    i = 0
    try:
        with Image.open(input_file) as img:
            width, height = img.size
            if len(data) > width * height * 3:
                print("Data is too large to be embedded in the image. Data contains {} bytes, maximum is {}".format(
                    int(len(data) / 8), int(width * height * 3 / 8)))
                exit(1)
            for x in range(0, width):
                for y in range(0, height):
                    pixel = list(img.getpixel((x, y)))
                    for n in range(0, 3):
                        if i < len(data):
                            pixel[n] = pixel[n] & ~1 | int(data[i])
                            i += 1
                    img.putpixel((x, y), tuple(pixel))
                    if i >= len(data):
                        break
                if i >= len(data):
                    break
            img.save(output_file, "png")
    except IOError:
        print("Could not open {}. Check that the file exists and it is a valid image file.".format(input_file))
        exit(1)
    print("Data written to {}".format(output_file))

image_path = "netflix.jpg" 
image = Image.open(image_path)
largeur, hauteur = image.size
taille = (largeur * hauteur) / 8
text = 'Hello World for ever'
lenght_text = len(text)
image_return = "disney.jpeg"
if lenght_text >= taille:
    print("Le message est trop long")
else:
    obfuscate_via_lsb(text,image_path,image_return)