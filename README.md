# Image To PDF Converter

This is a simple Python script that converts a collection of images into a single PDF file.

## Features

- Select multiple images to convert into a PDF.
- Choose various sizing options for images in the PDF:
  - Fit: Fit images to fill the entire page.
  - A4 Size: Standard A4 size for each image.
  - Contain: Fit images proportionally inside the page.
  - Custom Size: Set custom width and height for images.
  - Letter Size: Standard letter size (8.5 x 11 inches).
  - Legal Size: Standard legal size (8.5 x 14 inches).
  - Square: Resize images to be square-shaped.
  - Thumbnail: Resize images to thumbnail size.
- Centralized alignment for all images in the PDF.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/image-to-pdf-converter.git
    ```

2. Navigate to the directory:

    ```bash
    cd image-to-pdf-converter
    ```

3. Install the required dependencies:

    ```bash
    pip install fpdf
    ```

4. Run the script:

    ```bash
    python main.py
    ```

5. Select images from the file dialog.
6. Enter the output PDF name.
7. Choose the desired sizing option.
8. Click "Convert to PDF" button.
9. Find the generated PDF file in the same directory.

## Requirements

- Python 3.x
- tkinter library (usually included in Python installations)
- fpdf library
