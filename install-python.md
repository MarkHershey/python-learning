# How to Install Vanilla Python on macOS Properly?



### Note at the beginning:

1. Do NOT remove Apple-supplied system Python 2.7.x (whatever version that is), as it may break the whole operating system. 




### Vanilla Install Python 


What to be installed:

- `Homebrew`: a package manager targeted at macOS. Similar to Apt for Linux. 
- `Pip`: a package manager for the python world, installing python packages with pip will fetch packages from the Python Package Index.
- `Python 3`

#### Step 0: Remove existing 3rd party Python

```
sudo rm -rf /Library/Frameworks/Python.framework/Versions/2.7
```
```
sudo rm -rf "/Applications/Python 2.7"
```



#### Step 1: Install Homebrew

Open Terminal on your Mac and paste in the following command and hit Enter. 

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

#### Step 2: Install Python using Homewbrew

```
brew install python
```


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