from setuptools import setup
import os
import pathlib

VERSION = '1.0.0'

with open(os.path.json(pathlib.Path(__file__).parent, "README.md"), "r") as fh:
    long_description = fh.read()

setup(
    name='ics_ipa_interface',
    packages=['ics_ipa_interface'],
    version=VERSION,
    description='API used to to allow users to make scripts that work local'
                ' and on wivi server',
    long_description=long_description,
    maintainer='Zaid Nackasha',
    maintainer_email='ZNackasha@intrepidcs.com',
    url='https://github.com/intrepidcs/ics_ipa_interface',
    download_url='https://github.com/intrepidcs/ics_ipa_interface/archive/' +
                 VERSION + '.tar.gz',
    classifiers=['Operating System :: Microsoft :: Windows',
                 'Operating System :: Unix',
                 'Programming Language :: Python :: 3.6']
)

