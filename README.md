# Snake AI

Simple Python implementation of the popular game of Snake.

**But why play it yourself, if your computer can do it for you?**

## Usage

### Linux

- Run `setup.sh`
- Source the virtual environment: `. ./venv/bin/activate`
  - If you run a different shell like _fish_, source the appropriate file
- Run `pip install -r requirements.txt`
- Run `./main.py`

### Windows
- Optional: if prefer to use a virtual environment, create one and source it
- Run `pip install -r requirements.txt`
- Run the file `main.py` with your python interpreter

### Commands
Currently, the program accepts the following commands:
- `--size`: sets the size of the playing field; One integer
- `--tile_size`: sets the pixel size of one tile. Adjust for different resolutions; One integer
- `--interval`: the minimum time the AI waits between turns; One integer
