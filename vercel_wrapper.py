# /your_project/vercel_wrapper.py
import sys
import os

# Adjust the path to your virtual environment activation script
activate_this = "/your_project/.venv/bin/activate_this.py"

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from flask import Flask, render_template

# Adjust the import to correctly point to your Flask app's create_app function
from app import create_app  # Replace 'app' with the correct directory name

app = create_app()

def handler(request, response):
    return app(request.environ, response)

# For rendering Flask templates
def render_template_handler(request):
    # Adjust the path to your templates directory
    templates_path = os.path.join(os.path.dirname(__file__), "app", "app/templates")
    return render_template(request.path, **request.query, templates_path=templates_path)

if __name__ == "__main__":
    from vercel_python import serve
    serve(handler, render_template=render_template_handler)
