from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT ='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this functio will return list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements = requirements.remove(HYPHEN_E_DOT)
    return requirements



setup(
name ='EndToEndMlProject',
version='0.0.1',
author = 'Deepak',
author_email='deepaksinghnitsurat@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')

)
