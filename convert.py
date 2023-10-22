from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import pathlib

print(pytesseract.image_to_string(Image.open("./img/intro-paragraph.png")))

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError,
)

# use argparse to get input & output paths
# loop through files with glob */**.pdf ...find syntax

# impliment error handling
images = convert_from_path(
    "./pdfs/03-seaweed-and-algae-survey-reports-june-sept-1978.pdf",
    output_folder="img/macrophyte-algae-report-1978/",
)
# options:
# convert_from_path(pdf_path, dpi=200, output_folder=None, first_page=None, last_page=None, fmt='ppm', jpegopt=None, thread_count=1, userpw=None, use_cropbox=False, strict=False, transparent=False, single_file=False, output_file=str(uuid.uuid4()), poppler_path=None, grayscale=False, size=None, paths_only=False, use_pdftocairo=False, timeout=600, hide_attributes=False)

# IS THIS BETTER?
# import tempfile
# with tempfile.TemporaryDirectory() as path:
#     images_from_path = convert_from_path('./pdfs/03-seaweed-and-algae-survey-reports-june-sept-1978.pdf', output_folder=path)
#     # Do something here

ocrfile = pathlib.Path("./ocr/macrophyte-algae-report-1978.txt")

# create progress bar with richtext library

print("There are", len(images), "pages.")

# this will be the inner loop for each pdf in the folder
for index, image in enumerate(images):
    # outpath = pathlib.Path(
    #     f'./img/macrophyte-algae-report-1978/image{index}.jpg')
    # image.save(outpath, 'JPEG')
    # print(f'Saved image to {outpath}.')

    print(f"Extracting text from page {index+1}...")
    text = pytesseract.image_to_string(image)  # time consuming part

    with open(ocrfile, "a") as outfile:
        outfile.write(text)
        outfile.write(f"\n END PAGE {index+1}\n")  # do i need this?
        print(f"Page {index+1} appended to file.")

print("Conversion complete :)")

# create loop for files in folder that are already images not pdfs

# uninstall opencv-python and remove from requirements.txt? didn't seem to need it.
