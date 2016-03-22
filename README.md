-------------------------------------------
$ sudo pip install virtualenv
$ sudo easy_install virtualenv

Debian, Ubuntu:
--------------------------------------------
$ sudo apt-get install python-virtualenv

FreeBSD:
--------------------------------------------
$ cd /usr/ports/evel/py-virtualenv
$ make install clean


Go to application folder
--------------------------------------------
cd my_project_folder


create virtual environment:
-------------------------------------------
virtualenv --no-site-packages maps-places


activate:
-------------------------------------------
Linux: source maps-places/bin/activate
Windows: maps-places\Scripts\activate


install libraries:
-------------------------------------------
pip install -r requirements.txt


Exit virtual environment
-------------------------------------------
deactivate


Usage:
-------------------------------------------
maps-places/bin/python script.py -q "some query" -l "{'lat': 41.0, 'lng': -74.0}" -r "radius"
