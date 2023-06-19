from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


# 1. shortest_names: takes a list of country names and returns a list of country names that have the shortest length. 
# If there is only one country with the shortest name the list will contain only that country name, 
# otherwise multiple countries should be in the list. Use a for-loop and len!

def shortest_names(country_list):
    #variable aanmaken (oneindig) om naamlengte mee te vergelijken + een lege lijst voor het resultaat

    length = float('inf')
    shortest_list = []

    #voor "naam land" in de lijst met geimporteerde namen van landen:

    for name in country_list:
        name_length = len(name)
        

        #wanneer de lengte van de naam kleiner is dan de lengte van de vorige naam:
        if name_length < length:
            #"length" waarde wordt aangepast aan de lengte van het het eerste land
            length = name_length

            #gevonden land wordt toegevoegd aan de lijst
            shortest_list = [name]          
        
        #wanneer "name_length" (iedere keer de lengte van het nieuwe land) gelijk is aan de lengte van het vorige land, toevoegen aan de lijst met namen
        elif name_length == length:
            shortest_list.append(name)
    return shortest_list




#2. most_vowels: takes a list of country names and returns a list with the top three countries that have the most vowels in their name.

vowels = 'aeiou'
most_vowels_list = []

def count_vowels(country):
    count = 0
    for letter in country.lower():
            if letter in vowels:
                count += 1
    return count

def most_vowels(countries):
    most_vowels_list = sorted(countries,  key= lambda x: count_vowels(x), reverse=True)
    top_three = most_vowels_list[:3]
    return top_three


#3. alphabet_set: takes a list of country names and returns a list of country names whose letters can be combined to form the complete alphabet.



def alphabet_set(country_list):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    countries_lowercase = [country.lower() for country in country_list]
    short_name_list = []
    used_letters = []

    for country in countries_lowercase:

        for letter in country:

            if letter in alphabet:
                alphabet.remove(letter)
                
                if country not in short_name_list:
                    short_name_list.append(country)
            
                    if len(used_letters) == 26 and len(short_name_list) <= 14:
                        break

    return short_name_list



        








""" Write your functions here. """

# 1. returns a list of country names that have the shortest length.
#    If there is only one country with the shortest name the list will contain only that country name, 
#    otherwise multiple countries should be in the list. Use a for-loop and len!


"""
def shortest_names(names):    
    shortest_length = float('inf')  #set initial shortest length to infinity
    shortest_names = []             #create a temporary list to return the shortest names to

    for name in names:
        name_length = len(name)             #set name length to compare
        if name_length < shortest_length:   #compare length of name(taken from list) with number
            shortest_length = name_length   #set new shortest length value
            shortest_names = [name]         #set single name list, when shorter name is found, this list gets updated with the shorter name
            
        elif name_length == shortest_length:    #if name has same length as the name set in shortest_name, the name gets added to the list.
            shortest_names.append(name)
    return shortest_names


# 2.    Returns a list with the top three countries that have the most vowels in their name. 
#       The country with the most vowels should be on position 0 in the list, the country with the second-most on position 1
#       we count aeiou as vowels.

#create a function that counts the vowels
def count_vowels(name):
    count = 0
    vowels = "aeiou"

    for char in name.lower():
        if char in vowels:
            count += 1
    return count

#create a function that sorts the outcome of count_vowels(name) and takes the first 3 names
def most_vowels(country_names):
    sorted_counties = sorted(country_names, key=lambda x: count_vowels(x), reverse=True)
    top_three = sorted_counties[:3]
    return top_three


           
# 3. alphabet_set: takes a list of country names and returns a list of country names whose letters can be combined to form the complete alphabet. 
# lettercase is not relevant (a and A are the same)
# Solutions with 14 or fewer countries are accepted as correct.

#Alphabet = 'abcdefghijklmnopqrstuvwxyz'



def alphabet_set(country_list):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    found_countries = []
    countries_lowercase = [country.lower() for country in country_list]
    for country in countries_lowercase:

        for letter in country:

            if letter in alphabet:
                alphabet.remove(letter)
            
                if country not in found_countries:
                    found_countries.append(country)
        
        if alphabet == list("") and len(found_countries) <= 14:
            return found_countries



"""
"""

def alphabet_set(country_list):
    #create an empty list for used letters, end result and an list for all the letters of the alphabet
    covered_letters = []
    alphabet = ['abcdefghijklmnopqrstuvwxyz']
    result = []

    while covered_letters != alphabet:
        best_country = None
        best_letters = []
        

        for country in country_list:
            letters = list(country.lower())
            uncovered_letters = [letter for letter in letters if letters not in covered_letters]

            if len(covered_letters) > len(uncovered_letters):
                best_country = country
                best_letters = uncovered_letters

        if best_country is None:
            break

        result.append(best_country)
        covered_letters += best_letters
    
    return result

"""
"""

        for letter in name:
            letters_left = len(Alphabet)
            if alphabet_length != 0:
                if letter in Alphabet:
                    Alphabet.replace(letter,'')
                    alphabet_length = letters_left
                    set.append(name)
        return set

     """                



# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()
   
    """ Write the calls to your functions here. """

    print(shortest_names(countries))
    print(most_vowels(countries))
    print(alphabet_set(countries))