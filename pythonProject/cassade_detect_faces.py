import cv2
import numpy as np
import matplotlib.pyplot as plt

def cassade_detect_faces(image_path):
    # Resmi oku
    img = cv2.imread(image_path)
    # Gri tonlamaya çevir
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Haar Cascade sınıflandırıcısını yükle
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Yüzleri tespit et
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=6)

    # Yüzleri çerçeve içine al
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 10)

    # Sonucu göster
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Yüz Tespiti")
    plt.axis("off")

    # Grafik figürünü numpy dizisine dönüştürme
    fig = plt.gcf()
    fig.canvas.draw()
    img = np.array(fig.canvas.renderer.buffer_rgba())

    # OpenCV ile görüntüleme
    cv2.imshow('Matplotlib Grafik', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
