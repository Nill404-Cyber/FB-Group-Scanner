# Facebook High Rich Group Scraper

## Written By: Nill  
**Date:** 09/26/2024  
**Version:** 1.0

---

## Description

This script scrapes Facebook group information based on group IDs provided in a text file. It retrieves data such as the group name, total members, and the number of new posts in the last day. The results are categorized into "High Rich" and "Low Rich" groups based on the number of posts and saved into separate text files.

## Features

- Fetches group information from Facebook.
- Displays group data using rich formatting in the console.
- Saves URLs of groups with a high number of posts to a `HighRich` file and those with a low number to a `LowRich` file.
- Error handling for inaccessible groups or retrieval failures.

## Requirements

- Python 3.x
- Requests library
- Rich library

### Installation

You can install the required libraries using pip:

```bash
pip install requests rich
python3 main.py
