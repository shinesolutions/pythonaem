import os
import setuptools
from setuptools import sic
import yaml

readme_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "README.md")
with open(readme_file, "r") as readme_fh:
    readme = readme_fh.read()

info_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "conf/info.yaml")
with open(info_file, "r") as info_fh:
    info = yaml.load(info_fh, Loader=yaml.FullLoader)

setuptools.setup(
    name="pythonaem",
    version=sic(info["version"]),
    author="Shine Solutions",
    author_email="opensource@shinesolutions.com",
    keywords=["Adobe Experience Manager (AEM) API"],
    description="Python client for AEM API",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/shinesolutions/pythonaem",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pyyaml==5.4.1",
        "swaggeraem==1.2.0"
    ],
)