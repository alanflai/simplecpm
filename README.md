# simplecpm
Simple python script for project's critical path evluation.
The script inlcudes an example project's network diagram and
evaluates its lenght.

# Dependencies
The script uses the open source criticalpath's packages.
Its reference is: https://pypi.org/project/critical-path/
# How to execute
The script has been developd with Python 3.10.
First check your python version installation.
Then, if it'ok, clone the project.

Change the current directory

> cd ./simplecpm

Creates a virtualenv

> python -m venv venv

Then activate (the following command for Windows system)

> .\venv\Scripts|activates

Then Install the dependencies

> pip install -r .\requirements.txt -v

Then execute from the commandline:

> python simplecpm.py

If see as output printed the Critical Path node's list and the length, then the script has completed with success.

To create an executable file, use the following command:

> pyinstaller -F simplecpm.py

If there aren't error, the executable file will be available into the .\dist folder.

Try to execute:

> .\dist\simplecpm.exe
# Useful links

(1) Critical Path Method [Wikipedia]
URL: https://en.wikipedia.org/wiki/Critical_path_method
