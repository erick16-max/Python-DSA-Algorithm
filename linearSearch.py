
listOne = [4,5,6,9,3,100]
n = int(input("enter number to search"))
pos = 0

def search (list_items, searched_item):
    for index,value in enumerate(list_items):
        if  value == searched_item:
            return f"The number {value} is found at index {index} in the list"
    return f"The number not is found in the list"


print(search(listOne, n))

    


    

