import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import unicodedata
from adaptive_threshold_example import adaptive_threshold_example
from kenarlik_ekleme_example import kenarlik_ekleme_example
from image_processing_example import image_processing_example
from image_sharpening_example import image_sharpening_example
from apply_gamma_correction import apply_gamma_correction
from image_histogram_example import image_histogram_example
from apply_sobel_and_show_edges import apply_sobel_and_show_edges
from laplacian_edge_detection import laplacian_edge_detection
from canny_edge_detection import canny_edge_detection
from deriche_edge_detection import deriche_edge_detection
from harris_corner_detection import harris_corner_detection
from cassade_detect_faces import cassade_detect_faces
from contour_detection import contour_detection
from watershed_algorithm import watershed_algorithm
from watershed_algorithm_2 import watershed_algorithm_2
from face_detection import face_detection
from otsu_threshold_example import otsu_threshold_example
from live_face_detection import live_face_detection
class GörüntüİşlemeUygulaması:
    def __init__(self, root):
        self.root = root
        self.root.title("Görüntü İşleme Uygulaması")

        # Create canvas to display the selected image
        self.canvas = tk.Canvas(self.root, width=700, height=1000,bg="gray")
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create button to open the file dialog
        self.open_button = tk.Button(root, text="Görsel Yükle", command=self.gorsel_yukle,bg="gray")
        self.open_button.pack(side=tk.TOP, fill="x", pady=10)
        #Canlı yüz tespit  butonu
        self.live_face_detection_button = tk.Button(root, text="Canlı Yüz Tespiti", command=self.live_face_detection,bg="gray", relief=tk.GROOVE)
        self.live_face_detection_button.pack(side=tk.TOP, fill="x", padx=5, pady=5)

        self.algoritmalar = {
            "Adaptive Threshold": lambda img: adaptive_threshold_example(self.image_path,11,2),
            "Otsu Threshold": lambda img: otsu_threshold_example(self.image_path),
            "Sobel": apply_sobel_and_show_edges,
            "Gama Filtre": apply_gamma_correction,
            "Keskinlestirme": image_sharpening_example,
            "Bulanıklaştırmalar": image_processing_example,
            "Histogram Eğrisi": image_histogram_example,
            "Kenarlık Ekleme (CONSTANT)": lambda img: kenarlik_ekleme_example(img, method="CONSTANT"),
            "Kenarlık Ekleme (REPLICATE)": lambda img: kenarlik_ekleme_example(img, method="REPLICATE"),
            "Laplacian Edge Detection": lambda img: laplacian_edge_detection(self.image_path),
            "Canny Kenar Tespit": canny_edge_detection,
            "Deriche Kenar Tespit": lambda img: deriche_edge_detection(self.image_path),
            "Harris Kenar Tespit": lambda img: harris_corner_detection(self.image_path),
            "Cascade": lambda img: cassade_detect_faces(self.image_path),
            "Kontur Tespit": lambda img: contour_detection(self.image_path),
            "Watershed": lambda img: watershed_algorithm(self.image_path),
            "Watershed-2": lambda img: watershed_algorithm_2(self.image_path),
            "Yüz Tespit": lambda img: face_detection(self.image_path),
        }

        for algoritma_adı in self.algoritmalar.keys():
            btn = tk.Button(root, text=algoritma_adı, command=lambda a=algoritma_adı: self.algoritma_secildi(a),bg="gray", relief=tk.GROOVE)
            btn.pack(side=tk.TOP, fill="x", padx=5, pady=5)

    def gorsel_yukle(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        file_path = unicodedata.normalize('NFC', file_path)
        print(file_path)
        if os.path.exists(file_path):
            image = cv2.imread(file_path)
            if image is not None:
                self.image_path = file_path  # Dosya yolunu sakla
                self.image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                self.display_image()
            else:
                print("Dosya okuma hatası.")
        else:
            print("Geçersiz dosya yolu.")

    def display_image(self):
        self.clear_canvas()
        image = Image.fromarray(self.image)
        self.photo = ImageTk.PhotoImage(image.resize((500, 400), resample=Image.BICUBIC))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.root.update_idletasks()  # Güncellenmiş pencereyi görüntüle

    def algoritma_secildi(self, algoritma_adı):
        algoritma = self.algoritmalar.get(algoritma_adı)
        if callable(algoritma):
            algoritma(self.image.copy())

    def live_face_detection(self):
            live_face_detection()

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = GörüntüİşlemeUygulaması(root)
    root.mainloop()
