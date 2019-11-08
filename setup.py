from setuptools import setup

setup(
    name='dircompare',
    version='0.1.1',
    author='Adaikalaraj',
    description='Compare two directories',
    long_description=open('README.md').read(),
    url='https://github.com/adaikalaraj/utils',
    zip_safe=False,
    scripts=['dircompare.py'],
    entry_points={
        "console_scripts": [
            "dircompare=dircompare:main",
        ]
    },
)
