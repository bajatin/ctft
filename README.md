# ctft

ctft is a python cli tool to save and view ctftime.org writeups in your terminal

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
### DEMO
` python3 ctft.py -e asis`
![event_demo](event_demo.gif)

You can also make add a alias of ctft or add ctft to $PATH for easier usage

`ctft -v Web\ Warm-up`
![view_demo](view_demo.gif)

## TODO
- [ ] Add complete README
- [ ] Make pip package for easier installation and use
## Contributing
I started this project solely for educational purposes to familiarize myself with python and asynchronous programming.
Pull requests or suggestions for imporvement are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
