import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

root = tk.Tk()
root.title("Watermark App")

# Add a button to open the file dialog
def open_image():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

    # Load the image using Pillow
    image = Image.open(filepath)

    # Create a transparent overlay for the watermark
    watermark = Image.new("RGBA", image.size, (0, 0, 0, 0))

    # Choose a font and size for the watermark text
    font = ImageFont.truetype("arial.ttf", 50)

    # Create a Draw object to draw the watermark
    draw = ImageDraw.Draw(watermark)

    # Set the position and text of the watermark
    watermark_text = "hey"
    text_width, text_height = draw.textsize(watermark_text, font)
    x = image.width - text_width - 10
    y = image.height - text_height - 10
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

    # Apply the watermark to the image
    watermarked_image = Image.alpha_composite(image.convert("RGBA"), watermark)

    # Display the watermarked image in the Tkinter canvas
    tk_image = ImageTk.PhotoImage(watermarked_image)
    canvas.create_image(0, 0, anchor="nw", image=tk_image)
    canvas.image = tk_image  # Keep a reference to avoid garbage collection

open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

# Add a canvas to display the image
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

root.mainloop()
