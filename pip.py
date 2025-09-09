from PIL import Image

# Open the image
image = Image.open('logo.png')

# Make the image background transparent
image = image.convert("RGBA")

# Create a mask for the white pixels and make them transparent
data = image.getdata()

new_data = []
for item in data:
    # Change all white (also shades of whites) pixels to transparent
    if item[0] > 200 and item[1] > 200 and item[2] > 200:
        new_data.append((255, 255, 255, 0))  # Transparent
    else:
        new_data.append(item)

# Update image with the new data
image.putdata(new_data)

# Save the image as a PNG file with transparency
image.save('path_to_save_your_image_transparent.png', 'PNG')
