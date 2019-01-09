import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='softdelete',
    version='0.3.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A simple Django app to add soft-delete functionality to\
                 desired models using datetimes',
    long_description=README,
    url='https://github.com/ShaneRich5/django-softdelete-it',
    author='Shaifali Agrawal',
    author_email='agrawalshaifali09@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
    ],
)
