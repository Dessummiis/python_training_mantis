

def test_add_project(app, json_projects):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    project = json_projects
    # Проверить есть ли созданные группы
    # Создать группу если нет групп
    app.project.create(project)
    # Создать группу если есть группы
