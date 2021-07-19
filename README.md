# Git-Client
A simplified Git-like version control system written using Python.

Gitcl is not exactly Git, but it shares the important ideas of Git.To reduce the complexity of gitcl, it doesn't compress objects, doesn't save the mode of the files or doesn't save the time of a commit. But the important ideas, like commits, branches, the index, merges and remotes are all present and have been implemented very similar to Git.

## Requirements
Gitcl currently has only been testes on Linux based systems so the behaviour on Windows might be unpredictable or erroneous. For building Gitl you'll need to install Python v3.6 or higher and the following python modules using pip - 
```Typer```
```Typing``` and
```pathlib```

## Installation
To install gitcl on your system clone the repository and then run the command in the directory shell 
``` $ python3 setup.py develop --user ```
