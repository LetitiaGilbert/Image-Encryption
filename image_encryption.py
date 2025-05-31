from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Open image and convert to numpy array
    img = Image.open(input_path)
    img_array = np.array(img)

    # XOR operation on each pixel value
    encrypted_array = img_array ^ key

    # Convert back to image and save
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    # XOR operation is symmetric: encrypt and decrypt are the same
    encrypt_image(input_path, output_path, key)
    print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    input_img = "/Users/letitiagilbert/Desktop/prodigy/test.png"   # Change this to your input image path
    encrypted_img = "encrypted_image.png"
    decrypted_img = "decrypted_image.png"
    key = 123  # Simple XOR key (0-255)

    encrypt_image(input_img, encrypted_img, key)
    decrypt_image(encrypted_img, decrypted_img, key)
