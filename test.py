import random

nume1 = ("Popov", "Alex", "Maxim", "Putin", "Donald Trump", "Marrie Currie", "Steven Hawkinds", "Michael Jackson")
num1 = (2, 3, 4, 5, 6, 7, 8, 9)
obj = ("mere", 'banane', "pixuri", "chiloti", 'masini', "bomboane", "tigari","droguri")
nn1, nn2= random.sample(num1, 2)
ob = random.choice(obj)
n1,n2 = random.sample(nume1, 2)
sum = f"Cate {ob} au ei in total?"
prod = f"Cat este produsul obiectelor"
dif1 = f"Cu cat {n1} are mai multe {ob} decat {n2}"
dif2 = f"Cu cat {n2} are mai multe {ob} decat {n1}"
calc2 = (sum, prod, dif1, dif2)
calc = random.choice(calc2)
ecuatie = f"{n1} are {nn1} {ob}, iar {n2} are {nn2} {ob} .{calc}"

start = str(input("Vrei sa incepi? Da / Nu - "))
while start:
    if start.lower() == "da":
        print("Poftim problema:")
        print(ecuatie)
        pass
    elif start.lower() == "nu":
        print("Futeo la uman dar negrule")
        break
    else:
        print("Nu am inteles")
        break
    result = 0
    while calc:
        if calc == sum:
            result = nn1 + nn2
            pass
        
        elif calc == prod:
            result = nn1 * nn2
            pass
            
        elif calc == dif1:
            result = nn1 - nn2
            pass
            
        elif calc == dif2:
            result = nn2 - nn1
            pass
        while True:
                    
            rasp = int(input(f"Numarul de {ob}: "))
            pass

            if rasp == result:
                print("Bravo!")
                break
            else:
                print("Nu bravo, mai incearca")
        break
    break