from flask import render_template
import os

from blakearoberts import app
from blakearoberts.models.project import Project
from blakearoberts.models.about import About


@app.route('/')
def main():
    yaml_file = os.path.join(app.root_path, 'documents/projects.yaml')
    projects = Project.load_all(yaml_file)
    about_file = os.path.join(app.root_path, 'documents/about.yaml')
    about = About.load(about_file)
    return render_template('index.jinja', about=about, projects=projects)
