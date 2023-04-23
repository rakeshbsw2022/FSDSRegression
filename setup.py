from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    file=open(file_path,"r")
    file_data=file.readlines()
    for req in file_data:
        if req=="-e ." in file_data:
            continue
        requirements.append(req.replace("\n",""))
    return requirements




setup(
    name="RegressorProject",
    version="0.0.1",
    author="Rakesh",
    author_email="rakeshbsw2022@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()

)