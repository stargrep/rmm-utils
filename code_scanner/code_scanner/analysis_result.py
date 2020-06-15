from datetime import datetime
from pathlib import Path

from code_scanner.const import APP_VERSION


class AnalyzedFile:
    def __init__(self, path: Path, original: [str], filtered: [str]):
        self._path = path
        self._filtered = filtered
        self._original = original

    @property
    def path(self) -> Path:
        return self._path

    @property
    def filtered(self) -> [str]:
        return self._filtered

    @property
    def original(self) -> [str]:
        return self._original

    @path.setter
    def path(self, val) -> None:
        self._path = val

    @filtered.setter
    def filtered(self, val) -> None:
        self._filtered = val

    @original.setter
    def original(self, val) -> None:
        self._original = val

    def __str__(self):
        return str(self._path) + "-" + str(self._filtered)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return (
                self.__class__ == other.__class__ and
                self.__str__() == other.__str__()
        )


class AnalysisResult:

    def __init__(self, files: [AnalyzedFile], root: Path,
                 total_count: int, total_filtered_count: int):
        self._files = files
        self._root = root
        self._total_count = total_count
        self._total_filtered_count = total_filtered_count

    @property
    def files(self) -> [AnalyzedFile]:
        return self._files

    @property
    def root(self) -> Path:
        return self._root

    @property
    def total_count(self) -> int:
        return self._total_count

    @property
    def total_filtered_count(self):
        return self._total_filtered_count

    @files.setter
    def files(self, val) -> None:
        self._files = val

    @root.setter
    def root(self, val) -> None:
        self._root = val

    @total_count.setter
    def total_count(self, val) -> None:
        self._total_count = val

    @total_filtered_count.setter
    def total_filtered_count(self, val) -> None:
        self._total_filtered_count = val

    def __str__(self):
        return str(self._files) + "-" + str(self._total_count) + "-" + str(self._total_filtered_count)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return (
                self.__class__ == other.__class__ and
                self.__str__() == other.__str__()
        )


class TemplateModel:
    """
        _current_time
        _root
        _total_lines
        _logic_total_lines
        _total_lines_no_tests
        _logic_total_lines_no_tests
    """

    def __init__(self, src_result: AnalysisResult, all_result: AnalysisResult):
        self.current_time = datetime.now()
        self.root = src_result.root
        self.python_files = len(src_result.files)
        self.total_files = len(all_result.files)
        self.total_lines = all_result.total_count
        self.logic_lines = all_result.total_filtered_count
        self.src_total_lines = src_result.total_count
        self.src_logic_lines = src_result.total_filtered_count
        self.app_version = APP_VERSION

    def to_dict(self):
        return vars(self)
