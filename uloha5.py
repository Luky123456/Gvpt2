x = input("Zadaj mi číslo: ")
a = input("Zadaj mi menšie číslo z intervalu: ")
b = input("Zadaj mi váčšie číslo z intervalu: ")
if a > b:
    print("Zadal si čísla v zlom poradí")
elif a < x < b:
    print("Číslo patrí do intervalu")
else:
    print("Číslo nepatrí do intervalu")