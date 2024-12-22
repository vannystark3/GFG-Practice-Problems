def winner(arr, m, n):
    a = 0
    b = 0
    for num in arr:
        if(num%m==0):
            a += 1
            
    for num in arr:
        if(num%n==0 and num%m!=0):
            b += 1
    
    if(a>b):
        return "Ram"
    elif(a==b):
        return "Both"
    else:
        return "Rohan"
