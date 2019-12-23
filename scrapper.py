import requests
from bs4 import BeautifulSoup

# Global in case URI changes 
url = 'https://secure.parking.ucf.edu/GarageCount/iframe.aspx'

def getGarageSite():
    """Helper function that requests and returns the UCF Parking Garage website"""

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def getMaxSpots(soup):
    """Returns array containing the max spots for every parking garage"""
    max_spots = []
    for length in soup.find_all("strong"):
        x = length.next_sibling.strip()
        x = x.strip('/')
        max_spots.append(int(x))
    return max_spots 


def getSpotsLeft(soup):
    """Returns array containing the total spots left for every parking garage"""
    current_spots = []
    for length in soup.find_all("strong"):
        x = int (length.get_text())
        current_spots.append(x)
    return current_spots

def getGarageNames(soup):
    """Returns array containing the name of each garage field"""
    garageNames = []
    for length in soup.find_all('td',{'class':'dxgv'}, text=True):
        x = length.get_text()
        garageNames.append(x)
    return  garageNames


def garageStats():
    """Prints a table to STDOUT containing all the parking garages and their respective data"""

    soup = getGarageSite()
    maxSpots = getMaxSpots(soup)
    spotsLeft = getSpotsLeft(soup)
    names = getGarageNames(soup)
    for i in range(len(names)):
        print(f"{names[i]}    : {spotsLeft[i]} / {maxSpots[i]} | {maxSpots[i] - spotsLeft[i]} Spots Taken ~ {100 - (spotsLeft[i]/maxSpots[i] * 100): .0f}% Full")


def main():
    garageStats()


if __name__ == "__main__":
    main()