from pathlib import Path
APP_VERSION = '0.2.2'

IGNORED_FOLDER_START_PATTERN = (".", "env", "__", "dist", "build")
TEST_FOLDER_START_PATTERN = ("tests")
IGNORED_FILE_START_PATTERN = (".", "license")

CONFIG_SUFFIX = (".json", ".yaml", ".config")
DOCUMENT_SUFFIX = (".json", ".md", ".txt")
PYTHON_SOURCE_SUFFIX = (".py", ".c", ".sql")
JAVA_SOURCE_SUFFIX = (".java", ".sql")

DEFAULT_OUTCOME_PATH = ".__scanned_result.txt"

TEMPLATE_STANDARD_OUTCOME = """

--------------------------------------------------
-------------- start with code_scanner -----------
v{{app_version}}
{{current_time}}

Total Files #: {{total_files}}
Python Source Files #: {{python_files}}

Source Lines (w/o Comments): {{src_total_lines}} ({{src_logic_lines}}) Lines {{src_logic_lines/src_total_lines*100//1}}%
Total Lines (w/o Comments): {{total_lines}} ({{logic_lines}}) Lines {{logic_lines/total_lines*100//1}}% 

Non-tests Ratio (w/o Comments): {{src_total_lines/total_lines*100//1}}% ({{src_logic_lines/logic_lines*100//1}}%)
--------------------- end ------------------------
--------------------------------------------------

"""
