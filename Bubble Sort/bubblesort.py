def bubblesort(lists):
    n = len(lists)
    print(lists)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if lists[j] > lists[j+1] :
                lists[j], lists[j+1] = lists[j+1], lists[j]
                swapped = True
        if swapped == False: # to avoid extra iterations
            break
    return lists

if __name__ == '__main__':
    lists = [6,1,5,6,3]
    print("Sorted List : ", bubblesort(lists))