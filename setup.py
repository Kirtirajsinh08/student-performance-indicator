from typing import List
from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of required libraries/frameworks in the project.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = 'Student Performance Indicator',
    version = '0.0.1',
    author = 'Kirtirajsinh',
    author_email = 'kirtirajsinh0804@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)