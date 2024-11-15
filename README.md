
# Basic Caesar Cipher

A basic caesar cipher command-line program that ask for input and either encrypt or decrypt by an shift value depending on the users input.\
**created as an [CS50P Final Project](https://cs50.harvard.edu/python/2022/)**

## Demo

To see a demo of the project see [this youtube video](https://www)

## Documentation

here follows an in depth view of the project

### Files

- project.py : The main program file
- test_project.py : unti test of project.py
- requirements.txt : list of all pip installed libraries
- LICENSE.txt : License used
- README.md : detailed overview of project

### Project

The current version of the caesar cipher project work by utilizing the command line.
When the caesar cipher is called, it prompt the user to input some text tot apply the cipher on. Next it asks to pick between encrypting or decrypting, the choice can be made with e/encrypt  for encrypting and d/decrypt for decrypting(case insensitive). As last it ask for the shift value for which any positive integer can be used.\
With all input collected it will first validate the input, then apply the caesar cipher and outputs the value in the console

#### Functions

The project uses the following functions

- main()
  - main function which calls other functions and prints the end result
- caesar(message, is_encrypt, change)
  - Function that applies the cipher with a positive or negative change depending if is_encrypt is true
  - message = str value to apply the cipher on
  - is_encrypt = bool where True value means encrypting and False means decrypting
  - change = int the number of positions the letter in message should shift
  - first it checks the value of is_encrypt and if its False then change will be -change, then it gets the ascii number for the letters and applies the shift and modulus length alphabet. then it return the character of the new ascii number\
   (letter ascii value - initial ascii value + shift)mod length alphabet + initial ascii value
- clean_input(values)
  - cleans the inputs by stripping the message value, converting the mode value to a bool and changing the shift to an int
  -values = tupple(message, mode, shift) which are validated
- get_inputs()
  - ask for a text , mode and shift input value and the passes those to validate
- validate(text, mode, shift)
  - validate the inputs for invalid values
  - text value gets checked if it isn't an empty string
  - mode value gets checked if it isn't e/encrypt/d/decrypt (case insensetive)
  - shift gets checked if it isn't a int value or if it is less then 0

### Libaries

A list of libaries used in this project and why they are used

- sys !SHOULD REPLACE! - System-specific parameters and functions(in python standard libary)
  - sys.exit is used in to exit the program
  - Used in project.py validate function
  - refer then [Python documentation](https://docs.python.org/3/library/sys.html#sys.exit) for more information
- string - Common string operations(in python standard libary)
  - string.ascii_lowerscase stores all lowercase letter in the alphabet
  - used in project.py caesar function
  - refer then [Python documentation](https://docs.python.org/3/library/string.html#string.ascii_lowercase) for more information
- pytest - unit testing framework for python (pip install pytest)
  - pytest.raises(Exception) is used to test condition returns the Exception
  - used in test_project.py for the exceptions TypeError,ValueError and SystemExit
  - refer the [pytest documentation](https://docs.pytest.org/en/latest/#) for more information
- mypy - type hint validation for python (pip install mypy)
  - command mypy *filename* is used to validate type hinting
  - used on project.py with mypy project.py
  - refer the [mypy documentation](https://mypy.readthedocs.io/en/stable/) for more information
- ruff - fast python linter - pip install ruff
  - command ruff check *filename* is used for linter/error checking
  - used on project project.py with ruff check project.py
  - refer the [ruff documentation](https://docs.astral.sh/ruff/) for more information

## Running Tests

To run the unittests, run the following command

``` bash
  pip install pytest
  pytest test_project.py
```

## Usage/Examples

### For project.py

Encrypting abc with shift 1 to bcd

```text
python project.py
Provide the text to use:
abc
Type E to  encrypt, D to decrypt: E
Provide a number for the shift value: 1
bcd
```

Decrypting DECRYPT_this 123 with shift 99 to bcd

``` text
python project.py
Provide the text to use:
DECRYPT_this 123
Type E to  encrypt, D to decrypt: DECRYPt
Provide a number for the shift value:99
IJHWDUY_ymnx 123
```

### for test_project.py

```python
pytest test_project.py
=================================================================================== test session starts ====================================================================================
platform linux -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /workspaces/24992088/project
plugins: typeguard-4.4.0
collected 3 items

test_project.py ...                                                                                                                                                                  [100%]

==================================================================================== 3 passed in 0.02s =====================================================================================
```

## Roadmap

- [ ] Add an brute force function too decrypt
- [ ] Add the possibility to read a file if a filename was given
- [ ] Add if input was a file, output  should be a new file
- [ ] Validate if filetype is supported/file exist
- [ ] Add the use command line arguments
- [ ] Add more ciphers
- [ ] restructure and refactor code

## Lessons Learned

- start with a basic program and then extend on it
- make sketches/notes on paper to visualize your project
- turn you goals into smaller goals that are easy to solve
- it is more then just code, it looked at licenses, created a README and requirements and wrote test
- me and the docs are now big buddies
- i had to strip a lot of feature i orignally wanted to implement so the project became doable

## Authors

- [@jmethorst](https://github.com/jmethorst)

## License

[MIT](https://choosealicense.com/licenses/mit/)
