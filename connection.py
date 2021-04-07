from mongoengine import *


class Connection:
    def __init__(self):
        self.cluster_url = "mongodb+srv://Arina:arina270799@cluster27-pldc3.gcp.mongodb.net/CompetitorsEvaluation" \
                           "?retryWrites=true&w=1 "

    def connect(self):
        conn = connect("CompetitorsEvaluation", host=self.cluster_url)
        print("Successfully connected!")
        mydb = conn['CompetitorsEvaluation']

        return mydb
