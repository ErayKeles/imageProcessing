import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny_edge_detection(image, low_threshold=50, high_threshold=150):
    # Canny kenar tespiti uygula
    edges = cv2.Canny(image, low_threshold, high_threshold, L2gradient=True)

    # Görselleştirme
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap="gray")
    plt.title("Orjinal Görüntü")

    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap="gray")
    plt.title("Canny Kenar Tespiti")

    # Grafik figürünü numpy dizisine dönüştürme
    fig = plt.gcf()
    fig.canvas.draw()
    img = np.array(fig.canvas.renderer.buffer_rgba())

    # OpenCV ile görüntüleme
    cv2.imshow('Matplotlib Grafik', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
