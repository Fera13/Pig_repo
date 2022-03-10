Pig dice game
==========================

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A dice game called Pig

[[_TOC_]]


About pig dice game
--------------------------

This project is based on the Pig Dice Game. The Pig Dice Game is a game usually played with a real dice between two players. The goal of the game is to reach 100 points before the other player. Pig Dice Game is a round based game where the player chooses how many times they would like to roll each round. If the player recieves a 1 from rolling the dice the round total will be set to 0 points. If the player chooses to stop rolling before recieving a 1, the round total will be added to the total score of the player.


Project description
--------------------------

When you start the game the main menu will pop up. From there you can choose from a variety of options, including starting a game, viewing high scores, updating names, deleting existing players, showing game rules and of course quitting. When you start the game you can either play against a friend or play against our AI called "Weird Ai Yankovic". The AI has three different difficulties, easy, normal and hard. The easy one has a larger chance of getting 1's while rolling, the normal one has the same odds as a regular human and the hard mode has a higher chance of rolling high numbers such as 5 and 6. In order to determine how many times the AI should roll, we use a random int to ask the AI how many times it wants to roll. The random is in range from 1 to 7 on hard and normal, and for easy it either rolls a low amount such as 1 or 2 or a lot of rolls ranging from 5 to 7. 

After a game is finished the high score will be updated accordingly by using different files. If the player had a better score than the players already on the high score it will get replaced in a dictionary and then it will write the new updated list to the file. That enables us to keep the high score even when quitting the game. The same works for the existing players, only that we work with a list instead of a dictionary. 

When a player starts the round, he first enters how many times he/she wants to roll. Once the player has given us how many times it would like to roll it will generate a number between 1 - 6 (the surfaces of a regular dice) for the amount of times the player wished to roll. If the player recieved a 1 however, the round total will be 0. Otherwise all the points from the roll will be added up and later returned and added to the total score for the player.


How to install the game
--------------------------

In order to install the game you first need to download the files from https://github.com/Fera13/Pig_repo. Once you have downloaded all the files you can check that you have the correct version of python by following the steps below. Once you have python installed, you can either use this through your command line, through an IDE like Visual Studio Code or by using Git Bash. When you want to run the game through the command line you need to enter the directory where you downloaded the game files and then enter the folder "Pig". Once you are in "Pig" you can write "python main.py" and the game should start. If the game is not running, make sure you are in the "Pig" folder and not the "Pig_Repo" folder. May the odds ever be in your favor!


Get going
--------------------------

This is how you can work with the development environment.



### Check version of Python

Check what version of Python you have. The Makefile uses `PYTHON=python` as default.

```
# Check you Python installation
make version
```

If you have another naming of the Python executable then you can solve that using an environment variable. This is common on Mac and Linux.

```
# Set the environment variable to be your python executable
export PYTHON=python3
make version
```

Read more on [GNU make](https://www.gnu.org/software/make/manual/make.html).



### Python virtual environment

Install a Python virtual environment and activate it.

```
# Create the virtual environment
make venv

# Activate on Windows
. .venv/Scripts/activate

# Activate on Linx/Mac
. .venv/bin/activate
```

When you are done you can leave the venv using the command `deactivate`.

Read more on [Python venv](https://docs.python.org/3/library/venv.html).



### Install the dependencies

Install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the `requirements.txt`.

Do not forget to check that you have an active venv.

```
# Do install them
make install

# Check what is installed
make installed
```

Read more on [Python PIP](https://pypi.org/project/pip/).



### Run the code

The game can be started like this.

```
# Execute the main program
Use "cd {the right directory}" and you should reach /Pig
When in the correct directory, type "python main.py"

```

All code is stored below the directory `Pig/`.



### Run the validators

You can run the static code validators like this. They check the sourcecode and exclude the testcode.

```
# Run each at a time
make flake8
make pylint

# Run all on the same time
make lint
```

You might need to update the Makefile if you change the name of the source directory currently named `guess/`.

Read more on:

* [flake8](https://flake8.pycqa.org/en/latest/)
* [pylint](https://pylint.org/)



### Run the unittests

You can run the unittests like this. The testfiles are stored in the `test/` directory.

```
# Run unttests without coverage
make unittest

# Run unittests with coverage
make coverage

# Run the linters and the unittests with coverage
make test
```

You can open a web browser to inspect the code coverage as a generated HTML report.

```
firefox htmlcov/index.html
```

Read more on:

* [unittest](https://docs.python.org/3/library/unittest.html)
* [coverage](https://coverage.readthedocs.io/)



### Run parts of the testsuite

You can also run parts of the testsuite, for examples files or methods in files.

You can run all tests from a testfile.

```
# Run a testfile
python -m unittest test.test_game
```

You can also run a single testcase from a file.

```
# Run a test method, in a class, in a testfile
python -m unittest test.test_game.TestGameClass.test_init_default_object
```



### Remove generated files

You can remove all generated files by this.

```
# Remove files generated for tests or caching
make clean

# Do also remove all you have installed
make clean-all
```



Optional targets
--------------------------

These targets might be helpful when running your project.



### Codestyle with black

You can unify the codestyle using black. Running black will change your source code to have a codestyle according to black codestyle.

```
# Same same, different names
make black
make codestyle
```

Read more on [black](https://pypi.org/project/black/).



More targets
--------------------------

The Makefile contains more targets, they are however not yet tested on this directory structure.
