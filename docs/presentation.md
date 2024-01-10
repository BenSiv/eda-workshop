---
author: Ben Sivan
marp: true
theme: uncover
backgroundImage: url("images/background.png")
# marp presentation.md --output presentation.pdf --allow-local-files
---

# How To Dev
## Workshop

---

## Core Idea

---

## Core Idea
![width:30.2px height:25.2px](images/cocoa-bean.png) Software is messy, especially when distributed.

---

## Greatest compliment

---

## Greatest compliment
![width:30.2px height:25.2px](images/cocoa-bean.png) It just works!

---

## What breaks programs?

---

## What breaks programs?
![width:30.2px height:25.2px](images/cocoa-bean.png) Code

---

## What breaks programs?
![width:30.2px height:25.2px](images/cocoa-bean.png) Code
![width:30.2px height:25.2px](images/cocoa-bean.png) Environment

---

## Development enablers

---

## Development enablers
![width:30.2px height:25.2px](images/cocoa-bean.png) Code

---

## Development enablers
![width:30.2px height:25.2px](images/cocoa-bean.png) Code - Version control system

---

## Development enablers
![width:30.2px height:25.2px](images/cocoa-bean.png) Code - Version control system - **Git**

---

## Development enablers
![width:30.2px height:25.2px](images/cocoa-bean.png) Code - Version control system - **Git**
![width:30.2px height:25.2px](images/cocoa-bean.png) Environment

---

## Development enablers
![width:30.2px height:25.2px](images/cocoa-bean.png) Code - Version control system - **Git**
![width:30.2px height:25.2px](images/cocoa-bean.png) Environment - Containerized environment

---

## Development enablers
![width:30.2px height:25.2px](images/cocoa-bean.png) Code - Version control system - **Git**
![width:30.2px height:25.2px](images/cocoa-bean.png) Environment - Containerized environment - **Docker**

---

## Development enablers
![width:30.2px height:25.2px](images/cocoa-bean.png) **Git**
![width:30.2px height:25.2px](images/cocoa-bean.png) **Docker**

---

## Development enablers
![width:30.2px height:25.2px](images/cocoa-bean.png) **Linux**
![width:30.2px height:25.2px](images/cocoa-bean.png) **Git**
![width:30.2px height:25.2px](images/cocoa-bean.png) **Docker**

---

## Linux
![](images/tux.png)

---

## Linux
![width:30.2px height:25.2px](images/cocoa-bean.png) Most computations runs on **servers**

---

## Linux
![width:30.2px height:25.2px](images/cocoa-bean.png) Most computations runs on **servers**
![width:30.2px height:25.2px](images/cocoa-bean.png) Most **servers** runs **Linux** 

---

## Linux
![width:30.2px height:25.2px](images/cocoa-bean.png) Most computations runs on **servers**
![width:30.2px height:25.2px](images/cocoa-bean.png) Most **servers** runs **Linux** 
![width:30.2px height:25.2px](images/cocoa-bean.png) Most effective in resources

---

## Linux
![width:30.2px height:25.2px](images/cocoa-bean.png) Most computations runs on **servers**
![width:30.2px height:25.2px](images/cocoa-bean.png) Most **servers** runs **Linux** 
![width:30.2px height:25.2px](images/cocoa-bean.png) Most effective in resources
![width:30.2px height:25.2px](images/cocoa-bean.png) **Linux** philosophy

---

## Linux
### Linux Philosophy

---

## Linux
### Linux Philosophy
![width:30.2px height:25.2px](images/cocoa-bean.png) Do only one thing

---

## Linux
### Linux Philosophy
![width:30.2px height:25.2px](images/cocoa-bean.png) Do only one thing
![width:30.2px height:25.2px](images/cocoa-bean.png) And do it well

---

## Linux
### Linux Philosophy
#### In practice

---

## Linux
### Linux Philosophy
#### In practice
![width:30.2px height:25.2px](images/cocoa-bean.png) Built out of tiny independent programs

---

## Linux
### Linux Philosophy
#### In practice
![width:30.2px height:25.2px](images/cocoa-bean.png) Built out of tiny independent programs
![width:30.2px height:25.2px](images/cocoa-bean.png) Productive terminal environment

---

## Linux
![width:30.2px height:25.2px](images/cocoa-bean.png) Fill at **~** in the **$**

---

## Linux
![width:30.2px height:25.2px](images/cocoa-bean.png) Fill at **~** in the **$**
![width:30.2px height:25.2px](images/cocoa-bean.png) Fill at **home** in the **terminal** (shell)

---

## Linux
![width:30.2px height:25.2px](images/cocoa-bean.png) This is the **/** of the problem

---

## Linux
![width:30.2px height:25.2px](images/cocoa-bean.png) This is the **/** of the problem
![width:30.2px height:25.2px](images/cocoa-bean.png) This is the **root** of the problem

---

## Linux
![width:30.2px height:25.2px](images/cocoa-bean.png) What is going on **.** ?

---

## Linux
![width:30.2px height:25.2px](images/cocoa-bean.png) What is going on **.** ?
![width:30.2px height:25.2px](images/cocoa-bean.png) What is going on **here** ?

---

## Linux
![width:30.2px height:25.2px](images/cocoa-bean.png) My **~** is at **/home/user/**

---

## Linux
![width:30.2px height:25.2px](images/cocoa-bean.png) Where have you **bin/** ?

---

## Linux
![width:30.2px height:25.2px](images/cocoa-bean.png) Where have you **bin/** ?
![width:30.2px height:25.2px](images/cocoa-bean.png) Directory structure:
**/bin /home /opt /tmp /usr /var /etc** 

---

## Linux
![width:30.2px height:25.2px](images/cocoa-bean.png) Don't **Bash** your head against the keyboard

---

## Linux
![width:30.2px height:25.2px](images/cocoa-bean.png) You don't need to say goodbye to your Windows machine **WSL** to the rescue

---

## Linux
### Hands-on!

---

## Linux
### Hands-on keyboard!

---

## Linux
### Hands-on keyboard!
![width:30.2px height:25.2px](images/cocoa-bean.png) Go to cmd

---

## Linux
### Hands-on keyboard!
![width:30.2px height:25.2px](images/cocoa-bean.png) Go to cmd
```ssh -i how-to-dev_key.pem howtodev@172.160.226.208```

---

## Linux
### Utilities

---

## Linux
### Utilities
```bash
ls
```
List all files in a directory

---

## Linux
### Utilities
```bash
cd
```
Change directory

---

## Linux
### Utilities
```bash
cat
less
```
Show content of file

---

## Linux
### Utilities
```bash
touch
cp
mv
```
Make, copy, move or rename files

---

## Linux
### Utilities
```bash
mkdir
```
Make a directory

---

## Git

---

## Git
![width:1000px height:463.5px](images/git_diagram.png)

---

## Git
```bash
mkdir <dir_name>
```

---

## Git
```bash
mkdir <dir_name>
git init .
```

---

## Git
```bash
mkdir <dir_name>
git init .
git status
```

---

## Git
```bash
nano <file_name>
echo <content> > <file_name>
```
Enter some content to a file.

---

## Git
```bash
nano <file_name>
echo <content> > <file_name>
git status
```

---

## Git
```bash
nano <file_name>
echo <content> > <file_name>
git status
git add <file_name>
```

---

## Git
```bash
nano <file_name>
echo <content> > <file_name>
git status
git add <file_name>
git status
```

---

## Git
```bash
nano <file_name>
echo <content> > <file_name>
git status
git add <file_name>
git status
git commit -m "some commit message"
```

---

## Docker
![width:360px height:214px](images/docker.png)

---

## Docker
![](images/docker_schema.png)

---

## Docker
```bash
docker build --tag "how-to-dev" .
```
Building a new docker image based on the 'Dockerfile' in the current directory.

---

## Docker
```bash
docker image list
```
```
REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
how-to-dev   latest    d211d6bfa5ab   About a minute ago   202MB
```

---

## Docker
```bash
docker run --interactive --tty --name <my_name> how-to-dev bash
```

---

## Docker
```bash
docker run -it --name <my_name> how-to-dev bash
```

---

## Docker
```bash
docker container list
docker container list --all
```

---

## Docker
```bash
docker run \
    -tty \
    --detach \
    --name <my_name> \
    how-to-dev \
    bash
```

---

## Docker
```bash
docker container list
docker container list --all
```

---

## Docker
```bash
docker exec -t <my_name> bash -c "ls"
```

---

# Bye

**Ben Sivan**
Data Scientist
![width:500px height:10px](images/line.png)
+972-546925522
ben.sivan@celleste-bio.com
