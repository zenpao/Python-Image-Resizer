from PIL import Image

print("RESIZE IMAGE W/O MAINTAINING ASPECT RATIO\n")

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

# Forcefully resize the image to the specified dimensions (no aspect ratio maintenance)
resized_image = original_image.resize((desired_width, desired_height), Image.Resampling.LANCZOS)

# Save the resized image in the same directory with a new name
resized_image_path = f"{image_path.rsplit('.', 1)[0]}_resizedExact.png"
resized_image.save(resized_image_path)

print(f"\nResized image saved as: {resized_image_path}")
