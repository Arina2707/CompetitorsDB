from mongoengine import *


class Connection:
    def __init__(self):
        self.cluster_url = ""

    def connect(self):
        conn = connect("CompetitorsEvaluation", host=self.cluster_url)
        print("Successfully connected!")
        mydb = conn['CompetitorsEvaluation']

        return mydb
