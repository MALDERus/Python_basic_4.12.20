rating = [4, 3, 1, 5, 2]
user_rating_el = None

while user_rating_el != 777:
    user_rating_el = int(input("Input new rating element\nFor exit input '777'\n>>>"))
    if user_rating_el == 777:
        print(f"Final rating list - {rating}")
    else:
        rating.append(user_rating_el)
        rating.sort(reverse=1)
        print(f"Current rating  list - {rating}")
