# Example Python package
This python package demonstrate an example of how a typical python package can be structured

```
helloworld/
│
├── helloworld/
│   ├── __init__.py
│   ├── helloworld.py
│   └── helpers.py
│
├── tests/
│   ├── helloworld_tests.py
│   └── helpers_tests.py
│
|── conf/
|   |──logging.ini
|
|── __main__.py
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

1. helloworld/__init__.py:  
- This file has many functions, but for our purposes it tells the Python interpreter that this directory is a package directory. 
- You can set up this __init__.py file in a way that enables you to import classes and methods from the package as a whole, instead of knowing the internal module structure and importing from helloworld.helloworld or helloworld.helpers.

