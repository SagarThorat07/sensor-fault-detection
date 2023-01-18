from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    This function will return a list of requirements


    """
    requirement_list:List[str] = []
    with open("requirements.txt") as f:
        for line in f:
            requirement_list.append(line.strip())
  
    return requirement_list
      
setup(
    name = "sensor",
    version = "0.0.1",
    author = "sagar",
    author_email = "sagarthorat53@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(), #['pymongo==4.2.0',]
)