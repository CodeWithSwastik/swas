from sys import argv
from setuptools import setup, find_packages


if argv[1] in ('install', 'build', 'sdist', 'bdist_wheel'):
  pass #will add file assoc soon  

 
classifiers = [
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='swas',
  version='1.8.3',
  description='A Progamming Language.',
  long_description=open('README.md').read(),
  long_description_content_type = "text/markdown",
  url = "https://github.com/CodeWithSwastik/swas", 
  project_urls={
   "Documentation": "https://github.com/CodeWithSwastik/swas/tree/main#getting-started",
   "Issue tracker": "https://github.com/CodeWithSwastik/swas/issues",
   },
  author='Swas.py',
  author_email='cwswas.py@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='swas,language,swas lang', 
  packages=find_packages(),
  install_requires= ['sly', 'click'],
  python_requires='>=3.6'
)