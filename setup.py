# -*- coding: utf-8 -*-

# python std lib
import os

try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import setup

# if you are using vagrant, just delete os.link directly,
# The hard link only saves a little disk space, so you should not care
if os.getenv('USER', '').lower() == 'vagrant':
    del os.link

with open('README.md') as f:
    readme = f.read()
with open(os.path.join('docs', 'release-notes.rst')) as f:
    history = f.read()

setup(
    name="inmar-redis-py-cluster",
    version=os.environ.get("INMAR_REDIS_PY_CLUSTER_VERSION"),
    description="Library for communicating with Redis Clusters. Built on top of redis-py lib",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    author="Johan Andersson",
    author_email="Grokzen@gmail.com",
    maintainer='Johan Andersson',
    maintainer_email='Grokzen@gmail.com',
    packages=find_packages(),
    url='http://github.com/grokzen/redis-py-cluster',
    license='MIT',
    install_requires=[],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    extras_require={},
    keywords=[
        'redis',
        'redis cluster',
    ],
    classifiers=[
        # As from https://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Environment :: Web Environment',
        'Operating System :: POSIX',
        'License :: OSI Approved :: MIT License',
    ]
)
