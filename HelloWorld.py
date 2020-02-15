print("Hello World");


RandomNumbers= [1,3,4,2,5,9]

for i in range(len(RandomNumbers)) :
    for j in range(len(RandomNumbers)) :
        if RandomNumbers[i]+RandomNumbers[j] == 10 and i != j  :
            SolutionList = [RandomNumbers[i],RandomNumbers[j]]
            i = len(RandomNumbers) 
            print(SolutionList)
            break
        else :
            pass