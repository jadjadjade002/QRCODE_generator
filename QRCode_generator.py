import qrcode
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import os

# Function to generate the QR code 
def generate_qr(): 
    link = entry.get()
    
    if link:  # Check if the input field is not empty
        # Create QR code object
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(link)
        qr.make(fit=True)

        # Generate QR code image
        img = qr.make_image(fill='black', back_color='white').convert('RGBA')

        # If logo selected, add it to the QR code
        if logo_path:
            logo = Image.open(logo_path).convert('RGBA')
            
            # Resize logo to fit in the center of QR code
            logo_size = (35, 35)
            logo = logo.resize(logo_size)

            # Create a white circular background for the logo
            background_size = (40, 40)  # Make the circle slightly bigger than the logo
            circle = Image.new('RGBA', background_size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(circle)
            draw.ellipse((0, 0, background_size[0], background_size[1]), fill=(255, 255, 255, 255))
            
            # Add the circular background
            circle.paste(logo, ((background_size[0] - logo_size[0]) // 2, (background_size[1] - logo_size[1]) // 2), logo)
            
            # Calculate position to paste logo with the circular background in the center
            img_w, img_h = img.size
            pos = ((img_w - background_size[0]) // 2, (img_h - background_size[1]) // 2)
            img = img.convert("RGBA")
            img.paste(circle, pos, circle)

        # Display the generated QR code
        img_tk = ImageTk.PhotoImage(img.resize((200, 200)))
        qr_label.config(image=img_tk)
        qr_label.image = img_tk
        
        # Store the generated QR code in memory
        global qr_image
        qr_image = img
    else:
        qr_label.config(text="Please enter a valid Text/URL", fg="red")

# Function to save QR code as PNG
def save_qr():
    filetypes = [('PNG files', '*.png')]
    file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=filetypes)
    
    if file_path:
        qr_image.save(file_path, 'PNG')
        status_label.config(text=f"QR Code saved as PNG file successfully!")

# Function to add logo to QR code
def upload_logo():
    global logo_path
    logo_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.png;*.jpg;*.jpeg')])
    if logo_path:
        status_label.config(text="Logo uploaded successfully!", fg="green")
    else:
        status_label.config(text="No logo uploaded.", fg="red")

# Main GUI
root = Tk()
root.title("QR Code Generator By Jadesadakorn")
root.geometry("500x570")

# Input URL
label1 = Label(root, text="Enter a Text/URL to generate a QR code:")
label1.pack(pady=10)
entry = Entry(root, width=40)  # Input field for link
entry.pack(pady=10)

generate_button = Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

qr_label = Label(root)
qr_label.pack(pady=10)

# Upload logo button
type_label = Label(root, text="Only file types: png, jpg, jpeg for logo")
type_label.pack(pady=10)

logo_path = ""
upload_logo_button = Button(root, text="Upload Logo (Optional)", command=upload_logo)
upload_logo_button.pack(pady=10)

save_button = Button(root, text="Save QR Code", command=save_qr)
save_button.pack(pady=10)

status_label = Label(root, text="", fg="green")
status_label.pack(pady=10)

root.mainloop()
