from pathlib import Path

import underscore_vars

cwd = Path.cwd().resolve()
print(f"Current working directory: {cwd}")

curr_file_abs_path = Path(__file__).resolve()
print(f"Current file path: {curr_file_abs_path}")

print(f"Variable '__file__': {__file__}")

print(f"Variable '__package__': {__package__}")

print(f"Variable '__name__': {__name__}")
