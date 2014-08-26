from os.path import abspath, dirname, join, normpath
from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(

    # Basic package information:
    name = 'mdx_collapse',
    version = '0.1.0',
    py_modules = ('mdx_collapse',),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['Markdown>=2.0'],

    # Metadata for PyPI:
    author = 'Alexandre Fonseca',
    author_email = 'alexandrejorgefonseca@gmail.com',
    license = 'Apache',
    url = 'https://github.com/AlexJF/mdx_collapse',
    download_url = 'https://github.com/AlexJF/mdx_collapse/archive/v0.1.0.zip',
    keywords = 'markdown extension collapse',
    description = ('A markdown extension for defining collapsible areas'),
    long_description = long_description
)
