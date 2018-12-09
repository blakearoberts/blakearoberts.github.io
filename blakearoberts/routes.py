from flask import redirect, render_template, url_for
import os

from blakearoberts import app
from blakearoberts.models.project import Project
from blakearoberts.models.about import About
from blakearoberts.models.experience import Experience

ABOUT_YAML_FILE = os.path.join(
    app.root_path, 'documents/about.yaml')
PROJECTS_YAML_FILE = os.path.join(
    app.root_path, 'documents/projects.yaml')
WORK_EXPERIENCE_YAML_FILE = os.path.join(
    app.root_path, 'documents/work_experience.yaml')

about = None
projects = None
work_experience = None


@app.route('/')
def index_route():
    global about, work_experience, projects

    if not about:
        about = About.load(ABOUT_YAML_FILE)
    if not projects:
        projects = Project.load_all(PROJECTS_YAML_FILE)
    if not work_experience:
        work_experience = Experience.load_all(WORK_EXPERIENCE_YAML_FILE)

    return render_template('index.jinja', about=about, projects=projects,
                           work_experience=work_experience)


@app.route('/resume.pdf')
def resume_route():
    return redirect(url_for(
        'static',
        filename='Blake_Roberts_Resume.pdf',
        _external=True,
    ))


@app.route('/projects/')
def projects_route():
    global projects

    if not projects:
        projects = Project.load_all(PROJECTS_YAML_FILE)

    return render_template('projects.jinja', projects=projects)


@app.route('/work_experience/')
def work_experience_route():
    global work_experience

    if not work_experience:
        work_experience = Experience.load_all(WORK_EXPERIENCE_YAML_FILE)

    return render_template('work_experience.jinja',
                           work_experience=work_experience)
