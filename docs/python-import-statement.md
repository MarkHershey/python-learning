# Python Import Statement

## Relative Import & Absolute Import - PEP 328

> Module: Every python file can be called a module.
>
> Package: A module or a set of module packaged for release.


When we import a python module into current file, we usually use:

```python
import foo
```

This module `foo` can be:
1. A python built-in module.
2. An installed package using pip. ()
3. Your python module / file located in the same folder as the current file.


Hence, this causes some ambiguity, because your own module file name may accidentally clash with an installed package name.

To avoid this, [PEP 328](https://www.python.org/dev/peps/pep-0328/) was introduced.

Now, if you want to import from a python file/ module located at the same level as your current file, you should do a relative import:
```python
import .foo
from . import foo
```
If you want to import from a python file/ module located in the same package, but one level above, you can use:
```python
import ..bar
from .. import bar
```
one dot `.` represents current directory, two dot `..` represents one level above the current directory, so on and so forth.

Any import statement without using dot notation will be regard as Absolute import, hence, python interpreter will only look for the module from `sys.path` but not from the same package.
```python
import foo
```
