# Create Virtual Env
```
python -m venv venv
```

# Activating Virtual Env

```
source venv/bin/activate
venv\Scripts\activate
```

# Installing Flask
```
pip install flask
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
