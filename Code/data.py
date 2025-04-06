import os
import shutil

# get current working directory
root_dir = os.getcwd()

# taregt folder for filtered images
output_dir = os.path.join(root_dir, "filtered_files")
os.makedirs(output_dir, exist_ok=True)

# the target coins
target_coins = [
    "1-Penny_united_kingdom",
    "5-Pence_united_kingdom",
    "10-Pence_united_kingdom",
    "20-Pence_united_kingdom",
    "50-Pence_united_kingdom"
]

valid_extensions = (".jpg", ".jpeg", ".png")

# iterate through all subfolders and files
for foldername, subfolders, filenames in os.walk(root_dir):
    for filename in filenames:
        # select only images with target coins and valid extensions
        if any(coin in filename for coin in target_coins) and filename.lower().endswith(valid_extensions):
            file_path = os.path.join(foldername, filename)
            new_path = os.path.join(output_dir, filename)

            # move the file to the target folder
            shutil.move(file_path, new_path)
            print(f"moved {file_path} -> {new_path}")

