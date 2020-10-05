import sys
import urllib.request

if len(sys.argv) != 2:
    raise ValueError('This is an error!')

print(f"Script Name is {sys.argv[0]}")

isbn = sys.argv[1]

print(f'The isbn is: { isbn }')

contents = urllib.request.urlopen(f'https://www.googleapis.com/books/v1/volumes?q=isbn:{ isbn }')

# TODO: prints only the adress of the object. I need a python thing.
print(contents)