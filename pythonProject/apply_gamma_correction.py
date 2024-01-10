
from tkinter import Canvas, NW, Tk, Label, TOP, X
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
def apply_gamma_correction(image, gamma=3.0, root=None):
    # Giriş görüntüsünü [0, 1] aralığına normalize et
    image_normalized = image / 255.0

    # Gamma düzeltmesi uygula
    gamma_corrected = np.power(image_normalized, gamma)

    # Görüntüyü [0, 255] aralığına geri ölçekle
    gamma_corrected = np.uint8(gamma_corrected * 255)

    # Orijinal ve Gamma düzeltmesi sonucu görüntüleri yan yana boyutlandırarak birleştir
    resized_original = cv2.resize(image, (500, 500))
    resized_gamma_corrected = cv2.resize(gamma_corrected, (500, 500))
    combined_image = np.hstack([resized_original, resized_gamma_corrected])

    # Yeni pencere oluştur
    window = tk.Toplevel(root)
    window.title("Gama Filtresi")

    # Tek bir resmi Tkinter PhotoImage objesine çevir
    combined_image = Image.fromarray(combined_image)
    photo = ImageTk.PhotoImage(combined_image)

    # Resmi Canvas üzerine yerleştir
    canvas = tk.Canvas(window, width=combined_image.width, height=combined_image.height)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    # Metni Canvas üzerine yerleştir
    text_label = tk.Label(window, text="Sol: Orijinal Resim | Sağ: Adaptive Threshold", bg="gray", fg="white")
    text_label.pack(side=tk.TOP, fill=tk.X)

    # Pencereyi göster
    window.mainloop()


def show_image_with_tkinter(image, window_title):
    root = Tk()
    root.title(window_title)
    canvas = Canvas(root, width=image.shape[1], height=image.shape[0])
    canvas.pack()
    photo = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))
    canvas.create_image(0, 0, anchor=NW, image=photo)
    root.mainloop()