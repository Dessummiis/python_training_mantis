

def test_add_project(app):
    # Проверить есть ли созданные группы
    # Создать группу если нет групп
    app.project.create(project)
    # Создать группу если есть группы
