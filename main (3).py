import random
Length=int(input("What do you want your password's length to be: "))
Alphabet_Type = int(input("Press 1 For Only Lowercase\nOr Press 2 For Only UPPERCASE\nOr Press 3 for both Lowercase and UPPERCASE"))
Alphabet_Lower = "abcdefghijklmnopqrstuvwxyz"
Alphabet_Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Symbols_Numbers = int(input("Press 1 For Only Symbols\nOr Press 2 For Only Numbers\nOr Press 3 for both Symbols and Numbers"))
Numbers = "0123456789"
Symbols = "!@#$%^&*()-_+"
Password = ""
for x in range(Length):
    if Alphabet_Type == 1 and Symbols_Numbers == 1: 
        Password += random.choice(Alphabet_Lower+Symbols)
    elif Alphabet_Type == 1 and Symbols_Numbers == 2:
        Password += random.choice(Alphabet_Lower+Numbers)
    elif Alphabet_Type == 1 and Symbols_Numbers == 3:
        Password += random.choice(Alphabet_Lower+Symbols+Numbers)     
    elif Alphabet_Type == 2 and Symbols_Numbers == 2:
      Password += random.choice(Alphabet_Upper+Symbols+Numbers)
    elif Alphabet_Type == 2 and Symbols_Numbers == 2:
      Password += random.choice(Alphabet_Upper+Numbers)
    elif Alphabet_Type == 3 and Symbols_Numbers == 3:
      Password += random.choice(Alphabet_Upper+Alphabet_Lower+Symbols+Numbers)
    elif Alphabet_Type == 3 and Symbols_Numbers == 1:
      Password += random.choice(Alphabet_Upper+Alphabet_Lower+Symbols)
    elif Alphabet_Type == 3 and Symbols_Numbers == 2:
      Password += random.choice(Alphabet_Upper+Alphabet_Lower+Numbers)


  
print(Password)
