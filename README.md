# QR Code Generator with Logo Support

This is a Python-based GUI application to generate QR codes with optional logo support, using `qrcode`, `PIL`, `Tkinter`, and more. It allows users to enter a URL or text, generate a QR code, and optionally insert a logo in the center of the QR code. The generated QR code can be saved in PNG, SVG, or PDF format.

## Features
- Generate a QR code from a given URL or text.
- Add an optional logo to the QR code.
- Save the QR code in PNG, SVG, or PDF format.
- Interactive GUI built using Tkinter.

## How to Install

### Prerequisites
1. **Python 3.6+** is required.
2. Install the following libraries using `pip`:
  *pip install qrcode[pil] Pillow tkinter reportlab svglib*
Warning: For some device, Tkinter may already be installed, so you can remove tkinter from command.

**How to Run**
- Download the project files.
- Ensure you have installed all required libraries.
- Detect file location (with cd)
- Run the script using the following command:
    *python QRCode_generator.py*

**How it Works**

1. Input Field: Users can enter a text or URL in the input field to generate a QR code. The application checks if the input field is not empty before proceeding.

2. Generate QR Code: Once the user clicks the "Generate QR Code" button, the app creates a QR code from the provided text or URL:

  - The QR code is generated with a version size, box size, and border width predefined in the code.
  - The QR code is displayed as an image on the GUI.
3. Upload Logo: Optionally, users can upload a logo to place at the center of the QR code. Here’s how it works:

  - The logo is resized to fit within the QR code.
  - The app creates a circular white background behind the logo for a cleaner look.
  - The logo is then placed at the center of the QR code with proper alignment.
4. Save QR Code: The user can save the QR code in one of the following formats:

  - PNG: The QR code is saved as a PNG image file.
  - SVG: The QR code is converted to an SVG vector image format.
  - PDF: The QR code is saved as a PDF file using ReportLab, which embeds the image into a PDF document.
  - The user can select the file type when saving the QR code through a file dialog.
