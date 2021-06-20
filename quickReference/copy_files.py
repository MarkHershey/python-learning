import os
import shutil
from pathlib import Path

# from shutil import copytree, ignore_patterns

# copytree(source, destination, ignore=ignore_patterns("*.pyc", "tmp*"))


license = Path("/Users/mark/Documents/CODE/python-learning/LICENSE")

if license.exists():
    print("license exists")


target = Path("/Users/mark/Documents/CODE/python-learning/testing/test/")


def copy_file_to_folder(src_file: Path, dst_folder: Path):
    if dst_folder.exists() and dst_folder.is_dir():
        shutil.copy(src_file, dst_folder)
    elif dst_folder.exists() and dst_folder.is_file():
        print("Warning: Going to Overwrite existing file.")
    elif not dst_folder.exists():
        # os.makedirs can make multiple level of non-existing directories at once
        # while os.mkdir only can make a new directory at first level
        os.makedirs(dst_folder)
        # shutil copy can create a new directory at first level
        # but not multiple levels
        shutil.copy(src_file, dst_folder)


def copy_folder_to_folder(src: Path, dst: Path, overwrite=False):
    ignore_pyc = shutil.ignore_patterns("*.pyc", "__pycache__")

    if src.exists() and src.is_dir():
        if dst.exists() and dst.is_dir():
            if overwrite:
                shutil.rmtree(dst)
            print("Warning: Going to Overwrite existing folder.")
            shutil.copytree(src, dst, ignore=ignore_pyc)
        else:
            print("dst does not exists")
            shutil.copytree(src, dst, ignore=ignore_pyc)
            # copytree copies the content from the src folder to a non-existing dst_folder
            # src folder name is not retained
    else:
        print("invalid src")


def copy_to_folder(src: Path, dst: Path, overwrite=False):

    ignore_pyc = shutil.ignore_patterns("*.pyc", "__pycache__", "venv")
    src = Path(src)
    dst = Path(dst)

    if not src.exists():
        raise ValueError("Source path does not exists.")

    if src.is_file():
        if dst.exists() and dst.is_dir():
            shutil.copy(src, dst)
        elif dst.exists() and not dst.is_dir():
            raise ValueError("Destination path is not a folder but a file")
        else:
            os.makedirs(dst)
            # call itself again to check if destination folder has been created
            # this is to prevent dst provided is a non-existing file path
            copy_to_folder(src, dst)

    elif src.is_dir():
        if dst.exists() and dst.is_dir():
            if overwrite:
                shutil.rmtree(dst)
                print("Overwriting existing folder.")
                shutil.copytree(src, dst, ignore=ignore_pyc)
            else:
                raise Exception("Destination path already exist.")
        elif dst.exists() and not dst.is_dir():
            if overwrite:
                print("Removing existing file.")
                os.remove(dst)
                copy_to_folder(src, dst)
            else:
                raise Exception("Cannot copy a folder's content to a file path")
        else:
            shutil.copytree(src, dst, ignore=ignore_pyc)


if __name__ == "__main__":

    src = Path("/Users/mark/Documents/CODE/python-learning/testing")
    # print(os.path.basename(src))
    dst = Path("/Users/mark/Documents/CODE/python-learning/testing2")
    copy_to_folder(license, dst, overwrite=False)


###

###


###
