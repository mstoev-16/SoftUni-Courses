class Component:
    def __init__(self, name):
        self.name = name
        self.parent = None

    def move(self, new_path):
        new_folder = get_path(new_path)
        del self.parent.children[self.name]
        new_folder.children[self.name] = self
        self.parent = new_folder

    def delete(self):
        del self.parent.children[self.name]


class Folder (Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_child(self, child):
        self.parent = self
        self.children[child.name] = child


class File (Component):
    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = contents


root = Folder('')


def get_path(path):
    names = path.split('/')[1:]
    node = root
    for name in names:
        node = node.children[name]
    return node


# from abc import ABC, abstractmethod
#
#
# class DataSource(ABC):
#     @abstractmethod
#     def writeData(self, data):
#         pass
#
#     @abstractmethod
#     def readData(self) -> str:
#         pass
#
#
# class FileDataSource(DataSource):
#     def __init__(self, filename):
#         self._file = filename
#
#     def writeData(self, data):
#         with open(self._file, 'w') as file:
#             file.write(data)
#
#     def readData(self) -> str:
#         with open(self._file, 'r') as file:
#             return file.readline()
#
#
# class EncryptionDecorator(DataSource):
#     def __init__(self, writer):
#         self.writer = writer
#
#     def writeData(self, data):
#         # encrypt the data
#         data = f"Encrypted {data}"
#         # pass encrypted data to wrapper
#         self.writer.writeData(data)
#
#     def readData(self) -> str:
#         # get encrypted data
#         line = self.writer.readData()
#         # decrypt it
#         new_line = line.replace('Encrypted ', '')
#         # return it
#         return new_line
#
#
# # file_data1 = FileDataSource('example_file.txt')
# # file_data1.writeData('hello!')
# # print(file_data1.readData())
#
# encrypted_hello = EncryptionDecorator(FileDataSource('example_file.txt'))
# encrypted_hello.writeData('hello!')
# print(encrypted_hello.readData())