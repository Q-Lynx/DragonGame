
class Stats:
    def __init__(self, stat_name, value=1):
        self.stat_name = stat_name
        self.value = value

    def __str__(self):
        return "{} : {}".format(self.stat_name, self.value)

    def statUp(self):
        self.value = self.value + 1 
  
    def improve(self):
        self.statUp() 
