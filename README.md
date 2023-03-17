# Security.nl News Scraper

This is a Python script that scrapes the latest news from [security.nl](https://www.security.nl/) and generates an HTML page with the news items. The script uses the [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library to extract the news items from the HTML source code of the website.

The generated HTML page includes the following information for each news item:

- Date and time
- Title
- Link to the article

The script automatically detects the date of the news items from the website heading and includes it in the HTML output. The script also includes some basic CSS styling to make the HTML output more visually appealing.

## Requirements

To run the script, you need to have the following software installed:

- Python 3.x
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

You can install Beautiful Soup using pip:

pip install beautifulsoup4


## Usage

1. Clone the repository or download the script file `security.py`.
2. Open a terminal or command prompt window and navigate to the directory where the script is located.
3. Run the following command to generate the HTML file:


python security.py


The script will generate an HTML file named `news.html` in the same directory.

4. Open the `news.html` file in a web browser to view the formatted output.

## License

This script is licensed under the [MIT License](LICENSE).

## Support

If you would like to support this project, you can make a donation through PayPal:

[![Donate with PayPal](https://img.shields.io/badge/Donate-PayPal-blue)](https://www.paypal.com/donate/?business=P9L4Y9YQYEW3Y&no_recurring=0&currency_code=EUR)

Don't forget to give this repo a ✨ STAR!

Have fun!
Joe

