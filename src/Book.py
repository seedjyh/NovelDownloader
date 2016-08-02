__author__ = 'jiangyh'

class Book:
    def __init__(self, title, author, chapter_list):
        self.__title = title
        self.__author = author
        self.__chapter_list = chapter_list

    def title(self):
        return self.__title

    def author(self):
        return self.__author

    def WriteToFile(self, file_path):
        f = open(file_path, 'wb')
        f.write(self.__title + '\n')
        f.write(self.__author + '\n')
        for ch in self.__chapter_list:
            f.write(ch.title() + '\n')
            f.write(ch.content() + '\n')
        f.close()
