from datetime import datetime
from pathlib import Path

from code_scanner.analysis_result import AnalysisResult
from jinja2 import Template

from code_scanner.const import DEFAULT_OUTCOME_PATH


def output_to_file(result: AnalysisResult, template_path_str: str,
                   outcome_path: Path = None) -> None:
    if outcome_path is None:
        outcome_path = result.root.joinpath(Path(DEFAULT_OUTCOME_PATH))

    if outcome_path.exists():
        old_content = outcome_path.read_text()
    else:
        old_content = ""

    with open(outcome_path, "w+") as f:
        tm = Template(Path(__file__).parent.joinpath(template_path_str).read_text())
        f.write(render_result(result, tm) + old_content)


def render_result(result: AnalysisResult, tm: Template) -> str:
    model = {
        "current_time": datetime.now(),
        "current_path": result.root,
        "filtered_total_lines": result.total_filtered_count,
        "total_lines": result.total_count
    }
    return tm.render(model)

