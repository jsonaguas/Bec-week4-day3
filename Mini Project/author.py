class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def biography(self):
        return self.__biography

    @biography.setter
    def biography(self, value):
        self.__biography = value

    def __str__(self):
        return f"Author: {self.__name}, Biography: {self.__biography}"
    
    