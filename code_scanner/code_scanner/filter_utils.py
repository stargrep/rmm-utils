from abc import ABCMeta, abstractmethod
from pathlib import Path

from code_scanner.const import IGNORED_FOLDER_START_PATTERN, IGNORED_FILE_START_PATTERN, PYTHON_SOURCE_SUFFIX


class IFileFilter(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'filter') and
                callable(subclass.filter) or
                NotImplemented)

    @abstractmethod
    def valid(self, path: Path) -> bool:
        """Check if a path is valid"""
        raise NotImplementedError

    def filter(self, paths: [Path]) -> [Path]:
        """Filter function for path obj"""
        return tuple(filter(self.valid, paths))


class GeneralFolderFilter(IFileFilter):

    def valid(self, path: Path) -> bool:
        """
        Checks name and type for a folder.
        :param path:
        :return:
        """
        return path.is_dir() and \
            not path.name.startswith(IGNORED_FOLDER_START_PATTERN)


class PythonFolderFilter(GeneralFolderFilter):

    def valid(self, path: Path) -> bool:
        paths = list(path.glob("*"))
        if not super().valid(path) or len(paths) == 0:
            return False
        return True


class GeneralFileFilter(IFileFilter):

    def valid(self, path: Path) -> bool:
        return path.is_file() and \
            not path.name.lower().startswith(IGNORED_FILE_START_PATTERN)


class PythonSourceFileFilter(GeneralFileFilter):

    def valid(self, path: Path) -> bool:
        return super().valid(path) and path.suffix.lower() in PYTHON_SOURCE_SUFFIX

