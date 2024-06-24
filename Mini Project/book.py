class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__availability_status = True

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    @property
    def publication_date(self):
        return self.__publication_date

    @publication_date.setter
    def publication_date(self, value):
        self.__publication_date = value

    @property
    def availability_status(self):
        return self.__availability_status

    @availability_status.setter
    def availability_status(self, value):
        self.__availability_status = value

    def __str__(self):
        return f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, Publication Date: {self.__publication_date}, Available: {'Yes' if self.__availability_status else 'No'}"
    
    