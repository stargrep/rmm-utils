import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'code_scanner')))

from code_scanner import hello2

try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []

print(os.path.abspath(os.path.join(os.path.dirname(__file__), 'code_scanner')))
print(user_paths)
hello2.greeting("3")