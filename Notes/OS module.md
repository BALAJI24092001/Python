## OS Python Module

The `os` module in Python provides a way to interact with the operating system. Here's a list of commonly used functions in the `os` module:

### File and Directory Functions
- `os.chdir(path)`: Change the current working directory.
- `os.getcwd()`: Get the current working directory.
- `os.listdir(path='.')`: List files and directories in the specified path.
- `os.mkdir(path[, mode])`: Create a directory.
- `os.makedirs(path[, mode])`: Recursively create directories.
- `os.remove(path)`: Remove a file.
- `os.rmdir(path)`: Remove an empty directory.
- `os.removedirs(path)`: Recursively remove directories.
- `os.rename(src, dst)`: Rename a file or directory.
- `os.replace(src, dst)`: Rename a file or directory, overwriting if necessary.
- `os.stat(path)`: Get file or directory status.
- `os.symlink(src, dst)`: Create a symbolic link.
- `os.path.isfile(path)`: Check if the path is a file.
- `os.path.isdir(path)`: Check if the path is a directory.

---

### File Descriptor Operations
- `os.open(path, flags[, mode])`: Open a file and return a file descriptor.
- `os.close(fd)`: Close a file descriptor.
- `os.read(fd, n)`: Read `n` bytes from a file descriptor.
- `os.write(fd, str)`: Write a string to a file descriptor.
- `os.lseek(fd, pos, how)`: Move the read/write file descriptor position.

---

### Process Management
- `os.getpid()`: Get the current process ID.
- `os.getppid()`: Get the parent process ID.
- `os.fork()`: Fork a child process (Unix only).
- `os.execv(path, args)`: Execute a new program, replacing the current process.
- `os.kill(pid, sig)`: Kill a process with the specified signal.
- `os.system(command)`: Run a system command.

---

### Environment Variables
- `os.environ`: A dictionary of environment variables.
- `os.getenv(key[, default])`: Get the value of an environment variable.
- `os.putenv(key, value)`: Set an environment variable (deprecated).
- `os.unsetenv(key)`: Unset an environment variable (deprecated).

---

### Path and Directory Utilities
- `os.path.join(path, *paths)`: Join one or more path components intelligently.
- `os.path.split(path)`: Split a pathname into head and tail.
- `os.path.basename(path)`: Get the base name of the path.
- `os.path.dirname(path)`: Get the directory name of the path.
- `os.path.exists(path)`: Check if the path exists.
- `os.path.getsize(path)`: Get the size of the file.
- `os.path.abspath(path)`: Get the absolute path of the file.

---

### Miscellaneous
- `os.urandom(n)`: Return `n` bytes of random data.
- `os.chmod(path, mode)`: Change the mode (permissions) of a file.
- `os.chown(path, uid, gid)`: Change the owner and group of a file.
- `os.setuid(uid)`: Set the current process's user ID.
- `os.setgid(gid)`: Set the current process's group ID.
- `os.umask(mask)`: Set the current numeric umask.
- `os.sep`: The separator used in paths (e.g., `'/'` for Unix, `'\\'` for Windows).
- `os.linesep`: The line separator (e.g., `'\n'` for Unix, `'\r\n'` for Windows).

You can find all the available functions by using:
```python
import os
print(dir(os))
```

This will include even internal functions (those starting with `_`).
