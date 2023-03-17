# Security.nl News Scraper

A Python script that scrapes the latest news from [security.nl](https://www.security.nl/) and generates a well-structured HTML page containing the news items. The script leverages the [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library for parsing the HTML source code of the website.

The generated HTML page showcases the following details for each news item:

- Date and time
- Title
- Link to the article

The script automatically extracts the date of the news items from the website heading and incorporates it into the HTML output. It also features basic CSS styling to enhance the visual appeal of the HTML output.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Support](#support)
- [Contributing](#contributing)

## Requirements

To execute the script, ensure the following software is installed:

- Python 3.x
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Installation

Install Beautiful Soup using pip:

pip install beautifulsoup4

## Usage

1. Clone the repository or download the script file `security.py`.
2. Open a terminal or command prompt window and navigate to the directory containing the script.
3. Run the following command to generate the HTML file:

python security.py

The script creates an HTML file named news.html in the same directory.

4. Open the news.html file in a web browser to view the formatted output.

## License

This script is licensed under the [MIT License](LICENSE).

## Support

If you would like to support this project, consider making a donation through PayPal:

[![Donate with PayPal](https://img.shields.io/badge/Donate-PayPal-blue)](https://www.paypal.com/donate/?business=P9L4Y9YQYEW3Y&no_recurring=0&currency_code=EUR)

Don't forget to give this repo a ✨ STAR!

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request

Enjoy!
Joe
