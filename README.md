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

Label form can be pre-filled using query string:
	http://localhost:8080/?part_no=55669905&quantity=400&description=Beskrivning&vendor_lot=100&serial=01&po_number=1212&vendor_number=RYD3&date=20051005
and labels can be directly rendered using the very same query string:
	http://localhost:8080/render?part_no=55669905&quantity=400&description=Beskrivning&vendor_lot=100&serial=01&po_number=1212&vendor_number=RYD3&date=20051005

Set up supervisor according to separate documentation