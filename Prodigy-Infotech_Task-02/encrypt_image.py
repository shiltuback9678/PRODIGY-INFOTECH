from PIL import Image

def encrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Simple encryption: swap R and B channels
            encrypted_pixel = (b, g, r)
            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path):
    img = Image.open(input_path)
    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Simple decryption: swap R and B channels back
            decrypted_pixel = (b, g, r)
            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")

# Replace with your actual image paths
input_image = "/home/kali/Desktop/New folder/input.jpg"
encrypted_image = "/home/kali/Desktop/New folder/encrypted_image.jpg"
decrypted_image = "/home/kali/Desktop/New folder/decrypted_image.jpg"

encrypt_image(input_image, encrypted_image)
decrypt_image(encrypted_image, decrypted_image)

