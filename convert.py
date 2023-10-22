from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import pathlib
import os
import argparse

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError,
)


def main():
    # use argparse to get input & output paths
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str)

    args = parser.parse_args()

    # loop through files with glob */**.pdf ...find syntax

    # impliment error handling
    temp_folder = "img/temp/"

    if args.input:
        images = convert_from_path(
            args.input,
            output_folder=temp_folder,
        )

        infile_name = args.input.split("/")
        outfile_name = infile_name[-1].split(".")[0]

        # options:
        # convert_from_path(pdf_path, dpi=200, output_folder=None, first_page=None, last_page=None, fmt='ppm', jpegopt=None, thread_count=1, userpw=None, use_cropbox=False, strict=False, transparent=False, single_file=False, output_file=str(uuid.uuid4()), poppler_path=None, grayscale=False, size=None, paths_only=False, use_pdftocairo=False, timeout=600, hide_attributes=False)

        # IS THIS BETTER?

        # with tempfile.TemporaryDirectory() as path:
        #     images_from_path = convert_from_path(args.input, output_folder=path)
        #     # Do something here

        ocrfile = pathlib.Path(f"./ocr/{outfile_name}.txt")

        # create progress bar with richtext library

        print("There are", len(images), "pages.")

        # this will be the inner loop for each pdf in the folder
        for index, image in enumerate(images):
            print(f"Extracting text from page {index+1}...")
            text = pytesseract.image_to_string(image)  # time consuming part

            with open(ocrfile, "a") as outfile:
                outfile.write(text)
                outfile.write(f"\n END PAGE {index+1}\n")  # do i need this?
                print(f"Page {index+1} appended to file.")

        print(f"deleting temporary files from {temp_folder}...")
        for file in os.listdir(temp_folder):
            if os.path.isfile(f"{temp_folder}/{file}"):
                os.remove(f"{temp_folder}/{file}")

        print("Conversion complete :)")

        # create loop for files in folder that are already images not pdfs

        # uninstall opencv-python and remove from requirements.txt? didn't seem to need it.


if __name__ == "__main__":
    main()
