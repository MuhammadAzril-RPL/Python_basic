from os import system

def login () :
    print("|=========================================|")
    print("|                  LOGIN                  |")
    print("|=========================================|")
    nm= input("Masukan Username : ")
    pw= input("Masukan password : ")

    if nm == ("A") and pw == ("a") :
     menu()
    else :
     system("cls") 
    login() 
         
 
def menu () :
   system('cls')
   Buah = ["Anggur", "Apel", "Bengkoang" , "jeruk","duren","Markisa","Stawberry"]
   print (Buah)
   print (Buah [2])
   Buah.append ('Manggis')
   print(Buah)
   Buah.insert (3,"Apel")

login()