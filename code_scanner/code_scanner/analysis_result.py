from code_scanner.data_validators import validator


class AnalysisResult:

    def __init__(self):
        pass


    def __str__(self):
        return self._folder + self._name

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.__str__() == other.__str__()
        )