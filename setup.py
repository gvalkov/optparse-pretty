#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup
from optparse_mooi import __version__, __author__, __license__

from os.path import abspath, dirname, join
here = abspath(dirname(__file__))

classifiers = (
    'Environment :: Console',
    'Topic :: Utilities',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'License :: OSI Approved :: BSD License',
    'Development Status :: 4 - Beta',
    #'Development Status :: 5 - Production/Stable',
    #'Development Status :: 6 - Mature',
    #'Development Status :: 7 - Inactive',
)

kw = {
    'name':              'optparse-pretty',
    'version':           __version__,
    'description':       'A more compact help formatter for optparse',
    'long_description':  open(join(here, 'README.rst')).read(),
    'author':            __author__,
    'author_email':      'georgi.t.valkov@gmail.com',
    'license':           __license__,
    'keywords':          'optparse formatter cmd',
    'classifiers':       classifiers,
    'url':               'https://github.com/gvalkov/optparse-pretty',
    'py_modules':        ['optparse_mooi'],
    'zip_safe':          True,
}

if __name__ == '__main__':
    setup(**kw)
