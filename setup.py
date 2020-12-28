from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="sozu",
    version="0.0.1",
    description="cross-platform threat modeling tool",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/awillis/sozu",
    project_urls={
        "Bug Reports": "https://github.com/awillis/sozu/issues",
        "Source": "https://github.com/awillis/sozu"
    },
    author="Alan Willis",
    author_email="alan@amekoshi.com",
    license="Apache-2.0",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.9",
        "Topic :: Security"
    ],
    keywords="threat model infosec security dfd",
    packages=find_packages(include=['sozu']),
    python_requires=">=3.9, <4",
    include_package_data=True,
    install_requires=[],
    data_files=[],
    entry_points={
        'console_scripts': [
            'sozu=sozu.console:main'
        ],
        'gui_scripts': [
            'sozu=sozu.visual:main'
        ]
    }
)
