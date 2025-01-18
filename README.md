# V0wels
An application that removes vowels and set the text to lowercase.

The application was implemented as a CS50P assignment.<br>
Please respect, and keep the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/) in mind.

A demo can be watched at [CS50P's Problem set 2 | twttr](https://cs50.harvard.edu/python/2022/psets/2/twttr/)

## Installation
1. Clone the repository:
```sh
# Using SSh 
ssh git@github.com:krigjo25/console-V0wels-py.git

# Using git bash
git clone https://github.com/krigjo25/console-V0wels-py.git

# Using Github Cli
gh repo clone console-V0wels-py
```

2. Navigate to the project directory
```sh
cd console-V0wels-py
```

3. Install the requirements
```sh
pip install -r requirements.txt
```

1. Run the file
```sh
python app.py
```

##  Usage
To use the application, run the following command in your terminal

```sh
Usage : type in the terminal python app.py, wait for the prompted message
then type in some names.
python app.py <Name>
```
Replace `<Name>` with the desired name, seperate the names with comma to add multiple name

## Example
```sh
python app.py

prompt: TWITTER
expected output: twttr
```

##  Credits

### Responsories
[pytest - Holger Krekel ( and many other developers)](https://github.com/pytest-dev/pytest)

##  Testing framework / Datasets
Implements the testing network <strong>pytest</strong>
to test the code.The testing network uses assertion to
test values and raise known exceptions.

Pytest was used to test this application According

The data sets which is used within this project can be found in [this folder](./tests/test_app.py)

```sh
pytest test_app.py
pytest -k test_app.py
pytest --html=index.html
```

## LICENCE
The application is under [The Unlicensed](./LICENCE).

## Notes from the developer
Created with love, for python programming,

Thanks for reading, and have a blessed day,<br>
@krigjo25