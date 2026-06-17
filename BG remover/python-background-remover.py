from rembg import remover
from PIL import image
import io

input_path = "input.jpg"
output_path = "output.jpg"

def remove_background(input_path, output_path):
    with open(input_path, "rb") as f:
        input_data = f.read()

    output_data = remove(input_data)

    with open(output_path, "wb") as f:
        f.write(output_data)

remove_background("input.jpg", "output.png")