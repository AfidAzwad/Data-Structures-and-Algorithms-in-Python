# Input data needs to be sorted in Binary Search and not in Linear Search
# Binary search access data randomly
# Binary search has time complexity O(log n)
# Binary search performs ordering comparisons

# test cases :-
# mid point value can be the desired query
# mid point value can be desired query and also it can be repeated in the list
# always we will pick the 1st position from left to right for the repeated value

def test_location(cards,mid,query):

    if cards[mid] == query:
        if mid-1 >=0 and cards[mid-1]==query:
            return 'left'
        else:
            return 'found'

def locate_card(cards,query):
    cards.sort(reverse=True)
    lo, hi = 0, len(cards)-1
    mid = (hi+lo)//2

    print(mid)
    print(cards[mid]) 
    
    if cards[mid] == query:
        resutlt = test_location(cards,mid,query)

        if resutlt == 'left':
            for i in range(lo,mid):
              if cards[i] == query:
                  print(cards)
                  return i
        elif resutlt == 'found':
            print(cards)
            return mid

    elif cards[mid] < query:
        for i in range(lo,mid):
            if cards[i] == query:
                print(cards)
                return i
    
    elif cards[mid] > query:
        for i in range(mid,hi+1):
            if cards[i] == query:
                print(cards)
                return i


cards = [9,6,6,6,4,2,1]
query = int(input("Query : "))
print(locate_card(cards,query))
