# Task for user input to for individual to go to the cinema
age_prompt = True
name_prompt = True


while name_prompt is True:
    name = input(f"What is your name?  ".capitalize())
    if name.isalpha():
        name_prompt = False
    else:
        print("Please use alphabetic letters for your name!")

while age_prompt is True:
    age = input(f"How old are you? {name}?  ")
    if age.isdigit():
        age_prompt = False
    else:
        print(f"{name}, Please insert your age in digits  {input} ")

films_to_watch = {
    "u_rated": ["The Lion King", "Frozen", "Toy Story", "All Dogs Go To Heaven"],
    "pg_rated": ["Cinderella Story", "The Princess Diaries", "Cheetah Girls", "Divergent"],
    "15_rated": ["The Longest Yard", "Green Mile", "American Assassin", "Iron Man", "Batman VS Superman"],
    "18_rated": ["Saw IV", "Freddy VS Jason", "Wolf of Wall Street", "Blade Trinity"]
}

while age_prompt is True:
    if age >= 110:
        print("Unfortunately, the age is not within a valid range.")
    elif age >= 18:
        print(f"You can watch a range of these movies ", {films_to_watch[:]})
    elif age >= 15 < 18:
        print(f"You can watch a range of these movies ", {films_to_watch[:3]})
    elif age >= 12 < 15:
        print(f"You can watch a range of these movies ", {films_to_watch[:2]})
    else:
        age <= 11
        print(f"You can watch a range of these movies ", {films_to_watch[:1]})
    break



