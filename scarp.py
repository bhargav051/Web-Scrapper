import requests
from bs4 import BeautifulSoup
import csv
import connection

# URL of the webpage
url = "https://byjusexamprep.com/current-affairs/cricket-world-cup-winners-list"

# Download the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
  
table_list = soup.find_all("table")
target_table = table_list[0]

print(target_table.prettify())

rows = target_table.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    for col in columns:
        print(col.get_text())

# Initialize an empty list to store the data
data = []

# Get the data from the HTML table
HTML_data = target_table.find_all("tr")[1:]
for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)
    if sub_data[0] !='Year':
        connection.insert_data_into_db(sub_data)

#getting CSV file
with open("Cricket_worldcup_winner.csv",'w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(data)