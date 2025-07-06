# APLIKASI-IMAGE-NOICE

Proyek ini berisi skrip Python untuk menambahkan noise (Gaussian dan Salt & Pepper) pada gambar serta melakukan filtering menggunakan Gaussian filter.

## Struktur File

- `gausian noice.py` — Menambahkan Gaussian noise pada gambar.
- `salt noice.py` — Menambahkan Salt & Pepper noise pada gambar.
- `fillter noice.py` — Menerapkan Gaussian filter pada gambar.
- `tes.png`, `tes21.png`, `images.jpeg` — Contoh gambar input/output.

## Kebutuhan

- Python 3.x
- OpenCV (`cv2`)
- NumPy

Install dependensi dengan:
```sh
pip install opencv-python numpy
```

## Cara Penggunaan

### 1. Menambahkan Gaussian Noise
Jalankan:
```sh
python "gausian noice.py"
```
Output: `noisy_gaussian.jpg`

### 2. Menambahkan Salt & Pepper Noise
Jalankan:
```sh
python "salt noice.py"
```
Output: `noisy_salt.jpg`

### 3. Filter Gaussian pada Gambar
Pastikan sudah ada file `noisy_gaussian.jpg`, lalu jalankan:
```sh
python "fillter noice.py"
```
Output: `filtered_image.jpg`

## Lisensi

Proyek ini bebas digunakan untuk pembelajaran.
