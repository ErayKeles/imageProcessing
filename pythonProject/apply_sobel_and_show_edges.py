import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

def apply_sobel_and_show_edges(image, root=None):
    # Sobel operatörünü uygula
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Mutlak değeri al
    sobelx = np.abs(sobelx)
    sobely = np.abs(sobely)

    # Dikey ve yatay kenarları birleştir
    edges = cv2.bitwise_or(sobelx, sobely)

    # Orijinal ve Sobel kenarlarını yan yana boyutlandırarak birleştir
    resized_original = cv2.resize(image, (500, 500))
    resized_edges = cv2.resize(edges, (500, 500))
    combined_image = np.hstack([resized_original, resized_edges])

    # Görüntü verisini uygun formata çevir
    combined_image = combined_image.astype(np.uint8)

    # Yeni pencere oluştur
    window = tk.Toplevel(root)
    window.title("Sobel Kenar Tespiti")

    # Tek bir resmi Tkinter PhotoImage objesine çevir
    combined_image = Image.fromarray(combined_image)
    photo = ImageTk.PhotoImage(combined_image)

    # Resmi Canvas üzerine yerleştir
    canvas = tk.Canvas(window, width=combined_image.width, height=combined_image.height)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    # Metni Canvas üzerine yerleştir
    text_label = tk.Label(window, text="Sol: Orijinal Resim | Sağ: Sobel Kenar Tespiti", bg="gray", fg="white")
    text_label.pack(side=tk.TOP, fill=tk.X)

    # Pencereyi göster
    window.mainloop()

