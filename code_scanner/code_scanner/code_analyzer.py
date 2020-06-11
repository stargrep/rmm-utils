from pathlib import Path

from code_scanner.analysis_result import AnalysisResult, AnalyzedFile
from code_scanner.file_info import FileInfo
from code_scanner.filter_utils import PythonSourceLineFilter


def python_code_counter(root: Path, files: [FileInfo]) -> AnalysisResult:
    filtered_files: [AnalyzedFile] = []
    for file in files:
        original_lines = PythonSourceLineFilter().filter(file.full_name.read_text().split("\n"))
        lines = remove_comments(original_lines)
        filtered_files.append(AnalyzedFile(file.full_name, original_lines, lines))

    return AnalysisResult(filtered_files, root,
                          line_num_sum(filtered_files, "original"),
                          line_num_sum(filtered_files, "filtered"))


def line_num_sum(analyzed_files: [AnalyzedFile], field_name: str) -> int:
    return sum(map(lambda f: len(getattr(f, field_name)), analyzed_files))


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

