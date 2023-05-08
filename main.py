import os
from PIL import Image

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the input and output directories
input_dir = os.path.join(script_dir, 'png')
output_dir = os.path.join(script_dir, 'webp')

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop over the input directory and convert all PNG files to WebP
for filename in os.listdir(input_dir):
    if filename.endswith('.png'):
        # Open the image
        with Image.open(os.path.join(input_dir, filename)) as im:
            # Construct the output filename
            output_filename = os.path.splitext(filename)[0] + '.webp'
            # Save the image in WebP format
            im.save(os.path.join(output_dir, output_filename), 'webp')
