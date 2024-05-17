# torspy

torspy is a Python package designed for scraping .onion sites using the Tor network. It offers a straightforward interface for retrieving HTML content from .onion URLs, searching for specific text within that content, and saving the results to a file. Additionally, torspy is capable of detecting hidden directories.

## Installation

You can install torspy via pip:

```sh
pip install torspy
```
## Usage
### Command-Line Interface
torspy allows you to interact with .onion sites from the command line:

- To display the content of a .onion site:
```sh
torspy http://example.onion
```
- To save the displayed content to a file:
```sh
torspy http://example.onion -s file.html
```
- The `-s` flag indicates saving, and you can specify any file name.

- To search for specific text within the content and save the results to a file:
```sh
torspy http://example.onion --find "search query" -s search_results.html
```
- The `--find` flag followed by the search query indicates searching for specific text.

- The `-s` flag followed by the file name indicates saving the search results.

- To save the content to a specified directory:
```sh
torspy http://example.onion -s file.html -d /path/to/directory
```
- The `-d` flag followed by the directory path indicates where to save the file.

- To check for directories listed in a file:
```sh
torspy http://example.onion --dir directories.txt
```
- The `--dir` flag followed by the file name checks for directories listed in the specified file.
- Move it all to another file
```sh
torspy http://example.onion --dir directories.txt -s output.txt
```
- For more information on available options, you can use the `--help` flag:
```sh
torspy --help
```
### Additional Examples
- Display the content of a .onion site and search for "important information", saving the results to a file named `results.html` in the specified directory:
```sh
torspy http://example.onion --find "important information" -s results.html -d /path/to/directory
```
- Save the entire HTML content of a .onion site to a file named `full_content.html` in the current directory:
```sh
torspy http://example.onion -s full_content.html
```
- Display the content of a .onion site and save it to a file named `output.txt` in the current directory:
```sh
torspy http://example.onion -s output.txt
```
### Using torspy in a Bash Script
- You can incorporate torspy into your Bash scripts for automated tasks. Here's an example script that fetches content from a list of .onion URLs and saves it to individual files:
```sh
#!/bin/bash

# List of .onion URLs
urls=("http://example1.onion" "http://example2.onion" "http://example3.onion")

# Loop through each URL
for url in "${urls[@]}"; do
    # Fetch content and save to a file
    torspy "$url" -s "${url##*/}.html"
done
```
### Integrating torspy with Other Languages
### Ruby
- You can call the torspy command-line tool from Ruby using the system method:
```ruby
system("torspy http://example.onion -s output.html")
```
### Python
- You can use the subprocess module to call torspy from a Python script:
```sh
import subprocess

subprocess.run(["torspy", "http://example.onion", "-s", "output.html"])
```
### PHP
- You can use the shell_exec function to call torspy from PHP:
```php
<?php
shell_exec("torspy http://example.onion -s output.html");
?>
```
### Node.js
- You can use the `child_process` module to call torspy from Node.js:
```js
const { exec } = require('child_process');

exec('torspy http://example.onion -s output.html', (error, stdout, stderr) => {
    if (error) {
        console.error(`Error: ${error.message}`);
        return;
    }
    if (stderr) {
        console.error(`Stderr: ${stderr}`);
        return;
    }
    console.log(`Output: ${stdout}`);
});
```
### How torspy Works
torspy utilizes the following process to interact with .onion sites:

<li><b>Checking Site Existence:</b> It verifies if the .onion site exists and is reachable through the Tor network.</li>

<li><b></b>Fetching HTML Content: </b>It retrieves the HTML content of the .onion site using Tor for anonymity.</li>

<li><b></b>Scraping and Searching:</b> If specified, torspy searches for specific text within the content and extracts matching results.</li>

<li><b>Saving Results: </b>Optionally, torspy allows you to save the retrieved content, either the entire HTML or the search results, to a file.</li>

### Contributing to torspy
If you're interested in contributing to torspy, you can:

- Report issues encountered while using torspy.
- Suggest new features or enhancements.
- Submit pull requests with improvements or fixes.

### Disclaimer
```
This tool is intended for ethical use only. The author is not responsible for any misuse or damage caused by this tool. Users are responsible for ensuring their activities comply with all relevant laws and regulations.
```
