import cv2
import numpy as np
import matplotlib.pyplot as plt


def harris_corner_detection(image_path, min_distance=10, block_size=3, k_value=0.04, threshold=0.01):
    # Resmi oku
    img = cv2.imread(image_path)

    # Gri tonlamaya çevir
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Harris köşe tespiti için parametreleri ayarla
    corners = cv2.cornerHarris(gray, block_size, 3, k_value)

    # Köşeleri belirli bir eşik değerine göre seç
    corners_dilated = cv2.dilate(corners, None)
    img[corners_dilated > threshold * corners_dilated.max()] = [0, 0, 255]

    # Sonucu göster
    plt.figure(figsize=(8, 8))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Harris Köşe Tespiti")
    plt.axis("off")
    # Grafik figürünü numpy dizisine dönüştürme
    fig = plt.gcf()
    fig.canvas.draw()
    img = np.array(fig.canvas.renderer.buffer_rgba())

    # OpenCV ile görüntüleme
    cv2.imshow('Matplotlib Grafik', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
