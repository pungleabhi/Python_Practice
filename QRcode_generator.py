# import qrcode

# data = input("Enter the text or URL: ").strip()   # here we used strip to remove any white spaces from the input taken from user
# filename = input("Enter the filename: ").strip()
# qr = qrcode.QRCode(box_size=10, border=4)
# qr.add_data(data)
# image = qr.make_image(fill_color='black', back_color='white')
# image.save(filename)
# print(f"QR code saved as {filename}")

import qrcode

data = input("Enter the text or URL: ")
filename = input("Enter the filename: ")

img = qrcode.make(data)
img.save(f"{filename}.png")   # always saves as PNG

print(f"QR code saved as {filename}.png")