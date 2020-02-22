import os
import json
from collections import UserDict



class Settings(UserDict):
    # def __init__(self, *args, **kwargs):
    #     super __init__(*args, **kwargs)

    def configPath(self):
        home = os.environ['HOME']
        subpath = os.path.join('.config','poledancer.json')
        return os.path.join(home, subpath)

    def restore_defaults(self):
        self.data = {
            "DriftTimer": 300
        }


    def load(self):
        self.restore_defaults()
        if os.path.exists(self.configPath()):
            self.data = json.loads(open(self.configPath()).read())

    def save(self):
        open(self.configPath(),'w').write(json.dumps(self.data, indent=4))