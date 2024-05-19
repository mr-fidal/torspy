# torspy

<img src="https://img.myindianhub.com/other/spyder.jpg">
<b>torspy</b> is a robust Python package fortified with powerful algorithms, designed for seamless exploration of .onion sites via the Tor network. Its arsenal includes adept scraping of HTML from .onion URLs, precise text localization within the acquired content, and proficient storage of findings. Moreover, torspy boasts formidable subdomain scanning capabilities, enabling thorough reconnaissance across diverse subdomains. Additionally, it excels at detecting hidden directories, further enhancing its efficacy in navigating and extracting valuable information from the depths of the dark web. Torspy also features advanced content analysis, comprehensive link extraction, detailed service information retrieval, and efficient content downloading, making it an indispensable tool for deep web exploration and analysis.

### Index

* [Command 01 How to view the HTML of a page on the Onion site](#command-01)
* [Command 02 How to clone an entire page and save it to a file](#command-02)
* [Command 03 How to move files into directory](#command-03)
* [Command 04 To search for content](#command-04)
* [Command 05 Search content and save file](#command-05)
* [Command 06 Search content and save file -d path](#command-06)
* [Command 07 directories](#command-07)
* [Command 08 directories and file](#command-08)
* [Command 09 subdomain](#command-09)
* [Command 10 subdomain and file](#command-10)
* [Command 11 analyzes](#command-11)
* [Command 12 How to transfer the analyzed data to a file](#command-12)
* [Command 13 downloads content from an onion site](#command-13)
* [Command 14 finds links on an onion site](#command-14)
* [Command 15 Command to convert all links into one file](#command-15)
* [Command 16 gets service info of an onion site](#command-16)
* [Command 17 help](#command-17)

### Advantages
-	torspy is easy to use

-	Many hidden directories can be found using torspy

-	Each request torspy makes for your purpose will be anonymous

-	torspy can be used to extract required text or content from the website

-	HTML files can be downloaded using torspy

-	With torspy  you can search for the files you need

-	torspy is the leading package for dark web scraping.

- Finding links from onion sites

- Finding services from onion sites
- Download files from onion sites
- Analyzing onion sites

-<b> torspy is the leading package for dark web scraping.</b>

### Disadvantages

-	Since requests are made using the Tor network, this tool will run slowly

-	The probability of finding hidden directories, subdomains and files is less than 20% 

-	Sometimes you have to wait some time for this tool to work 

- Some processes may take time to complete


<b>When using torspy tool you must use Tor otherwise it won't work : $ tor</b>

## Coding 

- Python : <a href="https://github.com/mr-fidal/torspy/blob/main/coding/python.md">Link</a>
- Bash : <a href="https://github.com/mr-fidal/torspy/blob/main/coding/bash.md">Link</a>

## Installation

You can install torspy via pip:

```sh
pip install torspy
```
## Usage
### Command-Line Interface
torspy allows you to interact with .onion sites from the command line:

<b id="command-01">Command 01</b>
- To display the content of a .onion site:
```sh
torspy http://example.onion
```
-	When the above command is run, a request goes through the Tor network to that onion site, and then the HTML page of the onion site is displayed on your terminal.

<b id="command-02">command 02</b>
- To save the displayed content to a file:
```sh
torspy http://example.onion -s file.html
```
-	The `-s` flag indicates saving, and you can specify any file name. 

-	The above command transfers the entire HTML code that were printed on your terminal to another file 

-	Also you can change the name of file.html to any name of your choice

<b id="command-03">command 03</b>

- How to move this file to a directory of your choice
```sh
torspy http://example.onion -s file.html -d /path/home/
```
-	`-d` stands for directory 

-	Given after `-d` is your path and if you run the above command your file will move to the given path

<b id="command-04">command 04</b>
-	Search only the content you need from Onion sites
```sh
torspy http://example.onion --find “search query”
```
-	If you enter the above command it will search only the content you need from the given onion site and print it. 

-	The command `--find` means to search

<b id="command-05">command 05</b>
- -	To search for specific text within the content and save the results to a file
```sh
torspy http://example.onion --find “search query” -s search_results.html
```
-	If you enter the above command it will search for the content you need from the site you provided and then transfer all that content to another file.

<b id="command-06">command 06</b>
-	How to search for content and move it to another directory
```sh
torspy http://example.onion --find “important information” -s results.html -d /path/to/directory
```
-	If you run the above command it will search for the content you need from the given onion site and then move it to a file and then move it to the directory you specified.

### Message 
- important <b>Remember that when trying to find subdomains, as well as trying to find directories, the success rate is only 20%.</b>
- Finding directories and subdomains for onion sites is more challenging than for regular websites because onion sites are part of the dark web, which is intentionally designed to be less accessible and more private.

<b id="command-07">command 07</b>

-	Command that finds the directories on the onion site
```sh
torspy http://example.onion --dir directories-list.txt
```
- <b>This process may take some time</b>
-	If you run the command above it will search for directories from the onion sites you provided

-	The command `--dir` stands for directories

-	This command performs directories scanning on the .onion site using the list of directories provided in the `directories-list.txt` file.

<b id="command-08">command 08</b>
-	How to move all the lists of directories you got into another file
```sh
torspy http://example.onion --dir directories-list.txt -s output.txt
```
-	If you run the above command all the directory lists you get will be moved to another file

-	Also you can move this file to other directory or other path using `-d` command

<b id="command-09">command 09</b>
- Command that finds subdomains in onion site
```sh
torspy http://example.onion --sub subdomain-list.txt
```
- <b>This process may take some time</b>
-	If you run the command above it will search for subdomains from the onion sites you provided

-	The command `--sub` stands for subdomains 

-	This command performs subdomains scanning on the .onion site using the list of subdomains provided in the `subdomains-list.txt` file.

<b id="command-10">command 10</b>
-	How to move all the lists of subdomains you got into another file
```sh
torspy http://example.onion --sub subdomain-list.txt -s output.txt
```
-	If you run the above command all the subdomains lists you get will be moved to 

-	another file

-	Also you can move this file to other directory or other path using `-d` command

<b id="command-11">command 11</b>

- Command that analyzes content of an onion site
```sh
torspy http://example.onion --analyze
```
- If you run the command above it will analyze the content of the onion site you provided.
- The command `–-analyze` performs content analysis on the .onion site.

<b id="command-12">command 12</b>
- How to transfer the analyzed data to a file
```sh
torspy http://example.onion --analyze -s file-name.html
```
- You can name the file whatever you want { chnage file-name.html }

<b id="command-13">command 13</b>

- Command that downloads content from an onion site
```sh
torspy http://example.onion --download -s filename
```
- If you run the command above it will download the content of the onion site you provided and save it to the specified file.
- The command `–-download` performs content downloading.
- example : `torspy http://example.onion –-download -s index.html` , `torspy http://example.onion –-download -s data.jpg` 
- The command -s specifies the file name to save the downloaded content.

<b id="command-14">command 14</b>
- Command that finds links on an onion site
```sh
torspy http://example.onion --links
```
- If you run the command above it will find all links on the onion site you provided.
- The command `–-links` performs link extraction.

<b id="command-15">command 15</b>
- Command to convert all links into one file
```sh
torspy http://example.onion --links -s file-link.txt
```
- After running the above command all the links will be changed to the file you have given

<b id="command-16">command 16</b>
- Command that gets service info of an onion site
```sh
torspy http://example.onion --service
```
- If you run the command above it will retrieve service info of the onion site you provided.
- The command `–-service` performs service information retrieval.
- You can use `-s` to save

<b id="command-17">command 17</b>

- For more information on available options, you can use the `--help` flag:
```sh
torspy --help
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

- Report issues encountered while using <a href="https://github.com/mr-fidal/torspy/issues">torspy</a>.
- Suggest new features or enhancements.
- Submit <a href="https://github.com/mr-fidal/torspy/pulls">pull requests</a> with improvements or fixes.

### Disclaimer
```
This tool is intended for ethical use only. The author is not responsible for any misuse or damage caused by this tool. Users are responsible for ensuring their activities comply with all relevant laws and regulations.
```
