from setuptools import setup,find_packages
from typing import List

HYPEN_e = "-e ."


def get_requirements(filepath:str) -> List[str]:
    requirements = []

    with open(filepath,"r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n","") for i in requirements]

        if HYPEN_e in requirements:
            requirements.remove(HYPEN_e)


setup(name='ML_Project_Pipeline',
      version='0.0.1',
      description='Machine Learning Pipeline Project',
      author='Saurav Sabu',
      author_email='saurav.sabu9@gmail.com',
      packages=find_packages(),
      install_requires = get_requirements("requirements.txt")
     )




