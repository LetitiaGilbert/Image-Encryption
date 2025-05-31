# Image-Encryption
A Python image encryption/decryption tool using pixel manipulation

This is a Python image encryption/decryption tool which uses pixel manipulation. It will:
1. Load an image
2. Encrypt by swapping pixels or applying a simple XOR operation on pixel values
3. Decrypt by reversing the operation

It uses Pillow for image handling and NumPy for pixel array manipulation. This approach works on RGB images.

How it works:

Encryption: XOR each pixel value with a key or swap pixel positions based on a key.
Decryption: Apply the same XOR or reverse the swaps.

How to use:

Install Pillow and numpy if you don’t have them:
>pip install pillow numpy

>pip install Pillow

Put your image in the same folder or provide full path.
Run the script.
It creates an encrypted image and then decrypts it back.
The key is an integer 0-255.
XOR (^) applied to each pixel channel value scrambles the image.
XOR with the same key again returns original pixels.
