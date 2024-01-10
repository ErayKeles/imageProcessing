import cv2
import numpy as np
import matplotlib.pyplot as plt


def watershed_algorithm_2(image_path):
    # Görüntüyü oku
    imgOrj = cv2.imread(image_path)

    # Medyan bulanıklaştırma uygula
    imgBlr = cv2.medianBlur(imgOrj, 31)

    # Gri tonlamaya çevir
    imgGray = cv2.cvtColor(imgBlr, cv2.COLOR_BGR2GRAY)

    # Eşikleme yap
    ret, imgTH = cv2.threshold(imgGray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Gürültüyü temizleme
    kernel = np.ones((5, 5), np.uint8)
    imgOpl = cv2.morphologyEx(imgTH, cv2.MORPH_OPEN, kernel, iterations=7)

    # Kesin arkaplan alanını elde etmek için genişletme işlemi uygula
    sureBG = cv2.dilate(imgOpl, kernel, iterations=3)

    # Her pikselin en yakın sıfır değerine sahip piksele olan mesafesini hesapla
    dist_transform = cv2.distanceTransform(imgOpl, cv2.DIST_L2, 5)

    # Eşikleme yap
    ret, sureFG = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    # Bilinmeyen bölgeleri bul
    sureFG = np.uint8(sureFG)
    unknown = cv2.subtract(sureBG, sureFG)

    # Etiketleme işlemi
    ret, markers = cv2.connectedComponents(sureFG, labels=5)

    # Bilinmeyen pikselleri etiketle
    markers += 1
    markers[unknown == 255] = 0

    # Watershed algoritması uygula
    markers = cv2.watershed(imgOrj, markers)

    # Contour'ları bul
    contours, hierarchy = cv2.findContours(markers, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    # Contour'ları orijinal görüntü üzerine çiz
    imgCopy = imgOrj.copy()
    for i in range(len(contours)):
        if hierarchy[0][i][3] == -1:
            cv2.drawContours(imgCopy, contours, i, (0, 255, 0), 5)

    # Sonuçları göster
    plt.figure(figsize=(15, 10))

    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(imgOrj, cv2.COLOR_BGR2RGB))
    plt.title("Orijinal Görüntü")

    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(imgBlr, cv2.COLOR_BGR2RGB))
    plt.title("Medyan Bulanıklaştırma")

    plt.subplot(2, 2, 3)
    plt.imshow(cv2.cvtColor(imgOpl, cv2.COLOR_BGR2RGB))
    plt.title("Açma İşlemi")

    plt.subplot(2, 2, 4)
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