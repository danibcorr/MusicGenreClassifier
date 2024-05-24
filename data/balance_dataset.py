# %% Libraries

import os
import random

# %% Functions

def balance_dataset(input_dir: str) -> None:
    """
    Balance the dataset by reducing the number of samples in each category to match the category with the fewest samples.

    Args:
        input_dir (str): The directory containing the audio files to process

    Returns:
        None
    """
    genre_counts = {}

    # Count the number of samples in each genre
    for genre in os.listdir(input_dir):
        genre_path = os.path.join(input_dir, genre)
        if os.path.isdir(genre_path):
            genre_counts[genre] = len([f for f in os.listdir(genre_path) if os.path.isfile(os.path.join(genre_path, f)) and f.endswith(('.png'))])

    # Print the genre counts for debugging
    print(f"Genre counts before balancing: {genre_counts}")

    # Find the minimum sample count
    min_count = min(genre_counts.values())
    print(f"Minimum sample count across genres: {min_count}")
    
    # Balance each genre
    for genre, count in genre_counts.items():
        if count > min_count:
            genre_path = os.path.join(input_dir, genre)
            files = [f for f in os.listdir(genre_path) if os.path.isfile(os.path.join(genre_path, f)) and f.endswith(('.png'))]
            print(f"Balancing genre '{genre}' with {count} files")
            files_to_remove = random.sample(files, count - min_count)
            for f in files_to_remove:
                file_path = os.path.join(genre_path, f)
                os.remove(file_path)
                print(f"Removed {file_path}")

    # Print the genre counts after balancing for debugging
    genre_counts_after = {}
    for genre in os.listdir(input_dir):
        genre_path = os.path.join(input_dir, genre)
        if os.path.isdir(genre_path):
            genre_counts_after[genre] = len([f for f in os.listdir(genre_path) if os.path.isfile(os.path.join(genre_path, f)) and f.endswith(('.png'))])
    print(f"Genre counts after balancing: {genre_counts_after}")

# %% Main

if __name__ == '__main__':
    
    input_dir = 'dataset/'
    balance_dataset(input_dir)
