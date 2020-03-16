# How to Install Python, Pip, Virtualenv, and Virtualenvwrapper on Linux?

> This guide is written based on Ubuntu 18.04.4 LTS

```
sudo apt update
sudo apt upgrade
```

```
python3 -V
which python3
```

```
>>> Python 3.6.9
>>> /usr/bin/python3
```


```
sudo apt install python3-pip
pip3 -V
```

```
>>> pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
```


```
sudo apt-get install virtualenv
sudo apt-get install virtualenvwrapper
```

```
sudo nano ~/.zshrc
```

```
#####################################################
# virtualenv and virtualenvwrapper

# set home folder for virtual environments
export WORKON_HOME=$HOME/.virtualenvs

# set python location for VIRTUALENVWRAPPER
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3

# set virtualenv location for VIRTUALENVWRAPPER
export VIRTUALENVWRAPPER_VIRTUALENV=$HOME/.local/bin/virtualenv

source $HOME/.local/bin/virtualenvwrapper.sh
#####################################################
```

```
source ~/.zshrc
```
