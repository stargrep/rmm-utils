from pathlib import Path
import os

from code_scanner.file_utils import retrieve_all_folders, retrieve_files

from code_scanner.code_analyzer import python_code_counter
from code_scanner.filter_utils import PythonSourceFileFilter, PythonFolderFilter, GeneralFolderFilter
from code_scanner.output_utils import output_to_file

root = Path(os.getcwd())
folders = retrieve_all_folders(root, [GeneralFolderFilter()])
path_info_list = retrieve_files(folders, [PythonSourceFileFilter()])
print(root)
print(folders)
print(path_info_list)
result = python_code_counter(root, path_info_list)

print(result)

output_to_file(result, "templates/outcome_template.txt")
