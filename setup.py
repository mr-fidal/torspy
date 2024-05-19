from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='torspy',
    version='2.0.2',
    author='Fidal',
    author_email='mrfidal@proton.me',
    description='torspy is a Python package for exploring .onion sites via Tor. It scrapes HTML content, localizes text, and detects hidden directories. With subdomain scanning, torspy enables thorough reconnaissance.',
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
    keywords=[
        'mrfidal',
        'tor',
        'DarkWeb',
        'onion',
        'torspy',
        'scraping',
        'dark web',
        'web scraping',
        'hidden services',
        'privacy',
        'security',
        'beautifulsoup4',
        'requests',
        'python'
    ],
)
