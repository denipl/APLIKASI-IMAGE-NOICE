import cv2
import numpy as np

def gaussian_filter(img, kernel_size=5, sigma=1.0):
  """Menerapkan filter Gaussian pada gambar.

  Args:
    img: Gambar input.
    kernel_size: Ukuran kernel Gaussian (bilangan ganjil).
    sigma: Parameter standar deviasi Gaussian.

  Returns:
    Gambar hasil filter Gaussian.
  """

  # Membuat kernel Gaussian
  x, y = np.meshgrid(np.arange(kernel_size), np.arange(kernel_size))
  sigma2 = 2 * sigma * sigma
  kernel = np.exp(-((x - (kernel_size - 1) / 2) ** 2 + (y - (kernel_size - 1) / 2) ** 2) / sigma2)
  kernel = kernel / np.sum(kernel)

  # Konvolusi gambar dengan kernel Gaussian
  img_filtered = cv2.filter2D(img, -1, kernel)

  return img_filtered

# Contoh penggunaan
img = cv2.imread('noisy_gaussian.jpg')
img_filtered = gaussian_filter(img, kernel_size=7, sigma=2)
cv2.imwrite('filtered_image.jpg', img_filtered)