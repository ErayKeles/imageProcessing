import cv2
import numpy as np
import matplotlib.pyplot as plt

def laplacian_edge_detection(image_path):
    # Görüntüyü siyah-beyaz olarak oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Laplacian operatörü ile kenar tespiti
    laplacian_result = cv2.Laplacian(image, cv2.CV_64F)

    # Laplacian görüntüyü normalize et
    laplacian_result = np.uint8(np.absolute(laplacian_result))

    # Görüntüyü GaussianBlur ile yumuşat ve tekrar Laplacian uygula
    blurred_image = cv2.GaussianBlur(image, (3, 3), 0)
    laplacian_result_blurred = cv2.Laplacian(blurred_image, cv2.CV_64F)

    # Laplacian görüntüyü normalize et
    laplacian_result_blurred = np.uint8(np.absolute(laplacian_result_blurred))

    # Görüntüleri göster
    plt.figure(figsize=(17, 5))
    plt.subplot(1, 3, 1), plt.imshow(image, cmap="gray"), plt.title("Orijinal Görüntü")
    plt.subplot(1, 3, 2), plt.imshow(laplacian_result, cmap="gray"), plt.title("Laplacian Kenar Tespiti")
    plt.subplot(1, 3, 3), plt.imshow(laplacian_result_blurred, cmap="gray"), plt.title("Blur + Laplacian")

    # Grafik figürünü numpy dizisine dönüştürme
    fig = plt.gcf()
    fig.canvas.draw()
    img = np.array(fig.canvas.renderer.buffer_rgba())

    # OpenCV ile görüntüleme
    cv2.imshow('Matplotlib Grafik', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()