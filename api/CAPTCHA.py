from PIL import Image, ImageDraw, ImageFont
import random
import io
import base64
import os
from pathlib import Path

def encode(key, msg):
    enc = list()
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(msg[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, msg):
    dec = list()
    message = base64.urlsafe_b64decode(msg).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)

# Set the image size
width = 500
height = 500
key = "kEY"
BASE_DIR = Path(__file__).resolve().parent.parent

def createCaptcha() -> tuple:

    # Generate a random background color
    bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Create a new image with the same size as the background
    img = Image.new('RGB', (width, height), color=bg_color)
    
    # Generate a random text string
    alphanumber = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    text = "".join(random.choice(alphanumber) for _ in range(5))

    # Choose a random font
    fontname = random.choice(os.listdir(os.path.join(BASE_DIR, "fonts")))
    fontsize = random.randint(80, 100)
    font = ImageFont.truetype(os.path.join(BASE_DIR, "fonts", fontname), size=fontsize)
    
    # Choose a random position for the text
    text_width, text_height = font.getsize(text)
    x = random.randint(0, max(0, width - text_width))
    y = random.randint(text_height, max(0, height - text_height))

    # Choose a random text color
    text_color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

    # Draw the text on the image
    draw = ImageDraw.Draw(img)

    # Generate random shapes
    for _ in range(10):
        shape = random.choice(['square', 'circle'])
        shape_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x1 = random.randint(0, max(0, width - 50))
        y1 = random.randint(0, max(0, height - 50))
        x2 = x1 + random.randint(20, 50)
        y2 = y1 + random.randint(20, 50)
        if shape == 'square':
            draw.rectangle((x1, y1, x2, y2), fill=shape_color)
        else:
            draw.ellipse((x1, y1, x2, y2), fill=shape_color)

    # Generate random lines
    for _ in range(10):
        line_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x1 = random.randint(0, max(0, width - 50))
        y1 = random.randint(0, max(0, height - 50))
        x2 = x1 + random.randint(20, 50)
        y2 = y1 + random.randint(20, 50)
        draw.line((x1, y1, x2, y2), fill=line_color, width=random.randint(2, 6))

    draw.text((x, y), text, font=font, fill=text_color)

    # Save the image to a buffer
    buffer = io.BytesIO()
    img.save(buffer, format='JPEG')

    # Convert the buffer to a base64-encoded string
    base64_str = base64.b64encode(buffer.getvalue()).decode('utf-8')


    #returning data
    return (encode(key, text), base64_str)

def checkCaptcha(token, value) -> bool:
    if decode(key, token) == value:
        return True
    else: return False