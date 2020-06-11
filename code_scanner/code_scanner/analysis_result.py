from pathlib import Path


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
    def root(self):
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
