'''There are N children standing in a line. 
Each child is assigned a rating value.

You are giving candies to these children 
subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more 
candies than their neighbors.
What is the minimum candies you must give?'''
rating = [1,3,4,5,2]
def candy(rating):
    numbers_candys = 0
    num = []
    for i in range(len(rating)):
        num.append(1)
    for i in range(len(rating)-1):
        
        if rating[i+1] > rating[i]:
            
            num[i+1] = num[i]+1

    for i in range(len(rating)-1):
        if rating[len(rating)-2-i] > rating[len(rating)-1-i] and num[len(rating)-2-i] <= num[len(rating)-1-i]:
            num[len(rating)-2-i] = num[len(rating)-1-i] + 1
    print(num)
    for i in num:
        numbers_candys += i
    return numbers_candys
    
print(candy(rating))