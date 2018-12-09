import yaml


class Experience(object):
    """
    Defines a professional/work experience.

    Properties:
        name: The name of the experience.
        description: The description of the experience.
    """

    def __init__(self, name='', description='', location='', start_date='',
                 end_date=''):
        self.name = name
        self.location = location
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def load_all(yaml_file):
        experiences = []
        with open(yaml_file, 'r') as file:
            raw_experiences = yaml.load(file)
            for experience in raw_experiences:
                experiences.append(Experience(
                    name=experience['name'],
                    location=experience['location'],
                    start_date=experience['start_date'],
                    end_date=experience['end_date'],
                    description=experience['description'],
                ))
        return experiences
