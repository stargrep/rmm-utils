from pathlib import Path

from code_scanner.analysis_result import AnalysisResult, TemplateModel
from jinja2 import Template

from code_scanner.const import DEFAULT_OUTCOME_PATH


def output_to_file(src_result: AnalysisResult,
                   result: AnalysisResult,
                   template_str: str,
                   outcome_path: Path = None) -> None:
    if outcome_path is None:
        outcome_path = result.root.joinpath(Path(DEFAULT_OUTCOME_PATH))

    if outcome_path.exists():
        old_content = outcome_path.read_text()
    else:
        old_content = ""

    with open(str(outcome_path), "w+") as f:
        tm = Template(template_str)
        f.write(render_results(src_result, result, tm) + old_content)


def render_results(src_result: AnalysisResult, result: AnalysisResult, tm: Template) -> str:
    return tm.render(TemplateModel(src_result, result).to_dict())

