# MOTHER


class Stats:
    def __init__(self, value=1):
        self.value = value

    def statUp(self):
        self.value = self.value + 1

    def statDown(self):
        if self.value < 0:
            pass
        else:
            self.value = self.value - 1
  
    def improve(self):
        self.statUp()

# CHILD


class Strength(Stats):
    def __init__(self):
        super().__init__(self.value)
        self.name = "Strength"


class Agility(Stats):
    def __init__(self):
        super().__init__(self.value)
        self.name = "Agility"


class Brutality(Stats):
    def __init__(self):
        super().__init__(self.value)
        self.name = "Brutality"


class Intelligence(Stats):
    def __init__(self):
        super().__init__(self.value)
        self.name = "Intelligence"


class Charisma(Stats):
    def __init__(self):
        super().__init__(self.value)
        self.name = "Charisma"
