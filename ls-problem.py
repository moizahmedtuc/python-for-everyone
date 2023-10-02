"""
Task:
1. Define a model to store the data
2. Parse the data and create instances from it.
3. Find album that was number one in all countries.

 Chart positions: UK AUS CAN FRA GER

 Records = ["A Hard Day's Night; Released: 26 June 1964; Label: United Artists (US);1;1;1”,"Beatles for Sale; Released:
 4 December 1964; Label: Parlophone (UK);1;1;-;-; Beatles '65; Released: 15 December 1964; Label: Capitol (US);-;-;1; 80;9;-;1;
 Rubber Soul; Released: 3 December 1965; Label: Parlophone (UK);1;1;1;5;1;-;1 evolver; Released: 5 August 1966; Label: Parlophone
 (UK);1;1;1;5;1;14;1;", gt. Pepper's Lonely Hearts Club Band; Released: 26 May 1967; Label: Parloph gical Mystery Tour; Released:
 27 November 1967 [F]; Label: Parlophone (UK), 1low Submarine; Released: 13 January 1969; Label: Apple (UK), Capitol (US) pey Road;
 Released: 26 September 1969; Label: Apple;1;1;1;1;1;1;1;", It Be; Released: 8 May 1970; Label: Apple;1;1;1;5;4;1;1;"]
"""


class Album:
    def __init__(self, title, release_date, label, chart_positions):
        self.title = title
        self.release_date = release_date
        self.label = label
        self.chart_positions = chart_positions

    def is_number_one_in_all_countries(self):
        return all(pos == '1' for pos in self.chart_positions)


data = [
    "A Hard Day's Night; Released: 26 June 1964; Label: United Artists (US);1;1;1",
    "Beatles for Sale; Released: 4 December 1964; Label: Parlophone (UK);1;1;-;-",
    "Beatles '65; Released: 15 December 1964; Label: Capitol (US);-;-;1;80;9;-;1",
    "Rubber Soul; Released: 3 December 1965; Label: Parlophone (UK);1;1;1;5;1;-;1",
    "Revolver; Released: 5 August 1966; Label: Parlophone (UK);1;1;1;5;1;14;1",
    "Sgt. Pepper's Lonely Hearts Club Band; Released: 26 May 1967; Label: Parlophone (UK);1;1;1;5;1;14;1",
    "Magical Mystery Tour; Released: 27 November 1967 [F]; Label: Parlophone (UK);1;1;1;5;1;14;1",
    "Yellow Submarine; Released: 13 January 1969; Label: Apple (UK), Capitol (US);1;1;1;5;1;14;1",
    "Abbey Road; Released: 26 September 1969; Label: Apple;1;1;1;1;1;1;1",
    "Let It Be; Released: 8 May 1970; Label: Apple;1;1;1;5;4;1;1"
]

# Parse the data and create instances of the Album class
albums = []
for item in data:
    parts = item.split(';')
    title = parts[0].strip()
    release_date = parts[1].strip().split(': ')[1]
    label = parts[2].strip().split(': ')[1]
    chart_positions = [pos.strip() for pos in parts[3:]]

    album = Album(title, release_date, label, chart_positions)
    albums.append(album)

# Find the album that was number one in all countries
number_one_albums = [album for album in albums if album.is_number_one_in_all_countries()]

if number_one_albums:
    print("Albums that were number one in all countries:")
    for album in number_one_albums:
        print(f"Title: {album.title}")
else:
    print("No album was number one in all countries.")
