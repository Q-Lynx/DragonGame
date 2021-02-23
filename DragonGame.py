#import DragonStatistics 

class Dragon:
    def __init__(self, name, level=0):
         self.name = name
         self.level = level
#         self.stats = Statistics.Stats()

    def __str__(self):
        return "name: {}, level: {}".format(self.name, self.level)

    def levelUp(self):
        self.level = self.level + 1

    def feed(self):
        self.levelUp()
    
    def save(self, filename):
        savefile = open(filename, 'w')
        try:
            savefile.write(str(self))
            savefile.write('\n')
        finally:
            savefile.close()

    def load(filename):
        name = None
        level = None
 
        savefile = open(filename, 'r')
        try:
            tmp = savefile.readline()
            name = tmp.split(',')[0][6:]     # TODO: FIX!
            level = int(tmp.split(',')[1][7:-1])  # TODO: FIX!
        finally:
            savefile.close()
 
        return Dragon(name, level)
