def egyptienne (a,b):
    
    c = 0
    while a != 0:
        if a % 2 == 1:
         c+= b
        a = a // 2
        b += b
    print (c)
    
    
egyptienne(7,11) 

  