import cv2
import numpy as np
import matplotlib.pyplot as plt

def deriche_edge_detection(image_path, alpha=0.5, kernel_size=3):
    # Görüntüyü siyah-beyaz olarak oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Deriche filtresi için sobel türevlerini kullan
    deriche_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=kernel_size)
    deriche_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=kernel_size)

    # Deriche filtresiyle türevleri birleştir
    edges = np.sqrt(alpha * deriche_x**2 + alpha * deriche_y**2)

    # Görselleştirme
    plt.figure(figsize=(17, 7))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap="gray")
    plt.title("Orjinal Görüntü")

    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap="gray")
    plt.title("Deriche Kenar Tespiti")

    # Grafik figürünü numpy dizisine dönüştürme
    fig = plt.gcf()
    fig.canvas.draw()
    img = np.array(fig.canvas.renderer.buffer_rgba())

    # OpenCV ile görüntüleme
    cv2.imshow('Matplotlib Grafik', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

