import cv2
import numpy as np
from matplotlib import pyplot as plt

def image_histogram_example(image):
    # Histogram hesapla
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    # Histogram eğrisini çiz
    plt.bar(range(256), hist.flatten(), color='blue', alpha=0.7, width=0.8)
    plt.title('Histogram Eğrisi')
    plt.xlabel('Piksel Değeri')
    plt.ylabel('Piksel Sayısı')

    # Histogram eğrisini göster
    plt.show()

    # İşlenmiş görüntüyü göster
    cv2.imshow("İşlenmiş Görüntü", image)

    # Yeni bir pencere aç ve histogram eğrisini burada göster
    plt.figure()
    plt.bar(range(256), hist.flatten(), color='blue', alpha=0.7, width=0.8)
    plt.title('Histogram Eğrisi')
    plt.xlabel('Piksel Değeri')
    plt.ylabel('Piksel Sayısı')
    fig = plt.gcf()
    fig.canvas.draw()
    img = np.array(fig.canvas.renderer.buffer_rgba())

    # OpenCV ile görüntüleme
    cv2.imshow('Matplotlib Grafik', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.waitKey(0)
    cv2.destroyAllWindows()


fig = plt.gcf()
fig.canvas.draw()
img = np.array(fig.canvas.renderer.buffer_rgba())

