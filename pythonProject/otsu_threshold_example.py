import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

def otsu_threshold_example(image_path, root=None):
    # Resmi gri tonlu olarak oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Otsu eşikleme işlemi uygula
    _, otsu_threshold = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Orijinal ve Otsu eşikleme sonucu görüntülerini yan yana boyutlandırarak birleştir
    resized_original = cv2.resize(image, (500, 500))
    resized_otsu_threshold = cv2.resize(otsu_threshold, (500, 500))
    combined_image = np.hstack([resized_original, resized_otsu_threshold])

    # Yeni pencere oluştur
    window = tk.Toplevel(root)
    window.title("Otsu Eşikleme Örneği")

    # Tek bir resmi Tkinter PhotoImage objesine çevir
    combined_image = Image.fromarray(combined_image)
    photo = ImageTk.PhotoImage(combined_image)

    # Resmi Canvas üzerine yerleştir
    canvas = tk.Canvas(window, width=combined_image.width, height=combined_image.height)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    # Metni Canvas üzerine yerleştir
    text_label = tk.Label(window, text="Sol: Renklendirilmis Resim | Sağ: Otsu Eşikleme", bg="gray", fg="white")
    text_label.pack(side=tk.TOP, fill=tk.X)

    # Pencereyi göster
    window.mainloop()
