import qrcode

user = input("Enter the text or URL :").strip()
file_name = input("Enter the filename :").strip()
QR = qrcode.QRCode(box_size = 100 , border = 4)
QR.add_data(user)
Image = QR.make_image(fill_color = "black" , back_color = "white")
Image.save(file_name)
print(f"QR code saved as {file_name}")