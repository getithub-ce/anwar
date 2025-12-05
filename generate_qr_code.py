import qrcode

# Replace this with the HTTPS URL where you host location-photo-capture.html
url = "https://yourdomain.com/location-photo-capture.html"

# Generate QR code
img = qrcode.make(url)
img.save("qr_code_location_photo.png")

print("QR code generated and saved as qr_code_location_photo.png")