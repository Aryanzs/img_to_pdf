import os
import tkinter as tk
from tkinter import filedialog
from fpdf import FPDF

class ImageToPdfConverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()
        self.selected_images_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.size_options = ["Fit", "A4 Size", "Contain", "Custom Size", "Letter Size", "Legal Size", "Square", "Thumbnail"]
        self.selected_size = tk.StringVar(value=self.size_options[0])  # Default to "Fit"
        self.custom_width = tk.DoubleVar()
        self.custom_height = tk.DoubleVar()
        
        self.initialize_ui()
    
    def initialize_ui(self):
        title_label = tk.Label(self.root, text="Image To Pdf Converter", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)
        
        select_images_button = tk.Button(self.root, text="Select Images", command=self.select_images)
        select_images_button.pack(pady=10)
        
        self.selected_images_listbox.pack(pady=(0,10), fill=tk.BOTH, expand=True)
        
        label = tk.Label(self.root, text="Enter Output Pdf Name: ")
        label.pack()
        
        pdf_name_entry = tk.Entry(self.root, textvariable=self.output_pdf_name, width=40, justify='center')
        pdf_name_entry.pack()
        
        # Dropdown box for size options
        size_label = tk.Label(self.root, text="Select Size Option: ")
        size_label.pack()
        size_dropdown = tk.OptionMenu(self.root, self.selected_size, *self.size_options)
        size_dropdown.pack()
        
        convert_button = tk.Button(self.root, text="Convert to PDF", command=self.convert_images_to_pdf)
        convert_button.pack(pady=(20,40))
        
    def select_images(self):
        self.image_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Images files", "*.png;*.jpg;*.jpeg")])
        self.update_selected_images_listbox()
        
    def update_selected_images_listbox(self):
        self.selected_images_listbox.delete(0, tk.END)
        for image_path in self.image_paths:
            _, image_name = os.path.split(image_path)
            self.selected_images_listbox.insert(tk.END, image_name)
            
    def convert_images_to_pdf(self):
        output_pdf_name = self.output_pdf_name.get()
        if not output_pdf_name:
            print("Please enter a PDF name.")
            return
        
        if not self.image_paths:
            print("Please select images to convert.")
            return
        
        size_option = self.selected_size.get()
        if size_option == "Custom Size":
            custom_size_window = tk.Toplevel(self.root)
            custom_size_window.title("Custom Size")
            
            width_label = tk.Label(custom_size_window, text="Width:")
            width_label.pack()
            width_entry = tk.Entry(custom_size_window, textvariable=self.custom_width)
            width_entry.pack()
            
            height_label = tk.Label(custom_size_window, text="Height:")
            height_label.pack()
            height_entry = tk.Entry(custom_size_window, textvariable=self.custom_height)
            height_entry.pack()
            
            confirm_button = tk.Button(custom_size_window, text="Confirm", command=self.apply_custom_size)
            confirm_button.pack()
        else:
            pdf = FPDF()
            for image_path in self.image_paths:
                pdf.add_page()
                if size_option == "Fit":
                    pdf.image(image_path, 0, 0, pdf.w, pdf.h)
                elif size_option == "A4 Size":
                    pdf.image(image_path, (pdf.w-210)/2, (pdf.h - 297) / 2, 210, 297)  # Standard A4 size
                elif size_option == "Contain":
                    pdf.image(image_path, 0, 0, 0, 0)
                elif size_option == "Letter Size":
                    pdf.image(image_path, (pdf.w - 215.9) / 2, (pdf.h - 279.4) / 2, 215.9, 279.4)  # Standard Letter size in millimeters (8.5 x 11 inches)
                elif size_option == "Legal Size":
                    pdf.image(image_path, (pdf.w - 215.9) / 2, (pdf.h - 355.6) / 2, 215.9, 355.6)  # Standard Legal size in millimeters (8.5 x 14 inches)
                elif size_option == "Square":
                    square_size = 200  # Size of the square in pixels
                    pdf.image(image_path, (pdf.w - square_size) / 2,(pdf.h - square_size) / 2 , square_size, square_size)
                elif size_option == "Thumbnail":
                    thumbnail_size = 150  # Average thumbnail size in pixels
                    pdf.image(image_path, (pdf.w - thumbnail_size) / 2,(pdf.h - thumbnail_size) / 2 , thumbnail_size, thumbnail_size)
            
            pdf.output(output_pdf_name + ".pdf")
    
    def apply_custom_size(self):
        custom_width = self.custom_width.get()
        custom_height = self.custom_height.get()
        try:
            custom_width = float(custom_width)
            custom_height = float(custom_height)
        except ValueError:
            print("Invalid input. Please enter numeric values for width and height.")
            return
        
        pdf = FPDF()
        for image_path in self.image_paths:
            pdf.add_page()
            pdf.image(image_path, (pdf.w - custom_width) / 2,(pdf.h - custom_height) / 2, custom_width, custom_height)
        
        output_pdf_name = self.output_pdf_name.get()
        pdf.output(output_pdf_name + ".pdf")

def main():
    root = tk.Tk()
    root.title("Image To Pdf")
    converter = ImageToPdfConverter(root)
    root.geometry("400x700")
    root.mainloop()

if __name__ == "__main__":
    main()
