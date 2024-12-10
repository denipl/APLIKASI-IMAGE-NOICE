import cv2
import numpy as np

def add_gaussian_noise(image, mean=0, std=25):
  """Menambahkan Gaussian noise pada gambar.

  Args:
    image: Gambar input.
    mean: Rata-rata distribusi Gaussian.
    std: Deviasi standar distribusi Gaussian.

  Returns:
    Gambar dengan noise Gaussian.
  """

  row, col, ch = image.shape
  noise = np.random.normal(mean, std, (row, col, ch))
  noise = noise.astype(np.uint8)
  img_noisy = cv2.add(image, noise)
  return img_noisy

# Contoh penggunaan
img = cv2.imread('tes.png')
noisy_img = add_gaussian_noise(img)
cv2.imwrite('noisy_gaussian.jpg', noisy_img)