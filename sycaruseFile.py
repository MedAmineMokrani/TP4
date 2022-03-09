class file:
    
    @staticmethod
    def Read ():
        fich = open("number.txt","r")
        
        return int(fich.read())

    @staticmethod
    def sycaruse (a):
        
            while (a != 1):
                if ( a % 2 == 0 and a > 0):
                    a = a/2
                    print(a)
                elif (a % 2 == 1 and a > 0):
                    a =a*3 + 1
                    print(a)
                f = open("myfile.txt", "w")
                f.write(str(a))
       
            return a
    @staticmethod    
    def Write(a):
        fich = open("resultat.txt","w")
        fich.write(str(a))
        fich.close 
        

classe = file()
read = classe.Read()
write = classe.sycaruse(read)
classe.Write(classe.sycaruse(write))