### flag hunters

We are given lyric-reader.py

Brief read and run through, its obvious that we need to somehow get into the secret intro part
Meanwhile, the input we can give is only during the CROWD section

Note that line 111 splits the line with ';', and its not sanitised. We can do injection here

After some attempts using python debugger in VSCode, putting ";RETURN 0" solves the problem
