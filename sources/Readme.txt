# How to config All Requirment for Python Dev Project 

## how to config VENV

## install brew, the package managment software 
you will new to install brew for this 


## install python
*** Need to install python3 using brew for mac 
brew install python3

## install virtual environment 
*** create the Virtual environment
python3.11 -m venv venvMain


*** activate the Virtual environment
source venvTest/bin/activate

## Install the matplotlib for example
**** upgrade pip
pip3 install --upgrade pip

*** install matplotlib
pip3 install matplotlib


### Deactive VENV and Delete

*** Deactivate Just type 
deactivate 

**** Delete folder 
sudo rm -r  vent


### Git to ingore some file that you don't want to track.
Here's how you can ignore files or folders in Git:

Create a file named .gitignore in the root directory of your Git repository. This file will contain the patterns of files or folders you want to ignore.

Open the .gitignore file in a text editor.

Add the file or folder patterns that you want to ignore, each on a new line. You can use wildcards and regular expressions to define patterns. For example, to ignore a file named secret.txt, you can simply add secret.txt to the .gitignore file. To ignore all files with a .log extension, you can add *.log. To ignore an entire folder named logs, you can add logs/.

Save the .gitignore file.

Commit the .gitignore file to your Git repository. This ensures that the patterns specified in the file are applied to your repository.

