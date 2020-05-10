
# Get Started with Git & GitHub

## What is the difference between Git and GitHub?

#### Short version:
- **Git** is a version management software that manages your local git repositories.
- **GitHub** is an online hosting service for your git repositories.

#### Long version:
- **Git** is open-source software that helps you manage code versions, it does not have a graphical interface, so you can't really "see" the software, but you can use git commands in your terminal/ shell to interact with it.
- **GitHub** is an online platform developed by a company and then acquired by Microsoft in 2018. Github, the platform, provides free hosting service for git repositories, which usually contains code or text files. It also enables collaboration on projects, since the repository is hosted on the cloud, teams can collaborate on the project repository from different locations. GitHub is an online service that is built around git, making git more convenient and powerful for programmers especially teams.


## Download Git

#### For macOS:

Just run the following command in your terminal to check your git version, it will prompt you to install Git if you don't have it.
```
git --version
```

#### For Other Operating Systems:

Refer to: [Getting Started Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Configure Git

#### Setting up Git username and email address
Just letting Git know who you are. If you already have a GitHub account, keep the username and the email address for your Git the same as your GitHub account.

- To check current username and email address for Git.
- It returns nothing if no name/email has been set.

```
git config --global user.name
git config --global user.email

```

- To set username and email address for Git.
- `--global` means to set for all the repositories on your machine.

```
git config --global user.name "Tom Cruise"
git config --global user.email "tom@example.com"

```


## Work with local Git repositories

#### `git init`
#### `git add`
#### `git help <git command>`
#### `git status`
#### `git log --all --graph --decorate`
#### `git commit`
#### `git commit -a`
Tell the command to automatically stage files that have been modified and deleted, but new files you have not told Git about are not affected.

#### `git commit -m "Your commit message"`

#### `git branch`
#### `git branch -vv`




#### `git checkout <hash string>`
#### `git checkout master`


## Work with remote Git repositories


### Get started with GitHub

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
4. key in the following git command, which is `git clone` and paste in the repository url you just copied in the first step.
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


## Collaboration

#### Contribute to a project where you have collaborator access

If you have collaborator permissions on a repository, you can create a branch off of the repository's default branch so you can safely experiment with changes.

#### Contribute to a project where you don't have write access

To contribute to a project where you don't have write access, you can use GitHub Desktop to create a fork of the repository. Changes on your fork don't affect the original repository. You can commit changes on your fork, then open a pull request to the original repository with your proposed changes.


---




#### How to unstage a changed file

#### How to remove a file from repository

#### How to let git ignore certain files
