# weekly

Every week something new!

# Week 01 ( 04.10.2020 - 10.10.2020)

Run the program with something like `isbn-catcher 9781590173138` and a file (or more) with the html/json code containing information about this book appears in the folder.

## Day 03
- display the content of the answer of the `urllib` call
- write it to a file `api-isbn-date.json`

## Day 02
- add a gitignore file, which ignores the venv specific files and folders.
- make a call to google books api and display the content of the json.
- should `pyvenv.cfg` be in gitignore?

### Achieved
#### Virtual Envs and .gitignore
- it seems, that `pyvenv.cfg` should be in gitignore file. At least github does this too. This is no good reason, but I think it is an indication for this.
- add all pyvenv related stuff to gitignore

#### Make a http call
This seems to be the simplest thing to do with python.

``` python
import urllib.request
contents = urllib.request.urlopen(f'https://www.googleapis.com/books/v1/volumes?q=isbn{isbn}')
print(contents)
``` 
> https://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python

## Day 01
- Create new a python project. (with a virtual environment manager) (How does this work again?) 
- have a program, that reads an input and displays it.

### Achieved

#### Virtual Env
- create a virtual environment, change into the folder and activate it
  ``` python
    python3 -m venv 01-isbn-catcher
    cd 01-isbn-catcher
    source bin/activate
  ```
- deactivate a virtual environment. This method comes with the bin/activate script that was sourced at the beginning
  ``` s
  deactivate
  ```
  > https://stackoverflow.com/questions/990754/how-to-leave-exit-deactivate-a-python-virtualenv

#### Read input from command line
- read an input using the `sys` module
  ``` python
  import sys

  if len(sys.argv) != 2:
      raise ValueError('This is an error!')

  print(f'Script Name is {sys.argv[0]}')

  isbn = sys.argv[1]

  print(f'The isbn is: { isbn }')
  ```
    This is really straightforward:
    access the `argv` array and iterate through it. `argv[0]` is always the script name itself. There are two further ways to do this.
    > If your script requires simple command-line arguments, you can go with sys.argv. But, if your program accepts a lot of positional arguments, default argument values, help messages, etc, then you should use argparse module. The getopt module works too but it’s confusing and hard to understand.
    > https://www.askpython.com/python/python-command-line-arguments

