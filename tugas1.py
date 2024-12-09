from PIL import Image

# Buka gambar
my_image = Image.open('tes.png')

# Tentukan ukuran baru
new_width = 800  # Ganti dengan lebar yang diinginkan
new_height = 600  # Ganti dengan tinggi yang diinginkan

# Ubah ukuran gambar
my_image = my_image.resize((new_width, new_height))

# Konversi gambar ke mode RGB
my_image = my_image.convert('RGB')

# Simpan gambar dalam format JPEG
my_image.save('compressedResized.jpg')
