__author__ = 'jiangyh'

class FileTool:
    def LoadFile(self, file_path):
        file_object = open(file_path, 'rb')
        data = file_object.read()
        file_object.close()
        return data
