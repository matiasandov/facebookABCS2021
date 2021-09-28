def lengthOfLongestSubstring(s):
        #acumula el mas largo
        maxTotal = ""
        
        #iterar sobre la palabra
        #max temporal el que ira comparando con el total
        maxTemp = ""
        for i in s:
            #si no  aparece en lo que ha guardado, lo guardas
            if maxTemp.count(i) == 0:
                maxTemp += i
                #print(maxTemp)
            else:
                #si se encuentra ya i en maxTemp vas a checar el tamaño de maxTemp
                #si es más largo que lo habia antes en maxTotal, ahora este sera el nuevo longestString, 
                if len(maxTemp) > len(maxTotal):
                    maxTotal = maxTemp
                    maxTemp = ""
                #sino no, solo se vacia maxTemp para seguir buscando y agrega el ultimo caracetr visitado
                else:
                    maxTemp = ""
                    maxTemp += i
                    
        return len(maxTotal)
print(lengthOfLongestSubstring("abcabcbb"))
print(len("1234"))