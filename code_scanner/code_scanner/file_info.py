from code_scanner.data_validators import validator
from code_scanner.enums import FileType


class FileInfo:

    def __init__(self, full_name, file_type=FileType.UNKNOWN):
        """
        :param full_name:   Absolute folder without file, Path
        :param file_type:   Enum FileType
        """
        self._full_name = full_name
        self._file_type = file_type

    @property
    def full_name(self):
        return self._full_name

    @property
    def file_type(self):
        return self._file_type

    @full_name.setter
    @validator(lambda field: field is None or len(str(field)) == 0, ValueError("name cannot be empty or "))
    def full_name(self, val):
        self._full_name = val

    @file_type.setter
    def file_type(self, val):
        self._file_type = val

    def __str__(self):
        return self._file_type.name + "-" + str(self._full_name)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return (
                self.__class__ == other.__class__ and
                self.__str__() == other.__str__()
        )
