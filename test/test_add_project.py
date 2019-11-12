from model.project import Project
import random
import string


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    project = Project(name=random_string(10), description=random_string(20))
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    assert app.session.is_logged_in_as("administrator")
    app.project.create(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
