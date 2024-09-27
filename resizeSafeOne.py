from PIL import Image

print("RESIZE IMAGE WHILE MAINTAINING ASPECT RATIO\n")

# Ask the user for the path of the image
image_path = input("Enter the path to the image (e.g /path/filename.png): ")

# Load the original image
original_image = Image.open(image_path)

# Ask for the desired size in inches
desired_width_inches = float(input("\nEnter the desired width in inches: "))
desired_height_inches = float(input("Enter the desired height in inches: "))

# Get the DPI (dots per inch) of the original image
dpi = original_image.info.get('dpi', (96, 96))  # Default to 96 if DPI info is not available

# Convert desired size from inches to pixels
desired_width = round(desired_width_inches * dpi[0])  # rounds to nearest integer
desired_height = round(desired_height_inches * dpi[1])  # rounds to nearest integer

# Calculate aspect ratio
original_width, original_height = original_image.size
aspect_ratio = original_width / original_height

# Determine the new size maintaining aspect ratio
if aspect_ratio > 1:
    # Landscape orientation
    new_width = desired_width
    new_height = int(desired_width / aspect_ratio)
else:
    # Portrait orientation or square
    new_height = desired_height
    new_width = int(desired_height * aspect_ratio)

# Resize the image using Resampling.LANCZOS
resized_image = original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

# Save the resized image in the same directory with a new name
resized_image_path = f"{image_path.rsplit('.', 1)[0]}_resizedSafe.png"
resized_image.save(resized_image_path)

print(f"\nResized image saved as: {resized_image_path}")
