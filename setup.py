from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1',
    packages=find_packages(),
    package_data={
        '': ['docs/*'],
    },
    include_package_data=True,
    install_requires=[
        // your dependencies here
    ],
)
