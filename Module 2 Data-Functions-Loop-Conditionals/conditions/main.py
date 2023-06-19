# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

Weather = ('rainy', 'sunny', 'windy', 'neutral')
time_of_day = ('day', 'night')
need_milking = (True, False)
Location_cows = ('pasture', 'cowshed')
season = ('winter', 'spring', 'summer', 'fall')
tank_full = (True, False)
grass_long = (True, False)

def main():
    return farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)

def farm_action(weather, time_of_day, need_milking, location_cows, season , tank_full, grass_long):
        if location_cows == 'pasture' and (time_of_day == 'night' or weather == 'rainy' or need_milking == True) and need_milking == True:
           return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'
        if location_cows == 'pasture' and (time_of_day == 'night' or weather == 'rainy' or need_milking == True) and tank_full == True and (weather == 'rainy' or 'neutral'):
           return'take cows to cowshed\nfertilize pasture\ntake cows back to pasture' 
        if location_cows == 'pasture' and (time_of_day == 'night' or weather == 'rainy' or need_milking == True):
           return 'take cows to cowshed'           
        if need_milking == True and location_cows == 'cowshed':
            return'milk cows'
        if tank_full == True and (weather == 'rainy' or 'neutral') and location_cows == 'cowshed':
            return 'fertilize pasture'
        if grass_long == True and season == 'spring' and weather == 'sunny' and location_cows != 'pasture':
            return 'mow grass'  
        else: 
            return 'wait'
                
if __name__ == '__main__':
     print(main())
