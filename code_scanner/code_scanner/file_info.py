from code_scanner.data_validators import validator


class FileInfo:

    def __init__(self, file_type, name='', folder='', is_folder=False):
        self._name = name
        self._folder = folder
        self._file_type = file_type
        self._is_folder = is_folder

    @property
    def name(self):
        return self._name

    @property
    def folder(self):
        return self._folder

    @property
    def file_type(self):
        return self._file_type

    @property
    def is_folder(self):
        return self._is_folder

    @name.setter
    @validator(lambda field: field is None or len(field) == 0, ValueError("name cannot be empty or "))
    def name(self, val):
        self._name = val

    @folder.setter
    def folder(self, val):
        self._folder = val

    @file_type.setter
    def file_type(self, val):
        self._file_type = val

    @is_folder.setter
    def is_folder(self, val):
        self._is_folder = val

    def __str__(self):
        return self._file_type.name + "-" + self._folder + self._name

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return (
                self.__class__ == other.__class__ and
                self.__str__() == other.__str__()
        )
