# Frequently-used Linux Commands

Print

```
echo
```


Print content of file

```
cat example.json
```

Secure copy 

```
scp [local file] [remote user]@[remote address]:[remote path]

scp example.json root@178.128.22.33:/home/root/example
```

create folder

```
mkdir new_folder
```

list all file with details (inc. hidden files)

```
ls -la
```

change owner for all files inside a folder

```
sudo chown -R username:username [folder]
```

update all packages

```
sudo apt update
sudo apt upgrade
```

