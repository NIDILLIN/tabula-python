from setuptools import setup, find_packages


setup(name='tabula-python',
      version='0.1',
      url='https://github.com/nidillin/tabula-python',
      license='MIT',
      author='Nico Dillinger',
      author_email='writebutread@outlook.com',
      description='Tabula-java wrapper on python',
      packages=find_packages(),
      long_description=open('README.md').read(),
      zip_safe=False)