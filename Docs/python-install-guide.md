# How to Install Vanilla Python on macOS Properly?


---
### Note at the beginning:

- Do NOT remove Apple-supplied system Python 2.7.x (whatever version that is), as it may break the whole operating system.


- What is a Vanilla Install?

	>'Vanilla Install' simply means 'not customized from their original form'.

    - What is Anaconda Python?

	>Anaconda is a open-source Python distribution. It aims to provide everything you need (Python-wise) for data science "out of the box".
    >
    >It includes:
    >
    >- The core Python language
    >- 100+ Python "packages" (libraries)
    >- Spyder IDE and Jupyter Notebook
    >- conda, Anaconda's own package manager, used for updating Anaconda and packages
    >
    >[Reference: Matthias Braun](https://stackoverflow.com/a/42096429/8198210)


	- If you think the following guide is overwhelming for you, Anaconda is a good choice for beginners, just head over to [Anaconda distribution](https://www.anaconda.com/distribution/), choose Python 3.X for your operating system, download and install it, and you are good to go.

---

### Vanilla Install Python


What to be installed:

- `Homebrew`: a package manager targeted at macOS. Similar to Apt for Linux.
- `Pip`: a package manager for the python world, installing python packages with pip will fetch packages from the [Python Package Index](https://pypi.org/).
- `Python 3.7.X`

#### Step 0: Remove existing 3rd party Python

##### Step 0.1:
Open Finder, Navigate to`/Applications`, delete any folder named `Python 2.X` or `Python 3.X`.

##### Step 0.2:
1. Open Finder, go to your main Drive, usually `Macintosh HD`
2. Use Finder, navigate to `/Library/Frameworks/Python.framework/Versions/`
3. Delete everything within`/Versions` folder.

Alternatively, if you know what version of Python do you have, let say 3.6, you can use the following command in the Terminal.

```
sudo rm -rf /Library/Frameworks/Python.framework/Versions/3.6
```
##### Step 0.3:
Remove all the symbolic links in`/usr/local/bin` that point to Python related files:

```
sudo rm /usr/local/bin/python*
```
```
sudo rm /usr/local/bin/pip*
```


#### Step 1: Install Homebrew

Open Terminal on your Mac and paste in the following command and hit Enter.

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

#### Step 2: Install Python using Homewbrew
Type this in Terminal and hit Enter.

```
brew install python
```
Homebrew will install Pip as well.

#### Step 3: Change Environment Variable in macOS:

##### Step 3.1

Depends on which shell you are using.

If you are using Bash Shell, open the`.bash_profile` file using nano.

```
nano ~/.bash_profile
```
If you are using ZSH or Z Shell, open the`.zprofile` file using nano.

```
nano ~/.zprofile
```
>GNU nano is a text editor for Unix-like computing systems or operating environments using a command line interface.

##### Step 3.2

Add the following line at the top of the file you have opened.

```
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
```

##### Step 3.3
Save and exit the nano editor.

```
Control + X
Y
Enter
```

##### Step 3.4
Close all Terminal windows and quit Terminal entirely. Open Terminal again, check environment variable by using this command:

```
echo $PATH
```

It should response as follow:

```
/usr/local/opt/python/libexec/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

#### Step 4: Check Python Versions and Pip Versions

```
python --version
```

it should return `Python 3.7.6`

```
pip --version
```
It should return soemthing like this
```
pip 19.3.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)
```
> The Python version 3.7.x should match what pip is pointing at.

#### Step 5: How to Install / Update Python Packages
![Reference](https://miro.medium.com/max/577/1*w-gYboE96IYdDBUDR7QokQ.png)




#### References
- [The Hitchhiker’s Guide to Python: Installing Python 3 on Mac OS X](https://docs.python-guide.org/starting/install3/osx/)
- [Dirk Avery: The Right Way to Set Up Python on Your Mac](https://medium.com/faun/the-right-way-to-set-up-python-on-your-mac-e923ffe8cf8e)
- [Uninstall Python on Mac](https://nektony.com/how-to/uninstall-python-on-mac)
- [How to Modify the Shell Path in macOS Sierra and OSX using Terminal](https://coolestguidesontheplanet.com/add-shell-path-osx/)
- [The right and wrong way to set Python 3 as default on a Mac](https://opensource.com/article/19/5/python-3-default-mac)
