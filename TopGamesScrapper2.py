import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_top_games():
    url = "https://store.steampowered.com/stats/stats"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    # Send a GET request to the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #table = soup.find('div', id='detailStats').find('table')
    #rows = table.find_all('tr')[1:] #skip header row
    
    # Find all game elements with the class "gameLink"
    games = soup.find_all('a', class_='gameLink')
   
    # Create an empty list to store the top 10 results
    top_games = []
    
    #for row in rows:
    #    cols = row.find_all('td')
        
    #    if len(cols) >= 3:
    #        current_players = cols[0].text.strip()
    #        peak_players = cols[1].text.strip()

    # Iterate through each game element and extract relevant information
    for game in games:
        name = game.text.strip()  # Remove any leading or trailing whitespace
        current_players_element = game.find('span', class_='currentServers')
        if current_players_element:
            current_players = int(current_players_element.text.strip())
        else:
            current_players = 0  # Set default value for games without a players
        
        # Append the top 10 result to the list
        top_games.append({
            'name': name,
            'current': current_players
        })
    
    return top_games

def display_top_games(top_games):
    #Get the time Now to display later because we care as this changes hourly
    now = datetime.now()

    # Print the top 10 results
    gameplace = 1
    print("\nTop 10 Steam Most Played Games Results: as of...\n")
    print(now.strftime("%A, %B, %d, %Y"))
    for game in top_games[:10]:
        name = game['name']
        current = game['current']
        #print(f"{gameplace}.{name}: | {current} players")
        print(f"\n{gameplace}.{name}")
        gameplace = gameplace + 1

# Main execution of the scrapper
if __name__ == "__main__":
    top_games = scrape_top_games()
    display_top_games(top_games)