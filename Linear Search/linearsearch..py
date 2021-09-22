# Linear search does the sequential access whereas Binary search access data randomly.
# Time complexity of linear search -O(n)
# Linear search performs equality comparisons

# The query can be absent in this list
# The array/list can be empty
# The query can be repeated in the list

def locate_cards(cards, query):
    length = len(cards)
    cards.sort(reverse=True)
    position = 0

    if length == 0:
        print("There is no card in this list!!")

    else:
        for i in cards:
            if i == query:
                position = cards.index(query)
                print(cards)
                return position
        return str(query + " is not in this list")


cards = [5, 8, 9, 3, 2, 4, 6, 1]
query = input("query:")
print("Position :", locate_cards(cards, query))
