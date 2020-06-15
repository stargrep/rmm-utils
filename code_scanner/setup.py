# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py
from setuptools import setup, find_packages

with open('LICENSE') as f:
    lis = f.read()

with open('README.md') as f:
    readme = f.read()

setup(
    name='code_scanner',
    version='0.2.1',
    description='Code Scanner for local run',
    long_description=readme,
    author='mike',
    author_email='mikenyc1207@gmail.com',
    url='https://github.com/stargrep/rmm-utils/tree/master/code_scanner',
    license=lis,
    packages=find_packages(exclude=('tests', 'docs')),
    data_files=[
        ('doc', ['documents.md', 'LICENSE', 'requirements.txt']),
        ('commands', ['Makefile'])
    ],
)

# import os
# from setuptools import setup, Command
#
# class CleanCommand(Command):
#     """Custom clean command to tidy up the project root."""
#     user_options = []
#     def initialize_options(self):
#         pass
#     def finalize_options(self):
#         pass
#     def run(self):
#         os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')
#
# # Further down when you call setup()
# setup(
#     # ... Other setup options
#     cmdclass={
#         'clean': CleanCommand,
#     }
# )
