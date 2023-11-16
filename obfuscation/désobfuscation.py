from bitstring import BitArray
from PIL import Image

def extract_text_via_lsb(input_file):
    extracted_bits = ""
    try:
        with Image.open(input_file) as img:
            width, height = img.size

            for x in range(0, width):
                for y in range(0, height):
                    pixel = img.getpixel((x, y))
                    for n in range(0, 3):
                        extracted_bits += str(pixel[n] & 1)
    except IOError:
        print("Could not open {}. Check that the file exists and it is a valid image file.".format(input_file))
        exit(1)
    return extracted_bits

hidden_text_bits = extract_text_via_lsb('disney.jpeg')

hidden_text = BitArray(bin=hidden_text_bits).bytes.decode(errors='replace')

print("Hidden Text: {}", hidden_text)