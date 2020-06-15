from pathlib import Path
import os

from code_scanner.const import TEMPLATE_STANDARD_OUTCOME
from code_scanner.file_utils import retrieve_all_folders, retrieve_files

from code_scanner.code_analyzer import python_code_counter
from code_scanner.filter_utils import PythonSourceFileFilter, SourceCodeFolderFilter, GeneralFolderFilter
from code_scanner.output_utils import output_to_file

# TODO: update to Path().cwd()
root = Path(os.getcwd())
current_path = Path(__file__).parent
print("Root path -", root)

folders = retrieve_all_folders(root, [GeneralFolderFilter()])
path_info_list = retrieve_files(folders, [PythonSourceFileFilter()])
# print(folders)
# print(path_info_list)
result = python_code_counter(root, path_info_list)

src_folders = retrieve_all_folders(root, [GeneralFolderFilter(), SourceCodeFolderFilter()])
src_list = retrieve_files(src_folders, [PythonSourceFileFilter()])
src_result = python_code_counter(root, src_list)
outputs = output_to_file(src_result, result, TEMPLATE_STANDARD_OUTCOME)

print(outputs)
