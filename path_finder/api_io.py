__author__ = 'bunny_gg'

# separator between parameters
spt_between_parameters = "_"


class apiIO:
    def __init__(self, name="", subject="", isOptional= False, string=""):
        self.name = name
        self.subject = subject
        self.isOptional = isOptional
        if string != "":
            self.GetContent(string)


    def GetContent(self, string):
        contentString = string.strip()
        if contentString.upper().endswith("(OPTIONAL)"):
            contentString = contentString[:-10]
            self.isOptional = True
        contentString = contentString.strip()
        ContentList = contentString.split(spt_between_parameters, 1)
        if ContentList.__len__() > 1:
            self.subject = ContentList[0]
            self.name = ContentList[1]
        else:
            self.name = contentString

    def __str__(self):
        return ("subject: " + self.subject + " || " if self.subject!="" else "") + "name: " + self.name + (" || " + "Optional" if self.isOptional else "")


# a = apiIO(string="project_user_id   (optional)    ")
# print a
# b = apiIO(string="password    ")
# print b