# Session 1
FirstName = input("First Name: Insert your First Name")
MiddleName = input("Middle Name: Insert your Middle Name")
LastName = input("Last Name: Insert your Last Name")
FullName = f"{FirstName} {MiddleName} {LastName}"
print(f"Full Name: {FullName.title()}")


# Session 2
FirstName = input("First Name: Insert your First Name")
MiddleName = input("Middle Name: Insert your Middle Name")
LastName = input("Last Name: Insert your Last Name")
print("Full Name:", (FirstName.title()), (MiddleName.title()), (LastName.title()))


# Session 3
PP = ["TPIA", "PTRO", "BRPT"]
print(PP)
PP.append("bren")
print(PP)
PP.insert(1, "cuan")
text_1 = f"My fav stock is {PP[2]}"
text_2 = f"My fav stock is {PP[-1].upper()}"
print(PP)
PP.remove("BRPT")
print(PP)
print(text_1)
print(text_2)
PP.sort()
print(PP)
PP.sort(reverse=True)
print(PP)
print(sorted(PP))
print(PP)
PP.reverse()
print(PP)
print(len(PP))

PPS = ["PTRO", "BREN", "CUAN", "TPIA", "BRPT"]
print(PPS)
print("Rank PP's Stock here:")
rank_1 = int(input("PTRO: "))
rank_2 = int(input("BREN: "))
rank_3 = int(input("CUAN: "))
rank_4 = int(input("TPIA: "))
rank_5 = int(input("BRPT: "))
if rank_1 == 1:
    print("Good Boy")
else:
    print("Bad Boy, should've done number 1")

if rank_2 == 2:
    print("Good Boy")
else:
    print("Bad Boy, should've done number 2")

if rank_3 == 3:
    print("Good Boy")
else:
    print("Bad Boy, should've done number 3")

if rank_4 == 4:
    print("Good Boy")
else:
    print("Bad Boy, should've done number 4")

if rank_5 == 5:
    print("Good Boy")
else:
    print("Bad Boy, should've done number 5")


# Session 4