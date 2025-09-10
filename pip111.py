
from PIL import Image

# Input/output file names
src = "kroran_cleaned_scaled2x.png"  # change to your file
out = "kroran_cleaned_scaled2x_v2.png"

# Open and ensure RGBA
img = Image.open(src).convert("RGBA")
pixels = img.load()

width, height = img.size

# Loop over all pixels
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        # If pixel is "light" (all channels above 220), remove it
        if r > 220 and g > 220 and b > 220:
            pixels[x, y] = (255, 255, 255, 0)  # transparent

# Scale 2x
scaled = img.resize((width * 2, height * 2), Image.Resampling.LANCZOS)

# Save output
scaled.save(out, "PNG")

print(f"Saved cleaned image as {out}")
