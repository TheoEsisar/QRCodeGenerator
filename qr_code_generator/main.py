import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from ttkthemes import ThemedTk
import qrcode
from PIL import Image, ImageTk
import os

class QRCodeGeneratorApp(ThemedTk):
    def __init__(self):
        super().__init__(theme="arc") # Choose a modern theme
        self.title("QR Code Generator")
        self.geometry("400x500")
        icon_path = os.path.abspath('qr_code_generator\\icon.ico')
        self.iconbitmap(icon_path)
        self.create_widgets()

    def create_widgets(self):
        self.entry = ttk.Entry(self, width=50)
        self.entry.pack(pady=10)

        self.generate_button = ttk.Button(self, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=10)

        self.qr_code_label = ttk.Label(self)
        self.qr_code_label.pack(pady=10)

    def generate_qr_code(self):
        text = self.entry.get()
        if text:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color=(245,246,247))
            img = ImageTk.PhotoImage(img)
            self.qr_code_label.config(image=img)
            self.qr_code_label.image = img # Keep a reference to the image
        else:
            messagebox.showwarning("Warning", "Please enter some text.")

if __name__ == "__main__":
    app = QRCodeGeneratorApp()
    app.mainloop()
