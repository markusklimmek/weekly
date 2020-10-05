# weekly

Every week something new!

# Week 01 ( 04.10.2020 - 10.10.2020)

Run the program with something like `isbn-catcher 9781590173138` and a file (or more) with the html/json code containing information about this book appears in the folder.

## Day 02
- add a gitignore file, which ignores the venv specific files and folders.
- make a call to google books api and display the content of the json.
- should `pyvenv.cfg` be in gitignore?


## Day 01
- Create new a python project. (with a virtual environment manager) (How does this work again?) 
- have a program, that reads an input and displays it.

### Achieved
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

