# Create Virtual Env

```bash

# Creating New Virtual Env
python -m venv venv

# Activating Virtual Env
source venv/bin/activate

# Installing Requirements
pip install -r requirements.txt

# Running App
FLASK_APP=mytinyjournal.py flask run

```

----

## Setup

Create a folder for your SQL lite database and update `INSTANCE_FOLDER_PATH` in the config file. Run `flask initdb` command to create tables and seed test data.

```
flask initdb
```
## Hello World

## Using Templates

* **Separation of Concern** Separating application logic and presentation logic
* To render template, Flask provides `render_template` function
* Under the cover, `render_template` uses **Jinja2** templating engine
