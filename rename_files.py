import os

def traverse_dir(input_dir, new_name):
    files = os.listdir(input_dir)
    episode_count = 1

    for file in sorted(files):
        og_path = os.path.join(input_dir, file)
        file_extension = os.path.splitext(file)[1]

        count_str = f"{episode_count:02}"

        new_filename = f"{new_name}{count_str}{file_extension}" 
        new_path = os.path.join(input_dir, new_filename)

        if os.path.exists(new_path):
            print(f"The file {file} will not be overwritten")
            continue
        
        os.rename(og_path, new_path)
        episode_count += 1
        
def new_filenames():
    print("Enter the show name:")
    show_name = input().strip().replace(" ", ".")
    show_name = show_name + ".S"

    print("Enter the season number:")
    season_number = input().strip()
    season_number = season_number + ".E"

    new_name = show_name + season_number
    return new_name

def main():
    print("Starting file renaming process...")
    input_dir = input("Enter path to directory: ").strip('"').strip("'")

    if not os.path.exists(input_dir):
        print(f"The directory {input_dir} does not exist.")
    else:
        new_name = new_filenames()
        traverse_dir(input_dir, new_name)

    print("File renaming process completed.")

if __name__ == "__main__":
    main()
