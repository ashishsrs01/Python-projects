from rembg import remover
from PIL import image
import io

input_path = "input.jpg"
output_path = "output.jpg"

session = new_session("isnet-general-use")

def remove_background(input_path, output_path):
    with open(input_path, "rb") as f:
        input_data = f.read()

    output_data = remove(
        input_data,
        session=session,
        alpha_matting=True,
        alpha_matting_foreground_threshold=240,
        alpha_matting_background_threshold=10,
        alpha_matting_erode_size=10
    )

    with open(output_path, "wb") as f:
        f.write(output_data)

remove_background("input.jpg", "output.png")