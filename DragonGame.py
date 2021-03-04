# import DragonStatistics
import json 


class Dragon:
    def __init__(self, name, level=0):
        self.name = name
        self.level = level
#         self.stats = Statistics.Stats()

    def __str__(self):
        return "name: {}, level: {}".format(self.name, self.level)

    def to_dict(self):
        result = dict()
        result["name"] = self.name
        result["level"] = self.level
        return result

    def to_json(self):
        return json.dumps(self.to_dict())

#            a_dict[variable] = eval(variable)

    @classmethod
    def from_json(cls, input_json):
        tmp = json.loads(input_json)
        result = cls(tmp["name"], tmp["level"])

        return result

    def levelUp(self):
        self.level = self.level + 1

    def feed(self):
        self.levelUp()
    
    def save(self, filename):
        savefile = open(filename, 'w')
        try:
            savefile.write(self.to_json())
            savefile.write('\n')
        finally:
            savefile.close()

    @classmethod
    def load(cls, filename):
        savefile = open(filename, 'r')
        tmp = ""

        try:
            tmp = savefile.read()
        finally:
            savefile.close()

        return cls.from_json(tmp)
