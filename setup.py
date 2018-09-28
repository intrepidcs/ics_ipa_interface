from setuptools import setup

VERSION = '0.0.0.1'

setup(
    name='ics_ipa_interface',
    packages=['ics_ipa_interface'],
    version=VERSION,
    description='API used to to allow users to make scripts that work local'
                ' and on wivi server',
    maintainer='Zaid Nackasha',
    maintainer_email='ZNackasha@intrepidcs.com',
    # url='https://github.com/intrepidcs/ICS_IPA',
    # download_url='https://github.com/intrepidcs/ICS_IPA/archive/' + VERSION +
    #              '.tar.gz',
    classifiers=['Operating System :: Microsoft :: Windows',
                 'Operating System :: Unix',
                 'Programming Language :: Python :: 3.6']
)
