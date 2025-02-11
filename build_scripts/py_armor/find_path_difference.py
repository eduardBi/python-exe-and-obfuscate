import os

def find_path_difference(path1: str, path2: str) -> str:
    """Compares two file paths and returns the differing ending portion as a clean string."""
    norm_path1 = os.path.normpath(path1).split(os.sep)
    norm_path2 = os.path.normpath(path2).split(os.sep)
    
    # Find the first index where the paths differ
    min_length = min(len(norm_path1), len(norm_path2))
    diff_index = next((i for i in range(min_length) if norm_path1[i] != norm_path2[i]), min_length)
    
    # Extract the differing portion from both paths
    diff_part1 = norm_path1[diff_index:]
    diff_part2 = norm_path2[diff_index:]
    
    return "/".join(diff_part1) if diff_part1 else "/".join(diff_part2)
