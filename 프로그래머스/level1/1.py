def solution(num):
    count = 0
    while True:
        if num==1:
            break

        elif count == 500:
            break

        elif num%2 == 0:
            num = num/2

        else:
            num = num*3+1
        count = count + 1

    if count==500:
        count = -1
        
    return count