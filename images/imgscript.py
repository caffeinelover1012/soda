import os
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from PIL.Image import Transpose

# define input and output folders
input_folder = "input"
output_folder = "output"

# define watermark parameters
watermark_text = "SK Shirts"
watermark_font = ImageFont.truetype(font="Chunk Five Print.otf",size=30)
watermark_position = (300,650) 

# check if output folder exists, if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
i=0
# loop through all files in the input folder
for filename in os.listdir(input_folder):
    # check if file is an image
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # open image and flip it horizontally
        with Image.open(os.path.join(input_folder, filename)) as img:
            img = img.transpose(Transpose.FLIP_LEFT_RIGHT)

            # increase brightness by 10%
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(1.1)

            # add watermark
            draw = ImageDraw.Draw(img)
            draw.text(watermark_position, watermark_text,fill="Black" ,font=watermark_font)

            i+=1
            # convert to png
            img = img.convert("RGBA")
            png_filename = f"output{i}.png"
            output_path = os.path.join(output_folder, png_filename)
            img.save(output_path, "PNG")
