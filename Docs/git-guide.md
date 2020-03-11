
# Git 101


### Git & GitHub

GitHub and Git are two separated things.

- Git is open-source software that helps you manage code versions, it does not have a graphical interface, so you can't really see the "software", but you can use git command in your terminal/ shell using the command line.
- GitHub is an online platform developed by a company, the company is acquired by Microsoft in 2018, so now it is under Microsoft. Github, the platform, provides free hosting service for repositories, which usually contains code or text files. It also enables collaboration on projects, since the repository is hosted on the cloud (actually in some server owned by Github) so that teams can collaborate in remote locations, but accessing the same repository. In summary, GitHub is a service that is built around git, making git more convenient and powerful for programmers.

### Using GitHub

1. Create a GitHub account
2. Create a repo on GitHub
3. Initiate your repo with a `README.md` file
4. Clone your own repo to local
5. Create a new file / make changes to your files
6. Stage your changes
7. Commit Changes
8. Push commits to Github

### Git Clone a Repository
"Clone" means copy or download a remote repository to your local machine.

- Clone a repository does not affect the original repository in any way, since you just make a copy only.
- You can clone your own repository and others' repository, basically any public repository.
- If you are cloning your own private repository, you will be required to log into your Github account after you key in the clone command.  

If you don't know how to use Git command, follow this Step-by-step guide:

0. Copy the repository git url from the GitHub repository page.
1. Create a new folder on your machine at your desired directory.
2. Open your Terminal / Shell on your machine.
3. Use command line to navigate into the folder you just created.
4. key in the following git command, which is `git clone` and paste in the repository url you just copyed in the first step.
5. press `Enter` key, the repository will be downloaded within a few seconds.

Git command:
`git clone + [Github Repository git URL]`

Example:

```
git clone https://github.com/MarkHershey/python-learning.git
```

### Git Stage Changes

```
git add [filename]
```

```
git add --a
```


### Git Commit Changes

```
git commit [filename] -m 'commit message'
```

```
git commit -a -m 'commit message'
```

### Git Push
```
git push
```

```
git push <remote> <branch>
```

### Git Fetch

### Git Merge


### Git Pull
```
git pull
```


### Git Branch


### Collaboration

#### Contribute to a project where you have collaborator access

If you have collaborator permissions on a repository, you can create a branch off of the repository's default branch so you can safely experiment with changes.

#### Contribute to a project where you don't have write access

To contribute to a project where you don't have write access, you can use GitHub Desktop to create a fork of the repository. Changes on your fork don't affect the original repository. You can commit changes on your fork, then open a pull request to the original repository with your proposed changes.


---

#### How to unstage a changed file

#### How to remove a file from repository

#### How to let git ignore certain files
