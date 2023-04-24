# Extraction Demo

This is the demo of how the project is going to be implemented.

# Setup

1. Create a Python environment using `virtualenv`
2. Run `pip install -r requirements.txt` to install dependencies.
3. Configure `STUDENT_ID` and `STUDENT_EMAIL` in `.env` file in the root folder.
   This is a required step as Projar API use both data to obtain the access token.
4. To run development server, use `python manage.py runserver`.


# Elements of demonstrations

- How data is obtained?
- How keywords will be extracted?

Currently, CSO classifier is not available due to the library is currently using [outdated dependencies](https://github.com/angelosalatino/cso-classifier/issues/13). [KeyBERT](https://maartengr.github.io/KeyBERT/index.html) is currently used instead