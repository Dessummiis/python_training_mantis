from model.project import Project
import random

def test_delete_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="project"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert old_projects == new_projects
