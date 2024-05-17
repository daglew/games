## Games
This is a file describing how to prepare the environment for creating a games application.

## Table of contents
* [Clone repository](#clone-repository-using-git-bash)
* [Installation virtual environment](#installation-virtual-environment-venv)


## Clone repository

1. Clone repository to your local machine use command.
``` 
https://github.com/daglew/games.git
``` 

2. Go to the chatbot folder with the given command.
``` 
cd games/
``` 

3. Installing the virtualenv package
```
python3 -m pip install virtualenv
```

4. Installation of the virtual environment to the .venv file (I can change and substitute this,
will be created in the file where we enforce it
```
python3 -m virtualenv .venv
```
5. Environmental activation
```
source .venv/Scripts/activate
```
6. Install external packages from the location where we call requirements.txt (must be in the same path)
```
pip install -r requirements.txt 
```
7. Execute the given command to open the project.
```
python3 main.py
```
