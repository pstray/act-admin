"""Setup script for the python-act library module"""

from os import path

from setuptools import setup

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), "rb") as f:
    long_description = f.read().decode("utf-8")

setup(
    name="act-admin",
    version="2.0.2",
    author="mnemonic AS",
    zip_safe=True,
    author_email="opensource@mnemonic.no",
    description="ACT admin tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="ACT, mnemonic",
    entry_points={
        "console_scripts": [
            "act-types = act.admin.types:main",
            "act-origin = act.admin.origin:main",
        ]
    },
    packages=["act.admin"],
    # https://packaging.python.org/guides/packaging-namespace-packages/#pkgutil-style-namespace-packages
    # __init__.py under all packages under in the act namespace must contain exactly string:
    # __path__ = __import__('pkgutil').extend_path(__path__, __name__)
    namespace_packages=["act"],
    url="https://github.com/mnemonic-no/act-workers",
    install_requires=["act-api>=2.0.0,<3.0.0", "act-types>=2.0.0,<3.0.0"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: ISC License (ISCL)",
    ],
)
