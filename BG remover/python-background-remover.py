# python-background-remover.py

from rembg import remove, new_session
from PIL import Image
import numpy as np

# ----------------------------------------------------
# Model Sessions
# We load the models once so that processing images is fast.
# ----------------------------------------------------
# 1. Specialized model for cartoon/anime illustrations
anime_session = new_session("isnet-anime")

# 2. Segment Anything Model (SAM) for highly accurate photo segmentation
sam_session = new_session("sam")


# ----------------------------------------------------
# Image Classification ("Thinking" Function)
# This function decides if the image is a cartoon/anime or a real photo.
# ----------------------------------------------------
def detect_image_type(img):
    # Resize the image to a small 200x200 size to make the calculation fast
    small_img = img.resize((200, 200))
    
    # Convert pixels into a flat list of RGB colors using numpy
    pixels = np.array(small_img).reshape(-1, 3)
    
    # Count the number of unique colors in the image
    unique_colors = len(np.unique(pixels, axis=0))
    print(f"Detected {unique_colors} unique colors in a 200x200 sample.")
    
    # Cartoon/anime images have flat shading and few unique colors.
    # Real-world photos have camera noise, shadows, and thousands of unique colors.
    # Out of 40,000 pixels (200x200), if there are fewer than 6,000 unique colors, it's anime!
    if unique_colors < 6000:
        return "anime"
    else:
        return "photo"


# ----------------------------------------------------
# Smart Background Remover
# This function analyzes the image first, then uses the best model.
# ----------------------------------------------------
def remove_background_smart(input_path, output_path):
    # Open the image using PIL
    img = Image.open(input_path).convert("RGBA")
    
    # Analyze the image type first
    image_type = detect_image_type(img)
    print(f"Image type classified as: {image_type.upper()}")
    
    if image_type == "anime":
        # For anime/cartoons, we use the specialized anime model
        print("Using the specialized 'isnet-anime' model...")
        output_img = remove(img, session=anime_session)
    else:
        # For real photos, we use the highly accurate SAM model
        print("Using the high-accuracy 'SAM' model...")
        width, height = img.size
        
        # We tell SAM to look at the center of the image
        # Note: input_points needs to be in [y, x] coordinate order
        input_points = np.array([[height // 2, width // 2]])
        input_labels = np.array([1])  # 1 means "this is the object we want to keep"
        
        output_img = remove(
            img,
            session=sam_session,
            input_points=input_points,
            input_labels=input_labels
        )
        
    # Save the output image
    output_img.save(output_path)
    print(f"Background removed successfully and saved to: {output_path}")


# ----------------------------------------------------
# Example Usage
# ----------------------------------------------------
if __name__ == "__main__":
    # Remove background automatically based on image classification
    # Make sure you have an "input.jpg" in the same folder.
    remove_background_smart("input.jpg", "output.png")