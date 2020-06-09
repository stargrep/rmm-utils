from pathlib import Path


class AnalyzedFile:
    def __init__(self, path: Path, filtered: [str], line_num: int):
        self._path = path
        self._filtered = filtered
        self._line_num = line_num

    @property
    def path(self) -> Path:
        return self._path

    @property
    def filtered(self) -> [str]:
        return self._filtered

    @property
    def line_num(self) -> int:
        return self._line_num

    @path.setter
    def path(self, val) -> None:
        self._path = val

    @filtered.setter
    def filtered(self, val) -> None:
        self._filtered = val

    @line_num.setter
    def line_num(self, val) -> None:
        self._line_num = val

    def __str__(self):
        return str(self._path) + "-" + str(self._line_num)

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

    def __init__(self, files: [AnalyzedFile], total_count: int):
        self._files = files
        self._total_count = total_count

    @property
    def files(self) -> [AnalyzedFile]:
        return self._files

    @property
    def total_count(self) -> int:
        return self._total_count

    @files.setter
    def files(self, val) -> None:
        self._files = val

    @total_count.setter
    def total_count(self, val) -> None:
        self._total_count = val

    def __str__(self):
        return str(self._files) + "-" + str(self._total_count)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return (
                self.__class__ == other.__class__ and
                self.__str__() == other.__str__()
        )
