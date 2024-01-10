

from tkinter import Canvas, NW, Tk, Label, TOP, X
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
def image_processing_example(image, root=None):
    # Uygulanacak kernel boyutunu belirle
    kernel_size = 5

    # Blur işlemleri
    blurred_image = cv2.blur(image, (kernel_size, kernel_size))
    median_blurred_image = cv2.medianBlur(image, kernel_size)
    box_filtered_image = cv2.boxFilter(image, -1, (kernel_size, kernel_size))
    bilateral_filtered_image = cv2.bilateralFilter(image, 9, 75, 75)
    gaussian_blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # İşlenmiş ve orijinal görüntüleri üstte ve altta boyutlandırarak birleştir
    resized_original = cv2.resize(image, (350, 350))
    resized_blurred = cv2.resize(blurred_image, (350, 350))
    resized_median_blurred = cv2.resize(median_blurred_image, (350, 350))
    resized_box_filtered = cv2.resize(box_filtered_image, (350, 350))
    resized_bilateral_filtered = cv2.resize(bilateral_filtered_image, (350, 350))
    resized_gaussian_blurred = cv2.resize(gaussian_blurred_image, (350, 350))

    combined_image_top = np.hstack([
        resized_original, resized_blurred, resized_median_blurred
    ])

    combined_image_bottom = np.hstack([
        resized_box_filtered, resized_bilateral_filtered, resized_gaussian_blurred
    ])

    combined_image = np.vstack([combined_image_top, combined_image_bottom])

    # Görüntü verisini uygun formata çevir
    combined_image = combined_image.astype(np.uint8)

    # Yeni pencere oluştur
    window = tk.Toplevel(root)
    window.title("Bulanıklaştırma Filtreleri")

    # Tek bir resmi Tkinter PhotoImage objesine çevir
    combined_image = Image.fromarray(combined_image)
    photo = ImageTk.PhotoImage(combined_image)

    # Resmi Canvas üzerine yerleştir
    canvas = tk.Canvas(window, width=combined_image.width, height=combined_image.height)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    # Metni Canvas üzerine yerleştir
    text_label = tk.Label(window, text="Üstte: Orijinal, Blur, Median Blur | Alttan İtibaren: Box Filter, Bilateral Filter, Gaussian Blur", bg="gray", fg="white")
    text_label.pack(side=tk.TOP, fill=tk.X)

    # Pencereyi göster
    window.mainloop()

