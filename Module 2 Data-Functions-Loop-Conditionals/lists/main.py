# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

# 1. Sorting with sort(), default alphabetic order, changes list forever

def alphabetical_order(movies):
        movies.sort()
        return movies

print(alphabetical_order(['Jaws', 'Star Wars', 'Superman', 'Home Alone', 'Hook', 'Stepmom']))


# 2. function won_golden_globe takes a film name and returns True or False if won a Golden Globe or not.

winning_movies = ['Memoirs of a Geisha', 'E.T. The Extra-Terrestrial', 'Star Wars: Episode IV - A New Hope', 'Jaws']
winning_movies_lower = [x.lower() for x in winning_movies]  #turn everything in lowercase letters

def won_golden_globe(movie):
    if movie.lower() in winning_movies_lower:
        return True
    else:
        return False
print(won_golden_globe('Jeff'))
print(won_golden_globe('JAWS'))
    

# 3. Write a function remove_toto_albums that takes a list of strings, removes Joseph's Toto albums from it and returns the tidy list.

mixed_albums = [
    'Fahrenheit',
    'Joseph Williams (re-released 2002)',
    'I Am Alive',
    '3',
    'Early Years',
    'Vertigo',
    'Two of Us',
    'Vertigo 2',
    'Smiles',
    'Tears',
    'This Fall',
    'Old Is New',
    'Denizen Tenant'
]
toto_albums = [
        'Fahrenheit',
        'The Seventh One',
        'Toto XX (lead vocals on "Last Night" and “In A Word”)',
        'Falling in Between (co-lead vocals on "Bottom Of Your Soul")',
        'Toto XIV',
        'Old Is New'
    ]

def remove_toto_albums(albums):     
    for album in albums:               
        # Check if the album name is in the toto_albums list
        if album in toto_albums:
            mixed_albums.remove(album)
    
    return mixed_albums

#remove_toto_albums([mixed_albums])

remove_toto_albums([
    'Fahrenheit',
    'Joseph Williams (re-released 2002)',
    'I Am Alive',
    '3',
    'Early Years',
    'Vertigo',
    'Two of Us',
    'Vertigo 2',
    'Smiles',
    'Tears',
    'This Fall',
    'Old Is New',
    'Denizen Tenant'
])

print(mixed_albums)

clean_albums = ['Joseph Williams (re-released 2002)',
                'I Am Alive',
                '3',
                'Early Years',
                'Vertigo',
                'Two of Us',
                'Vertigo 2',
                'Smiles',
                'Tears',
                'This Fall',
                'Denizen Tenant']

if mixed_albums == clean_albums: 
    print('finsihed')
else:
     print('not finished')



     """
updated_albums = remove_toto_albums(mixed_albums)
print(updated_albums)

"""

"""

toto_albums = ['1986: Fahrenheit', 
               '1988: The Seventh One', 
               '1998: Toto XX (lead vocals on "Last Night" and “In A Word”)',
               '2006: Falling in Between (co-lead vocals on "Bottom Of Your Soul")', 
               '2015: Toto XIV', 
               '2018: Old Is New']

mixed_albums = ['1986: Fahrenheit',
                '1982: Joseph Williams (re-released 2002)',
                '1996: I Am Alive',
                '1997: 3',
                '1999: Early Years',
                '2003: Vertigo',
                '2006: Two of Us'
                '2006: Vertigo 2',
                '2007: Smiles',
                '2007: Tears',
                '2008: This Fall',
                '2018: Old Is New',
                '2021: Denizen Tenant']

clean_albums = ['1982: Joseph Williams (re-released 2002)',
                '1996: I Am Alive',
                '1997: 3',
                '1999: Early Years',
                '2003: Vertigo',
                '2006: Two of Us'
                '2006: Vertigo 2',
                '2007: Smiles',
                '2007: Tears',
                '2008: This Fall',
                '2021: Denizen Tenant']
#clean_albums = [value for value in mixed_albums if value != toto_albums]
#print(list(clean_albums))

#clean_album = value for value in mixed_albums if value != toto_albums

def remove_toto_albums(album):
     if album in mixed_albums:
          mixed_albums.remove(album)
          return mixed_albums

print([mixed_albums])


def remove_toto_albums(album):
        if album in mixed_albums:
            mixed_albums.remove(album)
            return mixed_albums
print([mixed_albums])
#cleaned_albums = remove_toto_albums([mixed_albums])


def remove_toto_albums(album):
     #for title in album:
          if album in mixed_albums:
               mixed_albums.remove(album)
               return mixed_albums

remove_toto_albums(['1986: Fahrenheit', 
               '1988: The Seventh One', 
               '1998: Toto XX (lead vocals on "Last Night" and “In A Word”)',
               '2006: Falling in Between (co-lead vocals on "Bottom Of Your Soul")', 
               '2015: Toto XIV', '2018: Old Is New'])

print(mixed_albums)


remove_toto_albums

# cleaned_albums = remove_toto_albums([mixed_albums])


remove_toto_albums(['1986: Fahrenheit', 
               '1988: The Seventh One', 
               '1998: Toto XX (lead vocals on "Last Night" and “In A Word”)',
               '2006: Falling in Between (co-lead vocals on "Bottom Of Your Soul")', 
               '2015: Toto XIV', 
               '2018: Old Is New'])


if mixed_albums == clean_albums: 
    print('finished')
else:
     print('not finished')


"""



