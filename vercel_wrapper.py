# your_project/vercel_wrapper.py
import sys
activate_this = "/your_project/.venv/bin/activate_this.py"
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from flask import Flask, render_template
from app import create_app

app = create_app()

def handler(request, response):
    return app(request.environ, response)

# For rendering Flask templates
def render_template_handler(request):
    return render_template(request.path, **request.query)

if __name__ == "__main__":
    from vercel_python import serve
    serve(app, render_template=render_template_handler)
