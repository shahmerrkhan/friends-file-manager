# Friends File Manager

A command-line program for managing a list of names stored in a text file. Supports reading, writing, searching, appending, and deleting entries.

## What It Does

- Read all names from a file
- Write a fresh list to a file
- Search for a specific name
- Append new names without overwriting existing ones
- Delete a specific name from the file
- Switch between different files mid-session

## How to Run

```bash
python FriendsIO.py
```

You'll be asked for a filename. Press Enter to use the default `friends.txt`, or type any name (`.txt` is added automatically if you leave it out).

## Menu Options

```
1. Read the File
2. Write into the File
3. Search for a Name
4. Add Names
5. Delete Names
6. Change Filename
7. Quit
```

## Example

```
Enter file name: friends
1. Read the File
2. Write into the File
...
Input the number: 3
Enter the name to search for: Ahmed
Ahmed is in the file.
```

## Why I Built It

Built as a Grade 11 CS project to practice Python file I/O — reading, writing, appending, and safe deletion using a temporary file swap. Covers real file handling patterns used in production software.

## Built With

Python 3
