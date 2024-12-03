import qrcode

# Data to encode
data = "https://nayanpal01.github.io/anabd/"  # Replace with your URL or text

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 = 21x21, up to 40 = 177x177)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border (minimum is 4)
)

# Add data to the QR Code
qr.add_data(data)
qr.make(fit=True)

# Create the image
img = qr.make_image(fill="black", back_color="white")

# Save the image
img.save("qrcode.png")

print("QR code generated and saved as qrcode.png")
