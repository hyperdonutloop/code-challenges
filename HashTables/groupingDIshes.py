"""
You are given a list dishes, where each element consists of a list of strings beginning with the name of the dish, followed by all the ingredients used in preparing it. You want to group the dishes by ingredients, so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).

Return an array where each element is a list beginning with the ingredient name, followed by the names of all the dishes that contain this ingredient. The dishes inside each list should be sorted lexicographically, and the result array should be sorted lexicographically by the names of the ingredients.

"""
# Clue 1 - Make a hash table where the key is the ingredient, and the value associated with an ingredient is an array of dishes that use that ingredient.

# Clue 2 - Once you have iterated through all the dishes and each ingredient is associated with an array of dishes as a value, sort each value. THEN prepend the key (the ingredient) to the value.

# Clue 3 - Get a list of values from the hash table, and sort it. It should sort by the first element (i.e. the ingredient) first.

# Found solution one
def groupingDishes(dishes):
    hashTable = {}
    for dish in dishes:
        for ingredient in dish[1:]:
            if ingredient in hashTable:
                hashTable[ingredient].append(dish[0])
            else:
                hashTable[ingredient] = [dish[0]]
    ans = []
    for k, v in hashTable.items():
        if len(v) > 1:
            ans.append([k] + sorted(v))
    return sorted(ans)