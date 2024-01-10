import cv2

def live_face_detection():
    # Yüz tespiti için Cascade Classifier'ı yükle
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Kamera açma
    cap = cv2.VideoCapture(0)  # 0, yerel kamerayı temsil eder. Farklı bir sayı kullanarak başka bir kamera seçebilirsiniz.

    if not cap.isOpened():
        print("Kamera açılamadı. Lütfen bağlı olduğundan emin olun.")
        return

    while True:
        # Kameradan bir kareyi oku
        ret, frame = cap.read()

        if not ret:
            print("Kare okunamadı. Çıkılıyor...")
            break

        # Yüz tespiti işlemi
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        # Tespit edilen yüzleri çerçeve içine al
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Kameradan alınan görüntüyü göster
        cv2.imshow('Live Face Detection', frame)

        # 'q' tuşuna basıldığında döngüyü kır
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kamerayı serbest bırak ve pencereyi kapat
    cap.release()
    cv2.destroyAllWindows()