import qrcode

data = "KTC RW"  # данные для создания QRCode
print('Данные QRCode -->', data)
qr = qrcode.QRCode(version=2, box_size=30, border=5, error_correction=qrcode.constants.ERROR_CORRECT_Q,)  # создать QRCode
qr.add_data(data)  # добавить данные в QR-код
img = qr.make_image(fill_color="black", back_color="white")  # переносим реальное изображение
img.save("photo/rez.png")  # куда сохраняем файл (путь)
