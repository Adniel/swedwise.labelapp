Install
=======
Install Python 2.7
Create directory for label application
Inside the directory run:
$ virtualenv --no-site-packages venv

Run:
$ ./venv/bin/pip install pyramid
$ ./venv/bin/pip install reportlab

Run application by using:
$ ./venv/bin/python application.py

Set up supervisor according to documentation