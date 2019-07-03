
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

this is a automatic sudoko solver using python.
## Features:
- detect wrong numbers in eatch row and col .
- using 'numpy' library
- simple class
  
### usage

just run it! 

simple input :

```sh
reading strted ...
reading completed.
-------------------------------------
| 7   9     |           | 3         |
|   +   +   +   +   +   +   +   +   |
|           |         6 | 9         |
|   +   +   +   +   +   +   +   +   |
| 8         |     3     |     7   6 |
|---+---+---+---+---+---+---+---+---|
|           |         5 |         2 |
|   +   +   +   +   +   +   +   +   |
|         5 | 4   1   8 | 7         |
|   +   +   +   +   +   +   +   +   |
| 4         | 7         |           |
|---+---+---+---+---+---+---+---+---|
| 6   1     |     9     |         8 |
|   +   +   +   +   +   +   +   +   |
|         2 | 3         |           |
|   +   +   +   +   +   +   +   +   |
|         9 |           |     5   4 |
-------------------------------------


```

sample output:
```sh
 Processing... 

None
-------------------------------------
| 7   9   6 | 8   5   4 | 3   2   1 |
|   +   +   +   +   +   +   +   +   |
| 2   4   3 | 1   7   6 | 9   8   5 |
|   +   +   +   +   +   +   +   +   |
| 8   5   1 | 2   3   9 | 4   7   6 |
|---+---+---+---+---+---+---+---+---|
| 1   3   7 | 9   6   5 | 8   4   2 |
|   +   +   +   +   +   +   +   +   |
| 9   2   5 | 4   1   8 | 7   6   3 |
|   +   +   +   +   +   +   +   +   |
| 4   6   8 | 7   2   3 | 5   1   9 |
|---+---+---+---+---+---+---+---+---|
| 6   1   4 | 5   9   7 | 2   3   8 |
|   +   +   +   +   +   +   +   +   |
| 5   8   2 | 3   4   1 | 6   9   7 |
|   +   +   +   +   +   +   +   +   |
| 3   7   9 | 6   8   2 | 1   5   4 |
-------------------------------------

```
