from PIL import Image
import os

def convert_to_webp(input_image_path, output_image_path=None):
    try:
        # Open the input image
        with Image.open(input_image_path) as img:
            # If output path is not provided, use the same name with a .webp extension
            if output_image_path is None:
                output_image_path = os.path.splitext(input_image_path)[0] + '.webp'
            
            # Convert and save the image as WebP
            img.save(output_image_path, 'WEBP')
            print(f"Image successfully converted to: {output_image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_image_path = "input_image.jpg"  # Change this to your input image file
output_image_path = "output_image.webp"  # Optional: Specify an output file path

convert_to_webp(input_image_path, output_image_path)