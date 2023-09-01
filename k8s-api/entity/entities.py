# from db.model import Cluster
import json
from json import JSONEncoder

class ClusterEntity():
    def __init__(self, id, name, environment, apiserver, status, version):
        self.id = id
        self.name = name
        self.environment = environment
        self.apiserver = apiserver
        self.token = "***"
        # self.last_modified_time = last_modified_time
        self.status = status
        self.version = version
    
    # def toJSON(self):
    #     return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class ClusterEntityEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__
