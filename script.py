import os
import pytesseract
from PIL import Image

""" Reads text from our image! """
def read_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

""" Writes text to file! """
def write_text_to_file(text, file_path):
    with open(file_path, 'a') as file:
        file.write(text + '\n')

def main(image_folder, output_text_file):
    for filename in os.listdir(image_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_folder, filename)
            text = read_text_from_image(image_path)
            write_text_to_file(text, output_text_file)

if __name__ == '__main__':
    image_folder = './images'
    output_text_file = 'output_text.txt'

    main(image_folder, output_text_file)
