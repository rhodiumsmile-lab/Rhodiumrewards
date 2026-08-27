import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

root = r'C:\Users\a\Desktop\RewardApp'
out_path = os.path.join(root, 'app', 'app_icon_512.png')

img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
for y in range(512):
    for x in range(512):
        nx = x / 511.0
        ny = y / 511.0
        r = int(8 + 60 * nx + 22 * ny)
        g = int(18 + 30 * nx + 22 * ny)
        b = int(34 + 60 * nx + 38 * ny)
        img.putpixel((x, y), (r, g, b, 255))

# soft glow
boost = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
d = ImageDraw.Draw(boost)
d.ellipse((26, 26, 486, 486), fill=(20, 32, 64, 255))
img = Image.alpha_composite(img, boost.filter(ImageFilter.GaussianBlur(18)))

# main rounded square
container = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
cd = ImageDraw.Draw(container)
cd.rounded_rectangle((36, 36, 476, 476), radius=134, fill=(14, 20, 42, 255))
cd.rounded_rectangle((54, 54, 458, 458), radius=122, outline=(246, 202, 78, 255), width=12)
img = Image.alpha_composite(img, container)

# gold inner badge
badge = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
bd = ImageDraw.Draw(badge)
cx, cy = 256, 256
rad = 150
bd.ellipse((cx - rad, cy - rad, cx + rad, cy + rad), fill=(240, 190, 72, 255))
bd.ellipse((cx - rad + 24, cy - rad + 24, cx + rad - 24, cy + rad - 24), fill=(18, 24, 42, 255))
img = Image.alpha_composite(img, badge)

# purple ribbon behind monogram
ribbon = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
rd = ImageDraw.Draw(ribbon)
rd.rounded_rectangle((166, 182, 346, 330), radius=30, fill=(136, 92, 246, 255))
img = Image.alpha_composite(img, ribbon)

# letter R
font_path = r'C:\Windows\Fonts\segoeui.ttf'
try:
    font = ImageFont.truetype(font_path, 200)
except Exception:
    font = ImageFont.load_default()
text = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
td = ImageDraw.Draw(text)
td.text((256, 256), 'R', font=font, anchor='mm', fill=(255, 255, 255, 255))
img = Image.alpha_composite(img, text)

# sparkle star
star = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
sd = ImageDraw.Draw(star)
points = [(398, 110), (415, 136), (445, 136), (425, 158), (438, 186), (398, 168), (358, 186), (371, 158), (351, 136), (381, 136)]
sd.polygon(points, fill=(255, 214, 92, 255))
img = Image.alpha_composite(img, star)

# highlight sheen
shine = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
shd = ImageDraw.Draw(shine)
shd.rounded_rectangle((70, 70, 440, 220), radius=80, fill=(255, 255, 255, 40))
img = Image.alpha_composite(img, shine)

img.save(out_path, format='PNG')
print(out_path)
print(os.path.getsize(out_path))
