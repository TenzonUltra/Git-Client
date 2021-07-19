#Command setup file for the git client

from setuptools import setup

setup (name = 'gitcl',
       version = '1.0',
       packages = ['gitcl'],
       entry_points = {
           'console_scripts' : [
               'gitcl = gitcly.cli:main'
           ]
       })
