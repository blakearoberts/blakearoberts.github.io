from flask import url_for
import yaml


class About(object):
    """
    Defines a personal or school project.

    Properties:
        title: The title of the about me section.
        description: The description of the project.
        repo: The address of the repository.
    """

    def __init__(self, title='', image='', description='', contact=[]):
        self.title = title
        self.image = url_for('static', filename=image)
        self.description = description
        self.contact = contact

    @staticmethod
    def load(yaml_file):
        about = None
        with open(yaml_file, 'r') as file:
            raw_about = yaml.load(file)
            about = About(
                title=raw_about['title'],
                image=raw_about['image'],
                description=raw_about['description'],
                contact=raw_about['contact'],
            )
        return about
