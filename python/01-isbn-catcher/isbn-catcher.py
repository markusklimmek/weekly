import sys

if len(sys.argv) != 2:
    raise ValueError('This is an error!')

print(f'Script Name is {sys.argv[0]}')

isbn = sys.argv[1]

print(f'The isbn is: { isbn }')
