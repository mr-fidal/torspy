from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='torspy',
    version='1.0.2',
    author='Fidal',
    author_email='mrfidal@proton.me',
    description='torspy is a robust Python package fortified with powerful algorithms, designed for seamless exploration of .onion sites via the Tor network. Its arsenal includes adept scraping of HTML from .onion URLs, precise text localization within the acquired content, and proficient storage of findings. Moreover, torspy boasts formidable subdomain scanning capabilities, enabling thorough reconnaissance across diverse subdomains. Additionally, it excels at detecting hidden directories, further enhancing its efficacy in navigating and extracting valuable information from the depths of the dark web.',
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
