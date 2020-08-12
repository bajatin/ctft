#!/usr/bin/env python
import argparse
import os
import asyncio

from get_writeup_url import list_writeups


home = os.getenv("HOME")
path = os.path.join(home,"ctft_writeups")
if not os.path.exists(path):
    os.mkdir(path)

async def main():
    my_parser = argparse.ArgumentParser(prog='ctft',description='Get and view stylised ctftime writeups in your terminal')
    my_group = my_parser.add_mutually_exclusive_group(required=True)
    my_group.add_argument('-e','--event',help="Name of the ctf event")
    my_group.add_argument('-v','--view',help="View writeup in terminal",metavar="TASK NAME")
    args = my_parser.parse_args()
    if args.event:
        await list_writeups(args.event)
    if args.view:
        if not os.path.isfile(args.view):
            print("No such file in current directory")
        else:
            cmd = "vmd " + args.view + " | less -rc"
            os.system(cmd)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    
