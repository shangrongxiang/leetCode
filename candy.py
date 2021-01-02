'''There are N children standing in a line. 
Each child is assigned a rating value.

You are giving candies to these children 
subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more 
candies than their neighbors.
What is the minimum candies you must give?'''
rating = [1,3,6,6,6,2,1]
def candy(rating):
    numbers_candys = len(rating)
    num = []
    if rating[0] > rating[1] :
        num.append(2)
        numbers_candys += 1
    else:
        num.append(1)
    

    for i in range(len(rating)-2):
        print(rating[i+1])
        if rating[i+1] >= rating[i] or rating[i+1] >= rating[i+2]:
            if not (rating[i+1] == rating[i] and rating[i+1] == rating[i+2]):
                num.append(2)
            else:
                num.append(1)
        else:
            num.append(1)
    if rating[len(rating)-1] > rating[len(rating)-2]:
        num.append(2)
        numbers_candys += 1
    else:
        num.append(1)
    print(num)
    return numbers_candys
    
candy(rating)