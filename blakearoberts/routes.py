from flask import render_template
import os

from blakearoberts import app
from blakearoberts.models.project import Project


@app.route('/')
def main():
    yaml_file = os.path.join(app.root_path, 'documents/projects.yaml')
    projects = Project.load_all(yaml_file)
    return render_template('index.jinja', projects=projects)
