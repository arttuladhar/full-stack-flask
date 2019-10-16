# Create Virtual Env
```
python -m venv venv
```

# Activating Virtual Env

```
source venv/bin/activate
```

# Installing Requirements
```
pip install -r requirements.txt
```

# Running Hello World
```
FLASK_APP=mytinyjournal.py flask run
```

----

## Hello World

## Using Templates

* **Separation of Concern** Separating application logic and presentation logic
* To render template, Flask provides `render_template` function
* Under the cover, `render_template` uses **Jinja2** templating engine
