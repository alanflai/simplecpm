# simplecpm
Simple python script for project's critical path evaluation.
The script inlcudes an example project's network diagram and
evaluates its lenght.

# Dependencies
The script uses the open source criticalpath's packages (https://pypi.org/project/critical-path/)
# How to execute
You need a running Python 3.7.3 installation on your environment.
Change to the following directory

> cd ./simplecpm

Creates a virtualenv

> python3 -m venv venv

Activate it (the following command for Windows system)

> source ./venv/bin/activate

Install the dependencies

> pip3 install -r ./requirements.txt -v

Then execute from the commandline:

> python3 simplecpm.py

If everything has gone right, the Critical Path node's list and its length are printed out.

To create an executable file, use the following command:

> pyinstaller -F simplecpm.py

The executable file will be available into the .\dist folder.

Try to execute:

> ./dist/simplecpm
# Useful links

(1) Critical Path Method [Wikipedia]
URL: https://en.wikipedia.org/wiki/Critical_path_method
