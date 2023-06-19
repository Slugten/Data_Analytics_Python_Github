# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line

passport = {} 

def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport['name'] = str(name)
    passport['date_of_birth'] = str(date_of_birth)
    passport['place_of_birth'] = str(place_of_birth)
    passport['height'] = float(height)
    passport['nationality'] = str(nationality)

    return passport


def add_stamp(passport, country):
    
    if 'stamps' not in passport:
        passport['stamps'] = []
        passport['stamps'].append(country)

    if country != passport.get('nationality') and country not in passport['stamps']:
        passport['stamps'].append(country)

    return passport


"""
3. Write a function add_biometric_data that takes as its arguments, in this order:
A passport (dict) like the one returned by create_passport
A name (str) for the type of biometric data that will be added.
The value, or values of the to-be-added biometric data.
A date in ISO format YYYY-MM-DD (str) for when the biometric data was recorded.

"""


def add_biometric_data(passport, name, values, date):

    if 'biometric' not in passport:
        passport['biometric'] = {}
        
        value = {'date':date, 
                 'value': values}
        
        passport['biometric'][name] = value


    elif 'biometric' in passport:

        if name in passport['biometric']:

            value = {'date':date, 
                     'value':values}
            
            passport['biometric'][name].update(value)
        
        else:
            value = {'date':date, 
                     'value': values}
            
            passport['biometric'][name] = value

    return passport

omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
omari = add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
omari = add_biometric_data(omari, "eye_color_right", "blue", "2020-05-05")


# Omari gets a new left eye because of an accident
omari = add_biometric_data(omari, "eye_color_left", "brown", "2022-01-10")


# Add fingerprints too: just another value, but this is also a dict.
fingerprint_data = {
    "left_pinky": "2378945",
    "left_ring": "2349081",
    "left_middle": "132890",
    "left_index": "9823234",
    "left_thumb": "0924131",
    "right_thumb": "6234923",
    "right_index": "13249734",
    "right_middle": "34023784",
    "right_ring": "12332538",
    "right_pinky": "32458970",
}

omari = add_biometric_data(omari, "haar_kleur", "zwart", "2022-01-12")
omari = add_biometric_data(omari, "finger_prints", fingerprint_data, "2022-01-12")
omari = add_biometric_data(omari, "haar_kleur", "bruin", "2022-01-13")

print(omari)