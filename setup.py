"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['lokaverkefni.py']
DATA_FILES = ['img', 'snd']
OPTIONS = {'iconfile': 'app-icon.icns',
           'plist': {
                'CFBundleIdentifier': 'com.reyniraron.PizzaInvaders',
                'NSHumanReadableCopyright': '© 2018 Reynir Aron',
                'CFBundleVersion': "1.0.1",
                'CFBundleShortVersionString': "1.0.1",
           }}

setup(
    name='Pizza Invaders',
    url='https://github.com/reyniraron/pizza-invaders',
    author='Reynir Aron',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app', 'pygame'],
)