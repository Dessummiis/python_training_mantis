from model.project import Project
import random

def test_delete_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="project"))
    old_projects = app.soap.get_project_list(username, password)
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.soap.get_project_list(username, password)
    old_projects.remove(project)
    assert old_projects == new_projects
