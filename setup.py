from setuptools import setup, find_packages

setup(
    name='python_tools',
    version='1.1.0',
    packages=find_packages(),
    package_data={
        '': ['docs/*'],
    },
    include_package_data=True,
    install_requires=[
        'setuptools>=65.5.1',
        'pip>=21.0.0',
        'click>=8.0.0',
        'requests>=2.28.0',
        'python-magic>=0.4.27; platform_system != "Windows"',
        'python-magic-bin>=0.4.14; platform_system == "Windows"',
        'pathlib>=1.0.1; python_version < "3.4"',
        'pywin32>=223; platform_system == "Windows"',
        'pytest>=6.2.5',
        'pytest-cov>=2.12.1',
        'flake8>=3.9.2',
        'PyYAML>=5.4.1',
        'black>=21.9b0',
        'pylint>=2.9.6'
    ],
    entry_points={
        'console_scripts': [
            'python_tools=src.menu:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
