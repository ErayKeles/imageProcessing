from tkinter import Canvas, NW, Tk
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk


def kenarlik_ekleme_example(image, border_width=20, border_color=(0, 0, 0), method="CONSTANT"):
    # Resmin etrafına kenar eklemek için cv2.copyMakeBorder kullanın
    if method == "CONSTANT":
        image_with_border = cv2.copyMakeBorder(image, border_width, border_width, border_width, border_width,
                                               cv2.BORDER_CONSTANT, value=border_color)
    elif method == "REPLICATE":
        image_with_border = cv2.copyMakeBorder(image, border_width, border_width, border_width, border_width,
                                               cv2.BORDER_REPLICATE)
    else:
        print("Geçersiz kenarlık ekleme yöntemi.")
        return

    # Orijinal ve kenarlıklı görüntüyü yan yana boyutlandırarak birleştir
    resized_original = cv2.resize(image, (500, 500))
    resized_with_border = cv2.resize(image_with_border, (500, 500))
    combined_image = np.hstack([resized_original, resized_with_border])

    # Yeni pencere oluştur
    window = tk.Toplevel()
    window.title("Kenarlık Ekleme")

    # Tek bir resmi Tkinter PhotoImage objesine çevir
    combined_image = Image.fromarray(combined_image)
    photo = ImageTk.PhotoImage(combined_image)

    # Oluşturulan Canvas
    canvas = Canvas(window, width=combined_image.width, height=combined_image.height)
    canvas.pack()

    # Resmi Canvas üzerine yerleştir
    canvas.create_image(0, 0, anchor=NW, image=photo)

    # Metinleri Canvas üzerine yerleştir
    canvas.create_text(10, 10, anchor=NW, text=" Orijinal Resim", fill="white")
    canvas.create_text(510, 10, anchor=NW, text=" Kenarlık Ekleme", fill="white")

    # Pencereyi göster
    window.mainloop()
