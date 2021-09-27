def longest_common_prefix(strings):
    prefix = strings[0]
    notSinceBeginning = 0
    #actPref = ""
    for i in range (0, len(strings)-1):
        #para cada posicion (menos la ultima) exisitira esta variable que ira almacenado prefix
        actPref = ""
        for j in range (0, min( len(strings[i]) ,len(strings[i+1]) )):
            
            if(strings[i][j] == strings[i+1][j]):
                
                actPref = actPref + strings[i][j]
                notSinceBeginning = notSinceBeginning + 1
                print(actPref)
            else:
                if(notSinceBeginning == 0):
                    prefix = ""
                    return prefix
                #si se puede encontrar el actPref en 
                elif(prefix.find(actPref) and (notSinceBeginning != 0)):
                    prefix = actPref
                    #actPref = ""
        #esto debe ser en cada iteracion que se actualice
        prefix = actPref
    return prefix
                
a = ['flower','flow','flight']
pre = longest_common_prefix(a)
print('final : ', pre)