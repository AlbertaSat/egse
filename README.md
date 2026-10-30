# About

EGSE is a library and CLI tool for controlling electrical ground support equipment. It has support for the Rigol DP832A power supply and the Keysight 34460A multimeter.


## CLI

Documentation for each individual instrument is found in the `docs` folder.

**Usage**:

```console
$ egse [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `ls`: List connected instruments
* `dp832a`: Rigol DP832/A power supply subcommands
* `k34460a`: Keysight 34460A DMM subcommands

### `ls`

List connected instruments

**Usage**:

```console
$ egse ls [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.



## Installation

This repo uses Python 3.12.11, so ensure that you have that version installed. It also uses Poetry as a package manager, so install that as well.
1. `poetry install` to install the dependencies
2. `poetry env activate` to show the command to activate the venv. Copy the command and exectute it to activate the venv.
    - Sometimes you will have to set the correct python version
3. `egse --help` to get a list of commands

