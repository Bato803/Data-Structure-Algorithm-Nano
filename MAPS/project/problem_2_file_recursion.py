import os
import pdb

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    res = []
    helper(suffix, path, res)
    return res

def helper(suffix, path, res):
    
    if os.path.isfile(path):
        if path.endswith(suffix):
            res.append(path)
            return 
    
    if os.path.isdir(path):
        for p in os.listdir(path):
            newpath = os.path.join(path, p)
            helper(suffix, newpath, res)

if __name__ == "__main__":
    
    test_path = "./testdir"

    # Test 1: Find files ends with ".c"
    tst1 = find_files(".c", test_path)
    print(f"Test 1: path is {test_path}, result is {tst1}")

    # Test 2: Find files ends with ".gitkeep"
    tst2 = find_files(".gitkeep", test_path)
    print(f"Test 2: path is {test_path}, result is {tst2}")

    # Test 3: Edge case, ends with ".", it should not return anything. 
    tst3 = find_files(".", test_path)
    print(f"Test 3: path is {test_path}, result is {tst3}")
