""" setup.py
REPOSITORY:
  https://github.com/DavidJLambert/Python-Universal-DB-Client

SUMMARY:
  Command-line universal database client.

VERSION:
  0.2.3

AUTHOR:
  David J. Lambert

DATE:
  May 31, 2019
"""

from distutils.core import setup

with open("README.rst", 'r') as f:
    long_description = f.read()

setup(
    author='David J. Lambert',
    author_email='David5Lambert7@gmail.com',
    description='Python Universal Database Client',
    license='MIT License',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    name='universalClient',
    py_modules=["universalClient"],
    url='https://github.com/DavidJLambert/Python-Universal-DB-Client',
    version='0.2.3',
    install_requires=[
        cx_Oracle,
        ibm_db,
        psutil,
        psycopg2,
        pymssql,
        pymysql,
        pyodbc,
        pytest,
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
		'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Database :: Front-Ends',
    ],
)
