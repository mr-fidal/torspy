# torspy

torspy is a Python package for scraping .onion sites using Tor. It provides a simple interface for fetching HTML content from .onion URLs, searching for specific text within the content, and saving the results to a file.

## Installation

You can install torspy via pip:

```sh
pip install torspy
```

## Usage

<h2>Command-Line Interface</h2>
<p>You can use torspy from the command line by running the torspy command followed by the URL of the .onion site you want to scrape. Optionally, you can specify a search query and file-saving options.</p>

```sh
torspy http://example.onion --find "search query" -s output.txt
```

<p>For more information on available options, you can use the `--help` flag:</p>

```sh
torspy --help
```

### Contributing

<p>If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on GitHub.</p>
