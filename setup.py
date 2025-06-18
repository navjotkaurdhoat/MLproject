from setuptools import find_packages,setup
from typing import list

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str) ->list[str]:

    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

## \n was replaced with blankspace beacuse when setup.py will read using readline()
## requirements.txt there will be \n to go to the next line

setup(
name='MLproject',
version='0.0.1',
author='Navjot',
author_email='navjotkaurdhoat@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt') 

)