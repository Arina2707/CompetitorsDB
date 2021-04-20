from mongoengine import *
import yaml


class Connection:
    def __init__(self):
        credentials_data = self.process_yaml()
        self.cluster_url = credentials_data["db_cluster_link"]["url"]

    @staticmethod
    def process_yaml():
        with open("config.yaml") as file:
            return yaml.safe_load(file)

    def connect(self):
        conn = connect("CompetitorsEvaluation", host=self.cluster_url)
        print("Successfully connected!")
        mydb = conn['CompetitorsEvaluation']

        return mydb
