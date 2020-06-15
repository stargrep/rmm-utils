from pathlib import Path

import pytest
from code_scanner.output_utils import output_to_file

from code_scanner.analysis_result import AnalysisResult


@pytest.fixture
def result(tmp_test_folder) -> AnalysisResult:
    return AnalysisResult([], tmp_test_folder.joinpath("result-root-folder"), 20, 10)


@pytest.fixture
def src_result(tmp_test_folder) -> AnalysisResult:
    return AnalysisResult([], tmp_test_folder.joinpath("src-root-folder"), 16, 7)


@pytest.fixture
def output_file(tmp_test_folder) -> Path:
    return tmp_test_folder.joinpath("output.txt")


@pytest.fixture
def simple_template_str() -> str:
    return """
    {{current_time}}
    {{current_path}}
    Source Lines : {{src_total_lines}} ({{src_logic_lines}}) Lines {{src_logic_lines/src_total_lines*100//1}}%
    Total Lines : {{total_lines}} ({{logic_lines}}) Lines {{logic_lines/total_lines*100//1}}%
    Non-tests Ratio : {{src_total_lines/total_lines*100//1}}% ({{src_logic_lines/logic_lines*100//1}}%)
    """


def test_output_to_file(src_result, result, simple_template_str, output_file) -> None:
    result = output_to_file(src_result, result, simple_template_str, output_file)
    assert result == output_file.read_text()
    output_file.unlink()
