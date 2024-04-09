# 0x02. i18n

## Back-end

- **Weight:** 1
- **Project start:** Apr 9, 2024 6:00 AM
- **Project end:** Apr 10, 2024 6:00 AM
- **Checker release:** Apr 9, 2024 12:00 PM
- **Manual QA review:** Must be done (request it when you are done with the project)
- **Auto review:** Will be launched at the deadline

## Resources
Read or watch:

- [Flask-Babel](https://pythonhosted.org/Flask-Babel/)
- [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiv-i18n-and-l10n)
- [pytz](http://pytz.sourceforge.net/)

## Learning Objectives
- Learn how to parametrize Flask templates to display different languages
- Learn how to infer the correct locale based on URL parameters, user settings, or request headers
- Learn how to localize timestamps

## Requirements
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- All your *.py files should be executable
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions and methods should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Tasks

### 0. Basic Flask app
#### Mandatory
- First, you will set up a basic Flask app in `0-app.py`.
- Create a single `/` route and an `index.html` template that simply outputs "Welcome to Holberton" as page title (`<title>`) and "Hello world" as header (`<h1>`).

### 1. Basic Babel setup
#### Mandatory
- Install the Babel Flask extension: `$ pip3 install flask_babel==2.0.0`
- Then instantiate the Babel object in your app. Store it in a module-level variable named `babel`.
- Create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.
- Use `Config` to set Babel’s default locale ("en") and timezone ("UTC").
- Use that class as config for your Flask app.

### 2. Get locale from request
#### Mandatory
- Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.

### 3. Parametrize templates
#### Mandatory
- Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.
- Create a `babel.cfg` file containing...

... (remaining tasks truncated for brevity) ...

### 8. Display the current time
#### Advanced
- Based on the inferred time zone, display the current time on the home page in the default format.
- For example: "Jan 21, 2020, 5:55:39 AM" or "21 janv. 2020 à 05:56:28"
- Use the following translations:
  - English: "The current time is %(current_time)s."
  - French: "Nous sommes le %(current_time)s."

## Repository Information
- **GitHub Repository:** [alx-backend](https://github.com/orumagideon/alx-backend)
- **Directory:** 0x02-i18n
