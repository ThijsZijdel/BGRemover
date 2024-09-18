#!/usr/bin/env python

import sys
from rembg import remove
from PIL import Image
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: remove_bg.py <image_file>")
        sys.exit(1)
    input_path = sys.argv[1]

    if not os.path.exists(input_path):
        print(f"File {input_path} does not exist.")
        sys.exit(1)

    file_name = os.path.basename(input_path)
    output_path = os.path.join(os.path.dirname(input_path),f"{os.path.splitext(file_name)[0]}.trans.png")

    if os.path.exists(output_path):
        print(f"File {output_path} already exists.")
        sys.exit(1)

    try:
        with Image.open(input_path) as input_image:
            output_image = remove(input_image)
            output_image.save(output_path)
        print(f"Background removed from {input_path}.")
    except Exception as e:
        print(f"Error processing image: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()