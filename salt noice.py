import cv2
import numpy as np

def add_salt_pepper_noise(image, prob=0.05):
  """Menambahkan Salt and Pepper noise pada gambar.

  Args:
    image: Gambar input.
    prob: Probabilitas setiap pixel menjadi noise.

  Returns:
    Gambar dengan noise Salt and Pepper.
  """

  output = np.zeros(image.shape, np.uint8)
  thres = 1 - prob
  for i in range(image.shape[0]):
    for j in range(image.shape[1]):
      rdn = np.random.random()
      if rdn < prob:
        output[i][j] = 0
      elif rdn > thres:
        output[i][j] = 255
      else:
        output[i][j] = image[i][j]
  return output

# Contoh penggunaan
img = cv2.imread('tes.png')
noisy_img = add_salt_pepper_noise(img)
cv2.imwrite('noisy_salt.jpg', noisy_img)