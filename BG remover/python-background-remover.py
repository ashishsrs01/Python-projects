# background_remove_simple.py

from rembg import remove, new_session
from PIL import Image
import io
import numpy as np
import cv2

# Create the model once
session = new_session("isnet-general-use")

def remove_background(input_path, output_path):
    # Open image
    image = Image.open(input_path).convert("RGBA")

    # Convert image to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="PNG")
    input_data = img_bytes.getvalue()

    # Remove background
    output_data = remove(
        input_data,
        session=session,
        alpha_matting=True,
        alpha_matting_foreground_threshold=240,
        alpha_matting_background_threshold=10,
        alpha_matting_erode_size=10
    )

    # Open output image
    output_image = Image.open(io.BytesIO(output_data)).convert("RGBA")

    # Simple cleanup of the alpha channel
    data = np.array(output_image)
    rgb = data[:, :, :3]
    alpha = data[:, :, 3]

    # Remove small noise
    kernel = np.ones((5, 5), np.uint8)
    alpha = cv2.morphologyEx(alpha, cv2.MORPH_OPEN, kernel)
    alpha = cv2.morphologyEx(alpha, cv2.MORPH_CLOSE, kernel)

    # Add cleaned alpha back
    result = np.dstack((rgb, alpha))
    final_image = Image.fromarray(result, "RGBA")

    # Save output
    final_image.save(output_path)

    print("Background removed and saved to", output_path)


# Run the function
remove_background("input.jpg", "output.png")