-------------------------------------------
$ sudo pip install virtualenv
$ sudo easy_install virtualenv

Debian, Ubuntu:
$ sudo apt-get install python-virtualenv

FreeBSD:
$ cd /usr/ports/evel/py-virtualenv
$ make install clean
--------------------------------------------

cd my_project_folder
--------------------------------------------

create virtual environment:
virtualenv --no-site-packages maps-places
-------------------------------------------

activate:
source /maps-places/bin/activate
-------------------------------------------

install libraries:
pip install -r requirements.txt
-------------------------------------------

deactivate
-------------------------------------------


run  (absolute path):
~/venv/maps-places/bin/python 1.py
-------------------------------------------
