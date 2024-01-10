import cv2
import numpy as np
import matplotlib.pyplot as plt


def watershed_algorithm(image_path):
    # Resmi oku
    img = cv2.imread(image_path)

    # Gri tonlamaya çevir
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Morfolojik işlemler uygula
    sureBG = cv2.dilate(imgGray, None, iterations=3)
    sureFG = cv2.erode(sureBG, None, iterations=15)
    sureFG = cv2.dilate(sureFG, None, iterations=3)

    # Uzak noktaların bulunması
    dist_transform = cv2.distanceTransform(imgGray, cv2.DIST_L2, 5)

    # Eşikleme yap
    ret, sureF6 = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    # Bilinmeyen bölgeleri bul
    sureFG = np.uint8(sureFG)
    unknown = cv2.subtract(sureBG, sureFG)

    # Etiketleme işlemi
    ret, markers = cv2.connectedComponents(sureFG, labels=5)

    # Bilinmeyen pikselleri etiketle
    markers += 1
    markers[unknown == 255] = 0

    # Watershed algoritması uygula
    markers = cv2.watershed(img, markers)

    # Contour'ları bul
    contours, hierarchy = cv2.findContours(markers, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    # Contour'ları orijinal görüntü üzerine çiz
    imgCopy = img.copy()
    for i in range(len(contours)):
        if hierarchy[0][i][3] == -1:
            cv2.drawContours(imgCopy, contours, i, (0, 255, 0), 5)

    # Sonuçları göster
    plt.figure(figsize=(30, 30))

    plt.subplot(3, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Orijinal Görüntü")

    plt.subplot(3, 3, 2)
    plt.imshow(cv2.cvtColor(imgGray, cv2.COLOR_BGR2RGB))
    plt.title("Gri Tonlamalı Görüntü")

    plt.subplot(3, 3, 3)
    plt.imshow(cv2.cvtColor(sureBG, cv2.COLOR_BGR2RGB))
    plt.title("SureBG")

    plt.subplot(3, 3, 4)
    plt.imshow(cv2.cvtColor(sureFG, cv2.COLOR_BGR2RGB))
    plt.title("SureFG")

    plt.subplot(3, 3, 5)
    plt.imshow(cv2.cvtColor(dist_transform, cv2.COLOR_BGR2RGB))
    plt.title("Uzak Noktalar")

    plt.subplot(3, 3, 6)
    plt.imshow(cv2.cvtColor(sureF6, cv2.COLOR_BGR2RGB))
    plt.title("Eşiklenmiş Görüntü")

    plt.subplot(3, 3, 7)
    plt.imshow(cv2.cvtColor(unknown, cv2.COLOR_BGR2RGB))
    plt.title("Bilinmeyen Bölgeler")

    plt.subplot(3, 3, 8)
    plt.imshow(cv2.cvtColor(imgCopy, cv2.COLOR_BGR2RGB))
    plt.title("Sonuç (Contour'lar)")

    fig = plt.gcf()
    fig.canvas.draw()
    img = np.array(fig.canvas.renderer.buffer_rgba())

    # Resmi 1280x720 boyutuna yeniden boyutlandırma
    max_width = 1280
    max_height = 720
    img_height, img_width, _ = img.shape
    if img_width > max_width or img_height > max_height:
        ratio = min(max_width / img_width, max_height / img_height)
        img = cv2.resize(img, (int(img_width * ratio), int(img_height * ratio)))

    # OpenCV ile görüntüleme
    cv2.imshow('Matplotlib Grafik', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()