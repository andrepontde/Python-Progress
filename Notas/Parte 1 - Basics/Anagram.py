print("Este va a ser un test de conocimiénto en python")

#Voy a intentar hacer el codigo de los anagramas en python

word1 = input("Give the first sentence")
word2 = input("Give the second sentence")

equal = True

if len(word1) == len(word2):
    
    for x in word1:
        contadorPrincipal = 0
        check1 = 0
        check2 = 0
        active = word1[contadorPrincipal]
        
        for y in word1:
            contadorSecundario = 0
            if word1[contadorSecundario] == active:
                check1 = check1 + 1
            elif word2[contadorSecundario] == active:
                check2 == active
        
        if (check1 == check2):
            equal == True
        elif (check1 != check2):
            equal == False
            break

    if equal:
        print("It is an anagram")
    elif not equal:
        print("Not an anagram")
    
else:
    print("Not an anagram")

            