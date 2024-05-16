from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='torspy',
    version='0.1',
    author='Fidal',
    author_email='mrfidal@proton.me',
    description='Tor onion site scraping tool',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mr-fidal/torspy',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'torspy = torspy.cli:main'
        ]
    },
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
