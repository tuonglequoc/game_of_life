# Game Of Life
## Create virtual environment
```
$ virtualenv venv
```
```
$ source venv/bin/activate
```
```
$ pip install -r requirements.txt
```
## Configuration file
In config.py:
```
HEIGHT = 10  # Height of cells
WIDTH = 10  # Width of cells
FRAMES = 50  # Number of frames in the animation (number of iterations to perform)
INTERVAL = 100  # Interval of animation in milliseconds
OUTPUT_FILE_NAME = "output.gif"  # File name to save (gif file)
```
## Sample input file
In input.txt:
```
0100100100
0010001011
0001010010
1010010100
0101010101
0100010100
0000101001
1101000001
0100101001
1100010000
```
## Run the script
### Run with random value
```
$ python game_of_life.py
```
### Run with input file
```
$ python game_of_life.py --input input.txt
```
Notice: Input data must match with HEIGHT and WIDTH in config.py file.
### Open saved animation file
```
$ see output.gif
```