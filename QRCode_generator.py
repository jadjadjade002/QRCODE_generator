import qrcode
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import os

def generate_qr(): 
    link = entry.get()
    
    if link:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white').convert('RGBA')

        if logo_path:
            logo = Image.open(logo_path).convert('RGBA')
            
            logo_size = (35, 35)
            logo = logo.resize(logo_size)

            background_size = (40, 40)
            circle = Image.new('RGBA', background_size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(circle)
            draw.ellipse((0, 0, background_size[0], background_size[1]), fill=(255, 255, 255, 255))

            circle.paste(logo, ((background_size[0] - logo_size[0]) // 2, (background_size[1] - logo_size[1]) // 2), logo)

            img_w, img_h = img.size
            pos = ((img_w - background_size[0]) // 2, (img_h - background_size[1]) // 2)
            img = img.convert("RGBA")
            img.paste(circle, pos, circle)

        img_tk = ImageTk.PhotoImage(img.resize((200, 200)))
        qr_label.config(image=img_tk)
        qr_label.image = img_tk

        global qr_image
        qr_image = img
    else:
        qr_label.config(text="Please enter a valid Text/URL", fg="red")

def save_qr():
    filetypes = [('PNG files', '*.png')]
    file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=filetypes)
    
    if file_path:
        qr_image.save(file_path, 'PNG')
        status_label.config(text=f"QR Code saved as PNG file successfully!")

def upload_logo():
    global logo_path
    logo_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.png;*.jpg;*.jpeg')])
    if logo_path:
        status_label.config(text="Logo uploaded successfully!", fg="green")
    else:
        status_label.config(text="No logo uploaded.", fg="red")

root = Tk()
root.title("QR Code Generator By Jadesadakorn")
root.geometry("500x570")

label1 = Label(root, text="Enter a Text/URL to generate a QR code:")
label1.pack(pady=10)
entry = Entry(root, width=40)
entry.pack(pady=10)

generate_button = Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

qr_label = Label(root)
qr_label.pack(pady=10)

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
