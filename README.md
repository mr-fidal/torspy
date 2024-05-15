# torspy

torspy is a Python package for scraping .onion sites using Tor. It provides a simple interface for fetching HTML content from .onion URLs, searching for specific text within the content, and saving the results to a file.

## Installation

You can install torspy via pip:

```
pip install torspy
```

## Usage

### Command-Line Interface

torspy allows you to interact with .onion sites from the command line:

- To display the content of a .onion site:
```
torspy http://example.onion
```

- To save the displayed content to a file:
```
torspy http://example.onion -s file.html
```
  - The `-s` flag indicates saving, and you can specify any file name.

- To search for specific text within the content and save the results to a file:
```
torspy http://example.onion --find "search query" -s search_results.html
```
  - The `--find` flag followed by the search query indicates searching for specific text.
  - The `-s` flag followed by the file name indicates saving the search results.

- To save the content to a specified directory:
```
torspy http://example.onion -s file.html -d /path/to/directory
```
  - The `-d` flag followed by the directory path indicates where to save the file.

- For more information on available options, you can use the `--help` flag:
```
torspy --help
```

### Additional Examples

- Display the content of a .onion site and search for "important information", saving the results to a file named `results.html` in the specified directory:
```
torspy http://example.onion --find "important information" -s results.html -d /path/to/directory
```

- Save the entire HTML content of a .onion site to a file named `full_content.html` in the current directory:
```
torspy http://example.onion -s full_content.html
```

- Display the content of a .onion site and save it to a file named `output.txt` in the current directory:
```
torspy http://example.onion -s output.txt
```

### Using torspy in a Bash Script

You can incorporate torspy into your Bash scripts for automated tasks. Here's an example script that fetches content from a list of .onion URLs and saves it to individual files:

```bash
#!/bin/bash

# List of .onion URLs
urls=("http://example1.onion" "http://example2.onion" "http://example3.onion")

# Loop through each URL
for url in "${urls[@]}"; do
    # Fetch content and save to a file
    torspy "$url" -s "${url##*/}.html"
done
```

### Contributing

If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on GitHub.

## How torspy Works

torspy utilizes the following process to interact with .onion sites:

1. **Checking Site Existence**: It verifies if the .onion site exists and is reachable through the Tor network.

2. **Fetching HTML Content**: It retrieves the HTML content of the .onion site using Tor for anonymity.

3. **Scraping and Searching**: If specified, torspy searches for specific text within the content and extracts matching results.

4. **Saving Results**: Optionally, torspy allows you to save the retrieved content, either the entire HTML or the search results, to a file.

## Code Overview

torspy consists of the following components:

- `check_onion_site(url)`: Checks if the .onion site exists and is reachable.

- `scrape_onion_site(url, search_query, save_file, save_directory)`: Scrapes the .onion site, searches for specific text, and saves results if required.

- `main()`: Handles command-line arguments and invokes the scraping functionality.

## Contributing to torspy

If you're interested in contributing to torspy, you can:

- Report issues encountered while using torspy.
- Suggest new features or enhancements.
- Submit pull requests with improvements or fixes.
- 
