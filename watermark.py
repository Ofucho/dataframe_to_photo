# Importing the PIL library
from PIL import Image
from PIL import ImageDraw

# Open an Image

img = Image.open('ssudan_eco.png')

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Add Text to an image
I1.text((38, 10), "\u00A9 Colwed", fill=(255, 255, 255, 128))

# Display edited image
img.show()

# Save the edited image
img.save("car2.png")
