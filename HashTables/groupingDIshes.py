"""
You are given a list dishes, where each element consists of a list of strings beginning with the name of the dish, followed by all the ingredients used in preparing it. You want to group the dishes by ingredients, so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).

Return an array where each element is a list beginning with the ingredient name, followed by the names of all the dishes that contain this ingredient. The dishes inside each list should be sorted lexicographically, and the result array should be sorted lexicographically by the names of the ingredients.

"""
# Clue 1 - Make a hash table where the key is the ingredient, and the value associated with an ingredient is an array of dishes that use that ingredient.

# Clue 2 - Once you have iterated through all the dishes and each ingredient is associated with an array of dishes as a value, sort each value. THEN prepend the key (the ingredient) to the value.

# Clue 3 - Get a list of values from the hash table, and sort it. It should sort by the first element (i.e. the ingredient) first.

# Found solution one
dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

def groupingDishes(dishes):
  # creating a hashtable
  # key is the ingredient, the value is array of dishes
    hashTable = {}
    # iterate through all dishes
    for dish in dishes:
      # for every ingredient in the dish 1: slicing grabbing everything after the dish name
      for ingredient in dish[1:]:
        # if it is in the hashtable
        if ingredient in hashTable:
          # append the dish
          hashTable[ingredient].append(dish[0])
        # if it is not in the hashtable
        else:
          # put it in. ingredient is the key, value is the dish at the 0 index (the dish)
          hashTable[ingredient] = [dish[0]]
    # once program has gone through every array
    # initialize an answer array
    ans = []
    # .items returns a view object
    # VO shows key, value pairs in a tuple list
    for ing, di in hashTable.items():
        # if the length of the list is greater than 1
        if len(v) > 1:
            # append the ingredient(k) + dishes you can make(v)
            ans.append([ing] + sorted(di))
    # once this loops through return the fully sorted answer
    return sorted(ans)

groupingDishes(dishes)
