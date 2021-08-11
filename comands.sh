pip --version
pip install Nympy
pip install pandas
pip install matplotlib
pip install sklearn #scikit-learn
pip install TensorFlow

# Upgrade
pip install --upgrade pip
pip install --upgrade Numpy
pip install --upgrade matplotlib
pip install --upgrade sklearn
pip install --upgrade TensorFlow

# List of libraries with versions
pip freeze

# Django enviorment setup
    python --version
    pip freeze
    ##Create a Pipenv-based Virtual Environment:
    mkdir folder
    cd folder
    pipenv install
    pipenv shell
    # instead of pipenv shell we can use 
    .\Scripts\activate
    # to activate the shell
    # (folder) > 
    # to deactivate the virtualenv
    (folder) > deactivate
    # install django in the virtualenv, basically the project folder
    pipenv install Django==3.0.2 # (3.0.2 is the version of Django)