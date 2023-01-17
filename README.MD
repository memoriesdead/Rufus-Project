Git Info
This program prints specific facts about a local git repository. It takes one argument, the directory of the git repository and prints the following things:

1.active branch (boolean)
2.whether repository files have been modified (boolean)
3.whether the current head commit was authored in the last week (boolean)
4. whether the current head commit was authored by Rufus (boolean)

Getting Started
Clone the repository 

1. git clone https://github.com/memoriesdead/Rufus-Project.git
Run the script

2. python git_info.py "git_dir"

Make sure to replace git_dir with the actual directory of your local git repository.

Sample Output
active branch: True
local changes: False
recent commit: True
blame Rufus: True

Requirements
Python 3 and git installed on your computer.

Author
Kevin Chandarasane
