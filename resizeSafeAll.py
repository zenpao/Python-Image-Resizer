from PIL import Image
import os

print("RESIZE ALL IMAGES IN A FOLDER WHILE MAINTAINING ASPECT RATIO\n")

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
            resized_image_path = os.path.join(folder_path, f"resizedSafe_image_{index}.png")
            resized_image.save(resized_image_path)

            print(f"\nResized image saved as: {resized_image_path}")

    print("\nAll images processed.")
