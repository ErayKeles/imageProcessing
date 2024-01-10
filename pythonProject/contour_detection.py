import cv2
import matplotlib.pyplot as plt

def contour_detection(image_path):
    # Resmi yükle
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Kenarlara tespit etmek için Canny kenar dedektörünü kullan
    edges = cv2.Canny(gray, 50, 150)

    # Konturları bul
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Konturları çiz
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

    # Resmi göster
    cv2.imshow('Contours', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

