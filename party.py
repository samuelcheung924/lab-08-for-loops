userinput = input("Let's party! How long till the party? ")
usernum = int(userinput)

if usernum < 1:
    print("PARTY ON!!")
else:
  for i in range(usernum, 0, -1):
    print(i)
    if i == 1:
        print("PARTY TIME!!!")
