import sys
import urllib.request

if len(sys.argv) != 2:
    raise ValueError('This is an error!')

print(f"Script Name is {sys.argv[0]}")

isbn = sys.argv[1]

print(f'The isbn is: { isbn }')

contents = urllib.request.urlopen(f'https://www.googleapis.com/books/v1/volumes?q=isbn:{ isbn }')

print(contents.read().decode(contents.headers.get_content_charset()))