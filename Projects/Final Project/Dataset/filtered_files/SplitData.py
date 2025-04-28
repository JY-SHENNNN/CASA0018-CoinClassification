import os
import shutil

# current working directory
root_dir = os.getcwd()


target_coins = [
    "1-Penny_united_kingdom",
    "5-Pence_united_kingdom",
    "10-Pence_united_kingdom",
    "20-Pence_united_kingdom",
    "50-Pence_united_kingdom"
]

# iterate over all files in the current directory
for filename in os.listdir(root_dir):
    file_path = os.path.join(root_dir, filename)

    if not os.path.isfile(file_path):
        continue

    for coin in target_coins:
        if coin in filename:
            # create target folder if not exist
            target_folder = os.path.join(root_dir, coin)
            os.makedirs(target_folder, exist_ok=True)

            # move file to target folder
            dest_path = os.path.join(target_folder, filename)
            shutil.move(file_path, dest_path)
            print(f" moved: {filename} -> {target_folder}")
            break

