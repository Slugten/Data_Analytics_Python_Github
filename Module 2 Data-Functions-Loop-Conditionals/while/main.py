from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"



# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())


#1. unique_koala_facts: takes an integer as an argument and returns that number of unique koala facts in a list. 
# Note that there are only a limited number of unique facts in the dataset. 
# For high arguments your function should try to return all unique facts in the dataset. 
# No worries: the number of facts is small enough that this should be feasible. You can set an iteration limit of 1000.



def unique_koala_facts(n):
    unique_facts = set()
    loop_count = 0

    while len(unique_facts) != n and loop_count < 1000:
        loop_count += 1
        fact = random_koala_fact()

        if fact not in unique_facts:
            unique_facts.add(fact)
            
 
    return list(unique_facts)

print(len(unique_koala_facts(5)))


#2. num_joey_facts: young marsupials are called 'joeys'. How many unique facts mentioning this term are in our facts dataset? 
# Count them by getting facts from random_koala_fact until you have seen some particular fact 10 times, 
# then return how many unique joey facts you counted in the dataset.


def num_joey_facts():
    fact_count = {}
    unique_joey_facts = set()

    while True:
        fact = random_koala_fact()

        if 'joey' in fact.lower():
            unique_joey_facts.add(fact)

            if fact in fact_count:
                fact_count[fact] += 1
                if fact_count[fact] == 10:
                    break
            else:
                fact_count[fact] = 1

    return len(unique_joey_facts)


"""
def num_joey_facts():
    fact_count = {}
    joey_count = 0
    joey_fact_list = []
    used_facts = []

    while fact_count != 10:
        fact = random_koala_fact()

        if 'joey' in fact.lower() and fact not in joey_fact_list:
            joey_count += 1
            joey_fact_list.append(fact)
        
        elif 'joey' in fact.lower() and fact in joey_fact_list:
            fact_count[fact] += 1

        elif 'joey' not in fact.lower():

            if fact in used_facts:
                fact_count[fact] += 1
            
            elif fact not in used_facts:
                fact_count[fact] = 1
    return len(joey_fact_list)
"""

print(num_joey_facts())

    

# 3. koala_weight: somewhere in the data is a fact about how heavy a koala is. 
# This function should return that weight in kilogram (kg) as an integer.

def koala_weight():
    iteration_count = 0
    while iteration_count <= 100:
        
        fact_weight = random_koala_fact()


        if "kg" in fact_weight:
            iteration_count += 1
            break
    for word in fact_weight.split():
        if "kg" in word:
            return int(word[:-3])


print(koala_weight())