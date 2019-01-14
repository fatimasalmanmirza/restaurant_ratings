"""Restaurant rating lister."""



def restaurant_ratings(filename):
    file = open(filename)
    ratings = {}

    for line in file:
        line = line.rstrip()
        items = line.split(':')
        # print(items)

        ratings[items[0]] = items[1]

    return ratings


def sort_and_print(ratings_dict):        

    # print(sorted_ratings)

    for rating in sorted(ratings_dict.items()):
        print('{} is rated at {}'.format(rating[0], rating[1]))


def add_restaurant(ratings_dict):

    new_restaurant  = input("restaurant name? ")
    new_score = input("restaurant score? ")

    if int(new_score) >= 1 and int(new_score) <= 5:
        ratings_dict[new_restaurant.title()] = new_score
        sort_and_print(ratings_dict)

    else:
        print("That's not a valid score.")
        add_restaurant(ratings_dict)

    # while new_score >=1 and new_score <= 5:




        

restaurant_ratings('scores.txt')