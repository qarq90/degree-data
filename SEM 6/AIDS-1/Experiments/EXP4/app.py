import pandas as pd

dataset = [
    {
        "id": 1,
        "name": "Call of Duty 4: Modern Warfare",
        "developer": "Infinity Ward",
        "genre": "First-Person Shooter",
        "release_year": 2007,
        "metacritic_score": 94,
        "sales_millions": 15.7,
        "peak_players": 50000
    },
    {
        "id": 2,
        "name": "Call of Duty: Modern Warfare 2",
        "developer": "Infinity Ward",
        "genre": "First-Person Shooter",
        "release_year": 2009,
        "metacritic_score": 94,
        "sales_millions": 25.0,
        "peak_players": 120000
    },
    {
        "id": 3,
        "name": "Call of Duty: Black Ops",
        "developer": "Treyarch",
        "genre": "First-Person Shooter",
        "release_year": 2010,
        "metacritic_score": 87,
        "sales_millions": 30.7,
        "peak_players": 150000
    },
    {
        "id": 4,
        "name": "Call of Duty: Warzone",
        "developer": "Infinity Ward",
        "genre": "Battle Royale",
        "release_year": 2020,
        "metacritic_score": 80,
        "sales_millions": 0,  
        "peak_players": 6000000
    },
    {
        "id": 5,
        "name": "Call of Duty: Modern Warfare (2019)",
        "developer": "Infinity Ward",
        "genre": "First-Person Shooter",
        "release_year": 2019,
        "metacritic_score": 80,
        "sales_millions": 41.0,
        "peak_players": 500000
    },
    {
        "id": 6,
        "name": "Resident Evil 2",
        "developer": "Capcom",
        "genre": "Survival Horror",
        "release_year": 1998,
        "metacritic_score": 93,
        "sales_millions": 4.96,
        "peak_players": 0  
    },
    {
        "id": 7,
        "name": "Resident Evil 4",
        "developer": "Capcom",
        "genre": "Survival Horror",
        "release_year": 2005,
        "metacritic_score": 96,
        "sales_millions": 7.1,
        "peak_players": 0
    },
    {
        "id": 8,
        "name": "Resident Evil 7: Biohazard",
        "developer": "Capcom",
        "genre": "Survival Horror",
        "release_year": 2017,
        "metacritic_score": 86,
        "sales_millions": 12.4,
        "peak_players": 20000
    },
    {
        "id": 9,
        "name": "Resident Evil Village",
        "developer": "Capcom",
        "genre": "Survival Horror",
        "release_year": 2021,
        "metacritic_score": 84,
        "sales_millions": 8.5,
        "peak_players": 100000
    },
    {
        "id": 10,
        "name": "Resident Evil (Remake)",
        "developer": "Capcom",
        "genre": "Survival Horror",
        "release_year": 2002,
        "metacritic_score": 91,
        "sales_millions": 1.35,
        "peak_players": 0
    },
    {
        "id": 11,
        "name": "Grand Theft Auto V",
        "developer": "Rockstar North",
        "genre": "Action-Adventure",
        "release_year": 2013,
        "metacritic_score": 97,
        "sales_millions": 195.0,
        "peak_players": 500000
    },
    {
        "id": 12,
        "name": "Red Dead Redemption 2",
        "developer": "Rockstar Studios",
        "genre": "Action-Adventure",
        "release_year": 2018,
        "metacritic_score": 97,
        "sales_millions": 65.0,
        "peak_players": 120000
    },
    {
        "id": 13,
        "name": "Grand Theft Auto: San Andreas",
        "developer": "Rockstar North",
        "genre": "Action-Adventure",
        "release_year": 2004,
        "metacritic_score": 93,
        "sales_millions": 27.5,
        "peak_players": 0
    },
    {
        "id": 14,
        "name": "Bully",
        "developer": "Rockstar Vancouver",
        "genre": "Action-Adventure",
        "release_year": 2006,
        "metacritic_score": 87,
        "sales_millions": 1.5,
        "peak_players": 0
    },
    {
        "id": 15,
        "name": "Max Payne 3",
        "developer": "Rockstar Studios",
        "genre": "Third-Person Shooter",
        "release_year": 2012,
        "metacritic_score": 87,
        "sales_millions": 4.0,
        "peak_players": 5000
    },
    {
        "id": 16,
        "name": "God of War",
        "developer": "Santa Monica Studio",
        "genre": "Action-Adventure",
        "release_year": 2018,
        "metacritic_score": 94,
        "sales_millions": 23.0,
        "peak_players": 0
    },
    {
        "id": 17,
        "name": "The Last of Us",
        "developer": "Naughty Dog",
        "genre": "Action-Adventure",
        "release_year": 2013,
        "metacritic_score": 95,
        "sales_millions": 20.0,
        "peak_players": 0
    },
    {
        "id": 18,
        "name": "Uncharted 4: A Thief's End",
        "developer": "Naughty Dog",
        "genre": "Action-Adventure",
        "release_year": 2016,
        "metacritic_score": 93,
        "sales_millions": 16.0,
        "peak_players": 0
    },
    {
        "id": 19,
        "name": "Spider-Man",
        "developer": "Insomniac Games",
        "genre": "Action-Adventure",
        "release_year": 2018,
        "metacritic_score": 87,
        "sales_millions": 20.0,
        "peak_players": 0
    },
    {
        "id": 20,
        "name": "Horizon Zero Dawn",
        "developer": "Guerrilla Games",
        "genre": "Action RPG",
        "release_year": 2017,
        "metacritic_score": 89,
        "sales_millions": 20.0,
        "peak_players": 0
    }
]

df = pd.DataFrame(dataset)

print()
print("=" * 122)
print(f"{'ID':<4} {'Name':<35} {'Developer':<20} {'Genre':<18} {'Year':<6} {'Metacritic':<10} {'Sales (M)':<10} {'Peak Players':<12}")
print("-" * 122)

for game in dataset:
    print(f"{game['id']:<4} {game['name'][:34]:<35} {game['developer'][:19]:<20} {game['genre'][:17]:<18} "
          f"{game['release_year']:<6} {game['metacritic_score']:<10} {game['sales_millions']:<10.1f} {game['peak_players']:<12,}")

print("=" * 122)

mean_metacritic_score = df["metacritic_score"].mean()
mean_sales = df["sales_millions"].mean()
mean_peak_players = df["peak_players"].mean()

print(f"\nAverage Metacritic Score: {mean_metacritic_score:.2f}")
print(f"Average Sales (Millions): {mean_sales:.2f}")
print(f"Average Peak Players: {mean_peak_players:.2f}")

median_metacritic_score = df["metacritic_score"].median()
median_sales = df["sales_millions"].median()

print(f"\nMedian Metacritic Score: {median_metacritic_score:.2f}")
print(f"Median Sales (Millions): {median_sales:.2f}")

mode_metacritic_score = df["metacritic_score"].mode()[0]
mode_sales = df["sales_millions"].mode()[0]

print(f"\nMode Metacritic Score: {mode_metacritic_score:.2f}")
print(f"Mode Sales (Millions): {mode_sales:.2f}")

std_metacritic_score = df["metacritic_score"].std()
std_sales = df["sales_millions"].std()

print(f"\nStandard Deviation of Metacritic Score: {std_metacritic_score:.2f}")
print(f"Standard Deviation of Sales (Millions): {std_sales:.2f}")

variance_metacritic_score = df["metacritic_score"].var()
variance_sales = df["sales_millions"].var()

print(f"\nVariance of Metacritic Score: {variance_metacritic_score:.2f}")
print(f"Variance of Sales (Millions): {variance_sales:.2f}")

quartile1_metacritic_score = df["metacritic_score"].quantile(0.25)
quartile3_metacritic_score = df["metacritic_score"].quantile(0.75)

print(f"\n1st Quartile of Metacritic Score: {quartile1_metacritic_score:.2f}")
print(f"3rd Quartile of Metacritic Score: {quartile3_metacritic_score:.2f}")

kurtosis_metacritic_score = df["metacritic_score"].kurtosis()
kurtosis_sales = df["sales_millions"].kurtosis()

print(f"\nKurtosis of Metacritic Score: {kurtosis_metacritic_score:.2f}")
print(f"Kurtosis of Sales (Millions): {kurtosis_sales:.2f}")