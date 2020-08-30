# Polls App
--------------

#### Simple app to test a package [multiple-permissions](https://pypi.org/project/multiple-permissions/).

* #### Development requirements.

    * Install [python3](https://www.python.org/download/releases/3.0/) (>=3.6).
    * Make [virtualenv](https://virtualenv.pypa.io/en/latest/) (the way you would like). Example `virtualenv venv`.
    * Activate virtualenv `source /venv/bin/activate`.
    * Isntall requirements from **requirements.txt** `pip install -r requirements.txt`.
    * And run the app `./manage.py runserver`.

* #### Usage.

    * Register a random user.
    * Login with that user (and you will have access to see the polls list with that user).
    * --------------------------------------
    * Create superuser (with activated virtualenv) `./manage.py createsuperuser` (and you will have access to create polls with that user). 
