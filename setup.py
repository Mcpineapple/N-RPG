# Fichier de configuration permettant de transformer le projet en module

from setuptools import setup
import os

thelibFolder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')
install_requires = []
if os.path.isfile(thelibFolder):
    with open(thelibFolder) as f:
        install_requires = f.read().splitlines()

setup(name='nrpg',
        version='0.42',
        description='Module nécessaire au fonctionnement du N-RPG',
        packages=['nrpg'],
        install_requires=install_requires
        )
