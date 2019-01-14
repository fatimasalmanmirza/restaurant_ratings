"""Restaurant rating lister."""



def restaurant_ratings(filename):
    file = open(filename)
    ratings = {}

    for line in file:
        line = line.rstrip()
        items = line.split(':')
        # print(items)

        ratings[items[0]] = items[1]

    sorted_ratings = sorted(ratings.items())

    # print(sorted_ratings)

    for rating in sorted_ratings:
        print('{} is rated at {}'.format(rating[0], rating[1]))
