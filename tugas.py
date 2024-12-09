import cv2
import numpy as np

# Membaca gambar
img = cv2.imread('images.jpeg')

# Median Filtering
median = cv2.medianBlur(img, 5)

# Gaussian Blur
blur = cv2.GaussianBlur(img, (5,5), 0)

# Bilateral Filtering
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# Menampilkan hasil
cv2.imshow('Original', img)
#cv2.imshow('Median', median)
cv2.imshow('Gaussian', blur)
#v2.imshow('Bilateral', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()