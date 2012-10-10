#!/usr/bin/env python
#
from distutils.core import setup
#from DistUtilsExtra.command import *
import os

setup(name="unity-lens-empathy",
    version="0.1",
    author="Matt Parlette",
    author_email="matthew.parlette@gmail.com",
    url="https://github.com/matthew-parlette/unity-lens-empathy",
    license="GNU General Public License (GPL)",
    data_files=[
        ('share/unity/lenses/empathy', ['empathy.lens']),
        ('share/dbus-1/services', ['unity-lens-empathy.service']),
        ('lib/unity-lens-empathy', ['unity-lens-empathy.py']),
    ])
#cmdclass={"build":  build_extra.build_extra, })

os.system('setsid unity')
