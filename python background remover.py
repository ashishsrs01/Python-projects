from rembg import remover
from PIL import Image
input_path = 'input_image.png'

def remove_background(input_path):
    open_image = Image.open(input_path)
    output_image = remover(open_image)
    output_image.save('output_image.png')
    return 'Background removed and saved as output_image.png'

if __name__ == "__main__":
    result = remove_background(input_path)
    print(result)

