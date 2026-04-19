from PIL import Image, ImageDraw, ImageFont
import urllib.request
import io

# Create a blank image with the background color
width, height = 1080, 1080
image = Image.new('RGB', (width, height), color='#1a3644')
draw = ImageDraw.Draw(image)

# Add text
try:
    font_title = ImageFont.truetype("arial.ttf", 100)
    font_text = ImageFont.truetype("arial.ttf", 40)
except IOError:
    font_title = ImageFont.load_default()
    font_text = ImageFont.load_default()

draw.text((540, 200), "B-2 Spirit", font=font_title, fill="#ffffff", anchor="mm")
draw.text((540, 350), "Unrivaled stealth, unmatched global reach.", font=font_text, fill="#c0e0ff", anchor="mm")

# Download and add the bomber image
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/B-2_Spirit_original.jpg/800px-B-2_Spirit_original.jpg"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        img_data = response.read()
    bomber_img = Image.open(io.BytesIO(img_data))
    bomber_img = bomber_img.resize((800, 400))
    image.paste(bomber_img, (140, 450))
except Exception as e:
    print(f"Failed to download or paste image: {e}")

image.save('b2_spirit_poster.png')
print("Successfully generated b2_spirit_poster.png")
