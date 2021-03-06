# Python Packaging

## Types of packaging method

- Regular packages
- Namespace packages
    - native namespace packages (aka. [PEP 420](https://www.python.org/dev/peps/pep-0420/) packages)
    - pkgutil-style namespace packages
    - pkg_resource-style namespace packages



## File Structure

### Regular Package

Package name is `foo`

```
foo
|____ foo
|     |____ __init__.py
|     |____ bar.py
|____ README.md
|____ requirements.txt
|____ setup.py
```

### Namespace Package

The main purpose of having "Namespace Package" is to make multiple python package share the same namespace. Without using namespace package, the top-level namespace of a python package is the name of the package, but with namespace package, the top-level namespace of a pcakage is usually different from the package name.

Below is an example of two separate python namespace packages named `foo_x` and `foo_y` respectively, they share the same namespace `foo`.

Package name is `foo_x`
Namespace is `foo`

```
foo_x                            # this folder name is arbitrary
|____ foo_x                      # this folder name should be the package name
|     |____ foo                  # this folder name should be the namespace
|           |____ __init__.py
|           |____ bar_x.py
|____ README.md
|____ requirements.txt
|____ setup.py
```

Package name is `foo_y`
Namespace is `foo`

```
foo_y
|____ foo_y
|     |____ foo
|           |____ __init__.py
|           |____ bar_y.py
|____ README.md
|____ requirements.txt
|____ setup.py
```


## Details about `setup.py`

*import setuptools*
```python
from setuptools import setup, find_modules
```

*long_description*
```python
with open("README.md", "r") as f:
    long_description = f.read()

setup(
    ...
    long_description=long_description,
    long_description_content_type="text/markdown",
    ...
)
```

*install_requires*

## Tests

- Pytest
- Tox

## Docs

*Syntax*
- ReStructuredText | `.rst`
    - Sphinx
- MarkDown | `.md`
    - MkDocs

*README*

- Installation
    - Dependencies
- Usage
    - Examples
- Development
    - Installation
    - How to run test
