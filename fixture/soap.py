from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = self.wsdl()
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        client = self.wsdl()
        self.project_list_refined = []
        project_list = client.service.mc_projects_get_user_accessible(username, password)
        for i in project_list:
            id = i.id
            name = i.name
            description = i.description
            self.project_list_refined.append(Project(id=id, name=name, description=description))
        return list(self.project_list_refined)


    def wsdl(self):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        return client
