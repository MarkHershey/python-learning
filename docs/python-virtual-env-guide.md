# Python Virtual Environment Guide

#### Why do we need virtual environment for Python?

1. Virtual environment provides each project its own set of dependencies/ packages, so that you can use different versions of dependencies for different projects.
2. Virtual environment makes it easier for you to manage dependencies and share your project environment requirements with others. 

#### Step 0: Check if your Python and Pip are Installed Properly

#### Step 1: Install `virtualenv`

```
pip install virtualenv
```
Verify your install and its version

```
virtualenv --version
```

#### Step 2: Install `virtualenvwrapper`

```
pip install virtualenvwrapper
```
#### Step 3: Configure `virtualenvwrapper`

##### Step 3.1 Open your Shell Startup File

Depends on which shell you are using:

- bash
- ksh
- zsh

If you are using Bash Shell, open the`.profile` file using nano.

```
nano ~/.profile
```
If you are using ZSH or Z Shell, open the`.zprofile` file using nano.

```
nano ~/.zprofile
```
##### Step 3.2 Set Variables for `virtualenvwrapper`

Add the following line at the bottom of the file you have opened.

```
# virtualenv and virtualenvwrapper

# set home folder for virtual environments
export WORKON_HOME=$HOME/.virtualenvs

# set python location for VIRTUALENVWRAPPER
export VIRTUALENVWRAPPER_PYTHON=usr/bin/python3

# set virtualenv location for VIRTUALENVWRAPPER
export VIRTUALENVWRAPPER_VIRTUALENV=/home/mark/.local/bin/virtualenv

source /usr/local/bin/virtualenvwrapper.sh
```
Technical Details:
 
- The variable `WORKON_HOME` tells virtualenvwrapper where to place your virtual environments. The default is `$HOME/.virtualenvs`. If the directory does not exist when virtualenvwrapper is loaded, it will be created automatically.
- The variable `PROJECT_HOME` tells virtualenvwrapper where to place your project working directories. The variable must be set and the directory created before `mkproject` is used.
- During startup, `virtualenvwrapper.sh` finds the first python and virtualenv programs on the `$PATH` and remembers them to use later. This eliminates any conflict as the `$PATH` changes, enabling interpreters inside virtual environments where virtualenvwrapper is not installed or where different versions of virtualenv are installed. Because of this behavior, it is important for the `$PATH` to be set before sourcing `virtualenvwrapper.sh`. 
- To override the `$PATH` search, set the variable `VIRTUALENVWRAPPER_PYTHON` to the full path of the interpreter to use and `VIRTUALENVWRAPPER_VIRTUALENV` to the full path of the `virtualenv` binary to use. Both variables must be set before sourcing `virtualenvwrapper.sh`.

##### Step 3.3 Save and Exit the Nano Editor.

```
Control + x
y
Enter
```

##### Step 3.4 Reload the Shell Startup File

```
source ~/.profile
```
or

```
source ~/.zprofile
```

#### Step 4: Create Virtual Environment

Navigate to your project folder

```
cd ~/project/folder/
```

Create a virtual environment called venv (or any name of your choice)

```
mkvirtualenv venv -p python3
```
Exit Virtual Environment 

```
deactivate
```

Enter Virtual Environment

```
workon venv
```

Remove / Delete a Virtual Environment 

```
rmvirtualenv venv
```

List All Virtual Environments

```
workon
```

#### Step 5: Freeze & Share Your Environment Requirements

To “freeze” the current state of the environment packages

```
pip freeze > requirements.txt
```

To restore the environment (install all the packages in another machine for this project)

```
pip install -r requirements.txt
```

### References

- [Virtualenvwrapper Command Reference](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html)
- [The Hitchhiker's Guide to Python: Pipenv & Virtual Environments](https://docs.python-guide.org/dev/virtualenvs/)