# Creating virtual environment

### Setting up environment

Running with the system Python and libraries limits you to one specific Python version, chosen by your OS provider. Trying to run all Python applications on one Python installation makes it likely that version conflicts will occur among the collection of libraries. It's also possible that changes to the system Python will break other OS features that depend on it(In Linux system mostly, if python version is reverted or the python is removed overall, linux will be broken. It is suggested to not remove OS provided python version in any system.).

Virtual environments, are lightweight, self-contained Python installations, designed to be set up with a minimum of fuss, and to "just work" without requiring extensive configuration or specialized knowledge.

virtualenv avoids the need to install Python packages globally. When a virtualenv is active, pip will install packages within the environment, which does not affect the base Python installation in any way.

To setup a virtualenv, run the `venv.sh` file in your project folder, it will create a virtual environment `venv` for you. Make sure you have python, pip(package manager for python) available in your system.

Note: This repository is build on Linux, most of the Linux or Mac commands are likely to be sucessfully run. Windows based commands can be found on stackoverflow, if you reckon know what to search for.

- #### Step 1

Creating virtual environment with virtualenv python package. The virtual environment can be simply removed by just removing the folder venv.

Linux or Mac
```
sh venv.sh
```

Windows
```
bash venv.sh
```
The bash command wil also work in UNIX based OS.

- #### Step 2

Activate virtual environment, so that the python on the system is not used and the packages we install won't be available globally, unless the environment is active.

Linux or Mac
```
source venv/bin/activate
```

Windows
```
venv/bin/activate
or
venv\Scripts\activate
```

- #### Step 3

Installing all the packages mentioned in the requirements.txt file with particular versions given individually to each package, as used on this repository.

Linux or Mac
```
sh commands.sh
```

Windows
```
bash commands.sh
```

Instead of running the above commmand to install the packages, we can also do the below command
```
pip3 install -r requirements.txt
```

Your virtual environment setup is finished now, and available as the folder venv. `venv` is a general name used when creating a virtual environment, you can replace it with your desired name and also substitute the same in all the other commands.

Note: Pynvim, msgpack, greenlet python packages are suggested to be not installed to the environment. You can edit the requirements.txt file and remove the lines with these three packages and process step 3 again or just remove it using pip like shown below, also you can remove any package you dont want with the below commands supposedly.

```
pip3 uninstall pynvim msgpack greenlet
```

<!--
[adding](hyper_link_to_a_text)
-->
