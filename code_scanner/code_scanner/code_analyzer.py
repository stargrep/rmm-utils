from code_scanner.analysis_result import AnalysisResult, AnalyzedFile
from code_scanner.file_info import FileInfo
from code_scanner.filter_utils import PythonSourceLineFilter


def python_code_counter(files: [FileInfo]) -> AnalysisResult:
    filtered_files: [AnalyzedFile] = []
    for file in files:
        lines = remove_comments(PythonSourceLineFilter().filter(file.full_name.read_text().split("\n")))
        filtered_files.append(AnalyzedFile(file.full_name, lines, len(lines)))

    return AnalysisResult(filtered_files, sum(map(lambda f: f.line_num, filtered_files)))


def remove_comments(lines: [str]) -> [str]:
    """
    line starts with """ ''' or #
    line ends with ''' """
    :param lines:
    :return:
    """
    in_comment = False
    extracted = []
    for line in lines:
        trimmed = line.lower().strip()
        if trimmed == '' or trimmed.startswith("#") or trimmed.startswith("print"):
            continue

        if trimmed.startswith("'''") or trimmed.startswith('"""'):
            in_comment = True

        if not in_comment:
            extracted.append(line)

        if len(trimmed) > 3 and (trimmed.endswith("'''") or trimmed.endswith('"""')):
            in_comment = False
    return extracted

