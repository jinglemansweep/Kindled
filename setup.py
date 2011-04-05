import os
from distutils.core import setup

setup(
    name = "kindled",
    version = "0.11",
    author = "JingleManSweep",
    author_email = "jinglemansweep@gmail.com",
    description = "Calibre Distribution System for Kindle",
    url = "http://github.com/jingleman/kindled",
    packages = [],
    scripts = [os.path.join("bin", "kindled"),],
    include_package_data = True,
    setup_requires=[]
)
