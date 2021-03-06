import re
from setuptools import setup, find_packages

# import multiprocessing to avoid this bug (http://bugs.python.org/issue15881#msg170215)
import multiprocessing
assert multiprocessing


def get_version():
    """
    Extracts the version number from the version.py file.
    """
    VERSION_FILE = 'entity_history/version.py'
    mo = re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', open(VERSION_FILE, 'rt').read(), re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError('Unable to find version string in {0}.'.format(VERSION_FILE))


setup(
    name='django-entity-history',
    version=get_version(),
    description='History about Django Entities',
    long_description=open('README.rst').read(),
    url='https://github.com/ambitioninc/django-entity-history',
    author='Wes Kendall',
    author_email='opensource@ambition.com',
    keywords='',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
    ],
    license='MIT',
    install_requires=[
        'Django>=1.11',
        'django-entity>=2.0.0',
        'psycopg2'
    ],
    tests_require=[
        'django-nose>=1.4',
        'mock>=1.0.1',
        'coverage>=3.7.1',
        'django-dynamic-fixture',
    ],
    test_suite='run_tests.run',
    include_package_data=True,
    zip_safe=False,
)
