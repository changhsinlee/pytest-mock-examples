from setuptools import setup

setup(name='mock_examples',
      version='0.1',
      description='Examples for using pytest mock',
      author='Chang Hsin Lee',
      license='MIT',
      packages=['mock_examples', 'pytest', 'pytest-mock'],
      python_requires='>=3.5',
      zip_safe=False)
