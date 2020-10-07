# weekly

Every week something new!

# Week 01 ( 04.10.2020 - 10.10.2020)

Run the program with something like `isbn-catcher 9781590173138` and a file (or more) with the html/json code containing information about this book appears in the folder.

## Day 04
- where does this method `get_content_charset` come from? The response seems to be of type `http.client.HTTPResponse`. But where is that defined?
- write it to a file `api-isbn-date.json`

### Achieved
#### print file
``` python
with open('file.name', 'w') as f:
    f.write(contents.read().decode('utf-8'))
```
this is an interesting construct.
A problem is now, like with all streams, I cannot use him two times. When he was read, he was read.
So at the moment, I can read the stream and print it, or I can write it to a file.

If I want to write the file into a directory, I must 
1. create the directory
2. and then use this crazy `with open() as f:` syntax. Where does it come from?

## Day 03
- display the content of the answer of the `urllib` call &#10004;

### Achieved
#### print bufferedReader
1. debug output and see what type the answer is. In this case it was a `BufferedReader`, a byte stream. So we just needed to read the stream:
   ``` python
   contents = urllib.request.urlopen(url)
   stream = contents.read()
   ```
  > https://docs.python.org/3/library/io.html#io.BufferedReader
2. This caused the display of `\n` in the output. And this is a problem of the used charset. When this is not defined, the `\n` is not seen as line break, but as two distinct signs.
  ``` python
  encoding = contents.headers.get_content_charset()
  stream.decode(encoding)
  ```
  This will display the whole json, as it should be displayed.
  > https://stackoverflow.com/questions/14592762/a-good-way-to-get-the-charset-encoding-of-an-http-response-in-python
#### Questions
  But where does this method `get_content_charset` come from? Not really form `email.message.py`??? It seems, that it comes directly from there... I cannot explain how or why...



## Day 02
- add a gitignore file, which ignores the venv specific files and folders. &#10004;
- make a call to google books api and display the content of the json. &#10004;
- should `pyvenv.cfg` be in gitignore? &#10004;

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
- Create new a python project. (with a virtual environment manager) (How does this work again?)  &#10004;
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

