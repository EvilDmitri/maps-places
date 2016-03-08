-------------------------------------------
$ sudo pip install virtualenv
$ sudo easy_install virtualenv

Debian, Ubuntu:
$ sudo apt-get install python-virtualenv

FreeBSD:
$ cd /usr/ports/evel/py-virtualenv
$ make install clean
--------------------------------------------

create virtual environment path
:
mkdir ~/venv && cd ~/venv
--------------------------------------------

create virtual environment:
virtualenv --no-site-packages maps-places

-------------------------------------------

activate:
source ~/venv/maps-places/bin/activate

-------------------------------------------

install libraries:
pip install -r requirements.txt

-------------------------------------------

run  (absolute path):
~/venv/maps-places/bin/python 1.py
