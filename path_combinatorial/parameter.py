__author__ = 'bunny_gg'

class parameter:
    def __init__(self, name="A", interaction="P", comment=""):
        self.name = name
        self.interaction = interaction
        self.comment = comment

    def __str__(self):
        return str(self.name)