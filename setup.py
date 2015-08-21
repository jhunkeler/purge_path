import os
from setuptools import setup, find_packages
from purge_path.extern.version import get_git_version

entry_points = {}
package_data = {}

entry_points['console_scripts'] = [
    'purge_path = purge_path.purge_path:main',
]

package_data[''] = ['*.txt', '*.md']
version_py = os.path.join('purge_path', 'version.py')

#Omit git hash and let setuptools add a valid build number
git_version = get_git_version()
if git_version.rfind('-') != -1:
    git_version = git_version[:git_version.rfind('-')]


with open(version_py, 'w+') as version_data:
    version_data.write('__version__ = "{0}"\n'.format(git_version))

NAME = 'purge_path'
VERSION = git_version

setup(
    name=NAME,
    version=VERSION,
    description='A small PATH manipulator',
    provides=[NAME],
    author='Joseph Hunkeler',
    author_email='jhunk@stsci.edu',
    license='BSD',
    url='http://bitbucket.org/jhunkeler/purge_path',
    download_url='',
    use_2to3=True,
    packages=find_packages(),
    entry_points=entry_points,
    package_data=package_data,
)
