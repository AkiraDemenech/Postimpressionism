# -*- coding: utf-8 -*-
import setuptools

troca = 'at [PyPI](https://pypi.org/project/postimpressionism/) and (obviously) via PIP installation.'
por = 'test versions at [https://test.pypi.org/project/postimpressionism](https://test.pypi.org/project/postimpressionism/)'

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='postimpressionism',
    version='0.1.7',
    url='https://github.com/AkiraDemenech/Postimpressionism',
    license='MIT License',
    author='Akira Demenech',
    author_email='akira.demenech@gmail.com',
    keywords='art image postproduction postimpressionism',
    description="An Art Exploration Package based on Modernist Avant-garde as a Post-Production of Digital Contemporary Art;",
    long_description=long_description.replace(troca,por),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=['matplotlib', 'numpy', 'Pillow'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)