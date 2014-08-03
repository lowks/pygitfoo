from distutils.core import setup

setup(
    name='PyGitFoo',
    version='0.4.2dev',
    author='Luis Miranda',
    author_email='luistm@gmail.com',
    packages=['pygitfoo', ],
    license='MIT license',
    long_description=open('README.rst').read(),
    description='Git wrapper written in python.',
    url='https://github.com/luistm/pygitfoo/',
)
