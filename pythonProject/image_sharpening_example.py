
import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk
def image_sharpening_example(image, root=None):
    # Kernel tanımla
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    # filter2D fonksiyonunu kullanarak resmi işle
    sharpened_image = cv2.filter2D(image, -1, kernel)

    # İşlenmiş Görüntüleri Yan Yana Boyutlandırarak Birleştir
    resized_original = cv2.resize(image, (500, 500))
    resized_sharpened = cv2.resize(sharpened_image, (500, 500))
    combined_image = np.hstack([resized_original, resized_sharpened])

    # Görüntü verisini uygun formata çevir
    combined_image = combined_image.astype(np.uint8)

    # Yeni pencere oluştur
    window = tk.Toplevel(root)
    window.title("Görüntü Keskinleştirme Örneği")

    # Tek bir resmi Tkinter PhotoImage objesine çevir
    combined_image = Image.fromarray(combined_image)
    photo = ImageTk.PhotoImage(combined_image)

    # Resmi Canvas üzerine yerleştir
    canvas = tk.Canvas(window, width=combined_image.width, height=combined_image.height)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    # Metni Canvas üzerine yerleştir
    text_label = tk.Label(window, text="Sol: Orijinal Resim | Sağ: Görüntü Keskinleştirme", bg="gray", fg="white")
    text_label.pack(side=tk.TOP, fill=tk.X)

    # Pencereyi göster
    window.mainloop()

