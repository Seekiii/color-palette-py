from colorthief import ColorThief
import webcolors as wc

img = ColorThief("img.png")
_rgb = img.get_palette()

colors = []
for i in _rgb:
	colors.append(wc.rgb_to_hex(i))

print(colors)