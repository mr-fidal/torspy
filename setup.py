from setuptools import setup, find_packages

setup(
    name='torspy',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'torspy=torspy.scraper:main',
        ],
    },
    description='A package for scraping .onion sites using Tor',
    author='fidal',
    author_email='mrfidal@proton.me',
    url='https://github.com/mr-fidal/torspy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
