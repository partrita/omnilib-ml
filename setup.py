from setuptools import find_packages, setup

setup(
    name="nbfitnessml",
    version="0.1",
    packages=['nabstab'] + find_packages(exclude=['tests*']),
    install_requires=[],
    extras_require={
        'dev': [
            'notebook',  # Jupyter notebook is typically a development dependency
        ],
    },
)