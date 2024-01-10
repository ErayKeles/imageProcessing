import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

def adaptive_threshold_example(image_path, block_size=11, C=2, root=None):
    # Resmi gri tonlu olarak oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Adaptive threshold parametrelerini ayarla
    block_size = 11  # her pikselin eşik değerini hesaplamak için kullanılan komşu blok boyutu
    C = 2  # sabit, her pikselin eşik değerini ayarlamak için kullanılır

    # Adaptive threshold işlemi uygula
    adaptive_threshold = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, block_size, C
    )

    # Orijinal ve uygulanan adaptive threshold görüntülerini yan yana boyutlandırarak birleştir
    resized_original = cv2.resize(image, (400, 400))
    resized_threshold = cv2.resize(adaptive_threshold, (400, 400))
    combined_image = np.hstack([resized_original, resized_threshold])

    # Yeni pencere oluştur
    window = tk.Toplevel(root)
    window.title("Adaptive Threshold Örneği")

    # Tek bir resmi Tkinter PhotoImage objesine çevir
    combined_image = Image.fromarray(combined_image)
    photo = ImageTk.PhotoImage(combined_image)

    # Resmi Canvas üzerine yerleştir
    canvas = tk.Canvas(window, width=combined_image.width, height=combined_image.height)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    # Metni Canvas üzerine yerleştir
    text_label = tk.Label(window, text="Sol: Renklendirilmis Resim | Sağ: Adaptive Threshold", bg="gray", fg="white")
    text_label.pack(side=tk.TOP, fill=tk.X)

    # Pencereyi göster
    window.mainloop()
