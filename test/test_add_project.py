from model.project import Project
import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    project = Project(name=random_string(10), description=random_string(20))
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    app.project.create(project)
