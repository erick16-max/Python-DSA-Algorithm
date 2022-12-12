from jovian.pythondsa import evaluate_test_cases, evaluate_test_case
import jovian

tests = [

    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
    {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
    {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
    {'input': {'cards': [6], 'query': 6}, 'output': 0},
    {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
    {'input': {'cards': [], 'query': 7}, 'output': -1},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},'output': 7},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],'query': 6},'output': 2}
]
def linear_search(cards, query):
    #jovian algorithm
    # index = 0
    # while index < len(cards):
    #     if cards[index] == query:
    #         return index
    #     index += 1
    # return -1

    #gegerick algorithm
    if len(cards) < 1:
        return -1

    for index in range(0,len(cards)):
        if (cards[index] == query):
            return index
    return -1
#testing all the test cases including edge cases
# evaluate_test_cases(linear_search, tests)


#BINARY SEARCH
#jovian algorithm
def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

#gegerick algo
def binary_search(cards,query):
    
    max_num = len(cards) - 1
    min_num = 0
    while min_num <= max_num:
        mid = (max_num+min_num) // 2
        if cards[mid] == query:
            if mid-1 >= 0 and cards[mid-1] == query:
                #apply recursion to find the first occurence of query
                return binary_search(cards[:mid], query)
            return mid
        elif cards[mid] < query:
            max_num = mid - 1
        elif cards[mid] > query:
            min_num = mid + 1
    return -1


evaluate_test_cases(binary_search,tests)



   

# jovian.commit(project='python-binary-search', environment=None)
