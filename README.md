# Kinopoisk Movie Data Parser

## Overview

The Movie Data Parser is a Python script designed to scrape data from Kinopoisk's top 1000 movie list. It uses Selenium and Beautiful Soup for web scraping and allows you to gather information on the top-rated movies, including their name, rating, year of release, country of origin, producer, and availability on Kinopoisk.

## Average Execution Time

The average execution time of the program is approximately 30 seconds.

## Featuresgit checkout main

The Movie Data Parser offers the following functionality:

1. Automated web scraping of Kinopoisk's top 1000 movie list.
2. Extraction of movie details, including name, rating, year, country, producer, and availability on Kinopoisk.
3. Utilizes random User-Agent strings for anonymity.
4. Supports headless mode for running without a visible browser.

## Technologies

- Python
- Selenium
- Beautiful Soup
- Webdriver Manager
- Fake User-Agent

## Usage

1. Install Python on your system if it's not already installed.

2. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/movie-data-parser.git
   ```

3. Navigate to the project directory:

   ```bash
   cd movie-data-parser
   ```

4. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the script with the following command:

   ```bash
   python movie_data_parser.py
   ```

6. The parsed movie data will be saved to a JSON file named "top1000.json."
