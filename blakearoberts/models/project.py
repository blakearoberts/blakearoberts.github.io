import yaml


class Project(object):
    """
    Defines a personal or school project.

    Properties:
        name: The name of the project.
        description: The description of the project.
        repo: The address of the repository.
    """

    def __init__(self, name='', description='', repo=''):
        self.name = name
        self.description = description
        self.repo = repo

    def load_all(yaml_file):
        projects = []
        with open(yaml_file, 'r') as file:
            raw_projects = yaml.load(file)
            for project in raw_projects:
                projects.append(Project(
                    name=project['name'],
                    description=project['description'],
                    repo=project['repo'],
                ))
        return projects
