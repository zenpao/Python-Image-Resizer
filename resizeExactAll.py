from PIL import Image
import os

print("RESIZE ALL IMAGES IN A FOLDER W/O MAINTAINING ASPECT RATIO\n")

# Ask the user for the folder path containing images
folder_path = input("Enter the path to the folder containing images (e.g., /path/to/folder): ")

# Check if the folder exists
if not os.path.exists(folder_path):
    print("The specified folder does not exist. Please check the path and try again.")
else:
    # Ask for the desired size in inches
    desired_width_inches = float(input("\nEnter the desired width in inches: "))
    desired_height_inches = float(input("Enter the desired height in inches: "))

    # Get the DPI for conversion (assume 96 DPI for new images)
    dpi = (96, 96)

    # List all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Check if there are any images to process
    if not image_files:
        print("\nNo image files found in the specified folder.")
    else:
        # Process each image file
        for index, image_file in enumerate(image_files, start=1):
            image_path = os.path.join(folder_path, image_file)

            # Load the original image
            original_image = Image.open(image_path)

            # Convert desired size from inches to pixels
            desired_width = round(desired_width_inches * dpi[0])  # rounds to nearest integer
            desired_height = round(desired_height_inches * dpi[1])  # rounds to nearest integer

            # Forcefully resize the image to the specified dimensions (no aspect ratio maintenance)
            resized_image = original_image.resize((desired_width, desired_height), Image.Resampling.LANCZOS)

            # Save the resized image in the same directory with a new name
            resized_image_path = os.path.join(folder_path, f"resizedExact_image_{index}.png")
            resized_image.save(resized_image_path)

            print(f"\nResized image saved as: {resized_image_path}")

    print("\nAll images processed.")
