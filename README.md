Install
=======
Install Python 2.7
Create directory for label application
Inside the directory run:
$ virtualenv --no-site-packages venv

Run:
$ ./venv/bin/pip install pyramid
$ ./venv/bin/pip install reportlab

Make sure there is a folder for temporary label files as referenced in config.py
e g. TEMP_FILE_PATH = './out/'

If you want to keep a copy of the created label in the TEMP_FILE_PATH,
set REMOVE_LABEL_FILES to False, it is set to True by default

Run application by using:
$ ./venv/bin/python application.py

Set up supervisor according to separate documentation