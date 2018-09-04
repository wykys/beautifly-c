# Beautifly C/C++

The script runs [uncrustify](https://github.com/uncrustify/uncrustify) for the specified file, or recursively to the specified folder.

## Installation
```sh
# the script requires installed uncrustify
sudo aptitude install uncrustify
cd /usr/bin
# /home/wykys/projects replace your location
sudo ln -s /home/wykys/projects/beautifly-c/beautify-c.py beautifly-c
# create a link to the configuration file
cd ~/.config
ln -s /home/wykys/projects/beautifly-c/uncrustify.cfg
```

## Use
```sh
beautifly-c --help                # for help, you can use -h
beautifly-c --file your_directory # for your_directory -f
beautifly-c --file your.c         # for your file -f
beautifly-c                       # for actual diractory -f
```

## Parameters
```
$ beautifly-c --help
usage: beautifly-c [-h] [-f PATH]

The script runs uncrustify for the specified file, or recursively to the
specified folder.

optional arguments:
  -h, --help            show this help message and exit
  -f PATH, --file PATH  destination source or header file

```

## Support extension
```
.c
.c++
.cpp
.h
.h++
.hpp
```
