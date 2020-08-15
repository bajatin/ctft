# ctft

ctft is a python cli tool to save and view stylised [ctftime.org](https://ctftime.org) writeups locally in your terminal.

- **Search for writeups** by name or keyword
- **View Stylised writeups** from saved files
- Writeups are saved are as **markdown files** which can also be read as plaintext(even though it doesn't make sense to read plaintext over formatted :unamused: )

VSCode users can also use markdown viewing extensions like [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) to view writeups

The project took inspiration from [mzfr's lswriteups](https://github.com/mzfr/lswriteups) but I wanted to further the ease of access and reduce browser dependence.

The tool currently scrapes only writeups on CTFTime.org and github READMEs.
If you would like to add support for your site or your favourite author(with their permission ofcourse), feel free to contact me or make a pull request

## Usage

```bash
➜ python3 ctft.py -h
usage: ctft [-h] (-e EVENT | -v TASK NAME)

Get and view stylised ctftime writeups in your terminal

optional arguments:
  -h, --help            show this help message and exit
  -e EVENT, --event EVENT
                        Name of the ctf event
  -v TASK NAME, --view TASK NAME
                        View writeup in terminal

```

- The files are saved in your (home directory)/ctft_writeups

### DEMO

` python3 ctft.py -e asisctf`
![event_demo](https://github.com/bajatin/README_gif_host/blob/master/event_demo.gif)

You can also make an alias of ctft or add ctft to $PATH for easier usage

`ctft -v Web\ Warm-up`
![view_demo](https://github.com/bajatin/README_gif_host/blob/master/view_demo.gif)

## Installation 
- Cone the repo:

`git clone https://github.com/bajatin/ctft`

- Install dependencies:

`pip install -r requirements.txt`

## Contributing
I started this project solely for educational purposes to familiarize myself with python and asynchronous programming.
Pull requests or suggestions for imporvement are welcome. For major changes, please open an issue first to discuss what you would like to change.

## TODO
- [ ] Upload pip package for easier install 

## License
[MIT](https://choosealicense.com/licenses/mit/)
