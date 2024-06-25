# Step 1: Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Step 2: Define the URL of the news webpage
url = 'https://www.lostiempos.com/actualidad/cochabamba/20240625/sipe-sipe-bloquea-segundo-dia-carretera-al-occidente-del-pais'

# Step 3: Send a GET request to the URL
response = requests.get(url)

# Step 4: Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Step 5: Extract the title of the article
# Note: The tag and class used to find the title may vary depending on the website's structure
title = soup.find('h1', class_='node-title').get_text()
print("title\n", title)
# Step 6: Extract the content of the article
# Note: The tag and class used to find the article content may vary depending on the website's structure
content = soup.find('div', class_='body').get_text()
print("content\n", content)
# Step 7: Combine the title and content
full_text = title + '__________________\n' + content

# Step 8: Save the extracted information to a txt file in the "output" folder
with open('./output/article_content.txt', 'w', encoding='utf-8') as file:
    file.write(full_text) 

# Note: Replace 'YOUR_NEWS_WEBPAGE_URL_HERE' with the actual URL of the news webpage.
# Also, replace 'article-title-class' and 'article-content-class' with the actual classes used in the news webpage for the title and content.