# GUI PROGRAMMING

Installing packages into system
```
pip3 install tk
```

Error:
```
Traceback (most recent call last):
  File "/home/balaji/Documents/Github/Python/GUI/hello.py", line 1, in <module>
    import tkinter as tk
  File "/usr/lib/python3.10/tkinter/__init__.py", line 37, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk
ImportError: libtk8.6.so: cannot open shared object file: No such file or directory

```

In Linux install tk package
```sudo pacman -S tk```
