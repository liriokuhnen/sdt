Shape Discovery Tool
====================

This is a prototype design patterns to get a type of any shape format

# 1 Dependences
  - Python3

### Guide to work with python 3:

Folow those link below to install Python 3, PIP and Virtualenv

[python 3 on Linux](http://docs.python-guide.org/en/latest/starting/install3/linux/ "Install python 3 on linux")
[python 3 on Mac](http://docs.python-guide.org/en/latest/starting/install3/osx/ "Install python 3 on Mac")
[python 3 on Windows](http://docs.python-guide.org/en/latest/starting/install3/win/ "Install python 3 on Windows")

### 2 - Install requirements:

Before to install the requirements for this project you need to create and active your virtualenv.

```
virtualenv -p python3 envname
source envname/bin/activate
```

If you has luck and have the virtualenvwrapper installed just need one command

```
mkvirtualenv -p python3 envname
```

##### Install requirements

To install the requirements for this project run

```
pip3 install -r requirements_local.txt
```

### 3 - Run

To running smart robot to discovery triangle shapes

```
python run.py
```

### 4 - Tests

To running the tests

```
nosetests
```
