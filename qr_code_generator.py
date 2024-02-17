import qrcode
import image 
qr= qrcode.QRCode(
    version = 30,
    box_size = 15,
    border = 5
)
data = "https://github.com/pandey-gauri?tab=repositories"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("test.png")