from pathlib import Path

from code_scanner.data_validators import validator
from code_scanner.enums import FileType


class FileInfo:

    def __init__(self, full_name: Path, file_type: FileType = FileType.UNKNOWN):
        """
        :param full_name:   Absolute folder without file, Path
        :param file_type:   Enum FileType
        """
        self._full_name = full_name
        self._file_type = file_type

    @property
    def full_name(self) -> Path:
        return self._full_name

    @property
    def file_type(self) -> FileType:
        return self._file_type

    @full_name.setter
    @validator(lambda field: field is None or len(str(field)) == 0, ValueError("name cannot be empty or "))
    def full_name(self, val) -> None:
        self._full_name = val

    @file_type.setter
    def file_type(self, val) -> None:
        self._file_type = val

    def __str__(self) -> str:
        return self._file_type.name + "-" + str(self._full_name)

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return hash(self.__str__())

    def __eq__(self, other) -> bool:
        return (
                self.__class__ == other.__class__ and
                self.__str__() == other.__str__()
        )
