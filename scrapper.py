import requests
from bs4 import BeautifulSoup

url = 'https://secure.parking.ucf.edu/GarageCount/iframe.aspx'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

garages = []
current_spots = []
max_spots = []

# table where the data is gonna come from
table = soup.find('table', id='gvCounts_DXMainTable')

# get max spots
for length in soup.find_all("strong"):
    x = length.next_sibling.strip()
    x = x.strip('/')
    max_spots.append(int(x)) 

# get current spots
for length in soup.find_all("strong"):
    x = int (length.get_text())
    current_spots.append(x)

for length in soup.find_all('td',{'class':'dxgv'}, text=True):
    x = length.get_text()
    garages.append(x)


print(max_spots)
print(current_spots)
    # for each cell in each row
print(f"{garages[0]}")
print(f"{current_spots[0]} / {max_spots[0]}:" )
print(f"{current_spots[0] / max_spots[0] * 100:.2f} is percentage")
print(f"{100 - (current_spots[0] / max_spots[0] * 100):.2f} is full")


# percentage = (int(current_spots[0]) / int(max_spots[0])) * 100
# print(f"Percentage : {percentage}")
# print(f"Total percentage {current_spots[0]/max_spots[0]}")

# function to scrape website and return parking lot arrays
# def getParking():
