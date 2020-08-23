from pathlib import Path

print("====== Following lines are from underscore_vars.py ========\n")

cwd = Path.cwd().resolve()
# this is command line working directory where you run the script
print(f"Current working directory: {cwd}")

curr_file_abs_path = Path(__file__).resolve()
# this will gives you the absolute path of this file no matter what
print(f"Current file path: {curr_file_abs_path}")

print(f"Variable '__file__': {__file__}")
# this will print out relative path of this file if being run directly
# and it will print out absolute path of this file

print(f"Variable '__package__': {__package__}")
# this will print out the package name if this is part of a package

print(f"Variable '__name__': {__name__}")
# this will print out "__main__" if you run this file directly
# and it will print out the module name "underscore_vars" if this file is imported to other file.

print("\n======= Above lines are from underscore_vars.py ===========\n")
