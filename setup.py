import os
import re
import codecs
from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'rb').read().decode('utf-8')


def find_version(*path_parts):
    version_file = read(*path_parts)
    version_match = re.search("^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-maintenancemode',
    version=find_version('maintenancemode', '__init__.py'),
    description=('Django-maintenancemode allows you to '
                 'temporary shutdown your site for maintenance work'),
    long_description='\n\n'.join([read('README.rst'), read('CHANGES')]),
    author='Remco Wendt',
    author_email='remco@maykinmedia.nl',
    license="BSD",
    platforms=["any"],
    url='https://github.com/21strun/django-maintenancemode',
    packages=[
        'maintenancemode',
        'maintenancemode.conf',
        'maintenancemode.conf.settings',
        'maintenancemode.conf.urls',
        'maintenancemode.management',
        'maintenancemode.management.commands',
        'maintenancemode.tests',
        'maintenancemode.views',
    ],
    package_data={
        'maintenancemode': [
            'tests/templates/503.html',
            'fixtures/initial_data.json',
        ],
    },
    classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Utilities',
    ],
)
