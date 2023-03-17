import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://www.security.nl/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

news = soup.find('div', class_='posting_list with_row_background frontpage')
output = ''

today = datetime.today().strftime('%A %d %B %Y')
date = soup.find('div', class_='posting_list_heading').text.strip()

output += f"""
<html>
<head>
<style>
h2 {{
    text-align: center;
    color: #3d3d3d;
    font-size: 28px;
    margin-top: 50px;
}}
.news-item {{
    border: 1px solid #d9d9d9;
    padding: 10px;
    margin-bottom: 20px;
    background-color: #f8f8f8;
}}
.date {{
    font-weight: bold;
    margin: 0;
    color: #3d3d3d;
}}
.title {{
    margin: 10px 0;
    font-size: 18px;
    color: #3d3d3d;
}}
.link {{
    margin: 0;
    font-size: 16px;
    color: #3d3d3d;
}}
.link a {{
    color: #ff6600;
    text-decoration: none;
}}
.link a:hover {{
    text-decoration: underline;
}}
</style>
</head>
<body>
<h2>Security.nl News for {date}</h2>
"""

for item in news.find_all('div', class_='posting_list_item'):
    timestamp = item.find('div', class_='timestamp').text.strip()
    title = item.find('div', class_='title').find('a').text.strip()
    link = f"{url}{item.find('div', class_='title').find('a')['href']}"
    output += f"""
    <div class='news-item'>
        <p class='date'>{date} - {timestamp}</p>
        <p class='title'>{title}</p>
        <p class='link'>Link: <a href='{link}'>{link}</a></p>
    </div>
    """

output += "</body></html>"

with open('news.html', 'w') as f:
    f.write(output)

print("Output has been written to news.html")
