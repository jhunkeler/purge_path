import os
import sys
from setuptools import setup, find_packages
sys.path.insert(1, 'relic')

import relic.release
from setuptools import setup

NAME = 'purge_path'
version = relic.release.get_info()
relic.release.write_template(version, NAME)

entry_points = {}
package_data = {}

entry_points['console_scripts'] = [
    'purge_path = purge_path.purge_path:main',
]

package_data[''] = ['*.txt', '*.md']


setup(
    name=NAME,
    version=version.pep386,
    description='A small PATH manipulator',
    author='Joseph Hunkeler',
    author_email='jhunk@stsci.edu',
    license='BSD',
    url='http://github.com/jhunkeler/purge_path',
    download_url='',
    use_2to3=True,
    packages=find_packages(),
    entry_points=entry_points,
    package_data=package_data,
)
