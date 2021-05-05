
#!/usr/bin/python3

import sys, itertools
from itertools import repeat
import yaml
import io

global max_size, result
max_size =0

### reslut is a list of lists:
### in each index [i] in result we'll have the following information:
###[coins, [positions of the dragons]].
### for example: asum that in result[2] we have [12,[1,4]],[7,[1,3]]
### the meaning of that is that we have an options to kill 2 dragons
### if we'll chose to kill the dragons in 1,4 we'll get 12 coins
### if we'll chose kill the dragons in 1,3 we'll get 7 coins

### this is a recursive function. 
### in this function we'll be able to calculate all of the options that the knight has 
### if he will choose to kill the dragon that he met now or not

def dragon(coins, position,idx):
    if idx==1:
        ### results[0] - we didn't kill any dragon. 
        ### therefore we'll put 0 as the coins (didn't killed it) and the location of the dragon
        result[0].append([0,[position]])
        ### results[1] - we decided to kill only 1 dragon 
        ### therefore we'll put the coins that we'll get if we'll kill this specific dragon as the 'coins' , and the position of the dragon
        result[1].append([coins,[position]])
    else:
        ### recursive call - to make sure we'll cover all of the options
        dragon(coins,position,idx -1)
        ### go over all of the options that we have now (idx).
        ### check what will happen if we'll do them and also will kill the new dragon that we just met
        for (options) in result [idx-1:idx]:
            for op in options:
                ### if we can see the position of the dragon in this option 
                ### don't calculate it since we can be in any position only 1 time
                if position not in op[1]:
                    result[idx].append( [ int(coins)+op[0] , op[1]+[position] ]  )
            
def princess(value):
    ### remove all of the options that will cause the knight to take the wrong princess
    global result
    for i in range(value,max_size-1):
        result[i].clear()

def final(num_of_needed_kiled_dragon):
    ### let's assume that we can't get the wanted princess... unless we'll find that we can :)
    final = [-1]
    
    ### check only for the relevant options (which mean from the number of the dragons that we have to kill to get the princess and forward)
    ### logicly: if we can kill 5 dragos and get X coins- we'll also be able to kill 4 dragons and to get less coins (unless the missing dragon will give to us 0 coins)
    ### therefor we'll stop to check in the first point that we could see that we killed some dragons
    for idx, options in reversed( list( enumerate( result[num_of_needed_kiled_dragon:max_size-1] ) )):
        found_somthing=False
        if options != []:
            found_somthing=True
            for x in options:
                ###  if we found a better solution.
                if x[0] > final[0]:    
                    final=x
                ###  if we have more than 1 option - push only the postions of the dragons    
                elif x[0] == final[0]:
                    final.append(x[1])
        if found_somthing:
            break
        
    if -1 in final:
        print(-1)
        return
    else:
        for i in range(1, len(final) ):
            print(final[0])
            print(len(final[i]))
            [ print( (j+1), end=' ') for j in final[i]]
            print()

def starting(steps):    
    global result
    num_of_needed_kiled_dragon=int(steps[-1].replace('p ',''))
        
    ### if the last princess need more dragons than what we can have ever- don't waste time and return that we can't do it.
    if num_of_needed_kiled_dragon > max_size-1:
        print(-1)
        return
        
    ### the list of the options.
    result = [[] for i in repeat(None, max_size-1)]
       
    ### go over the steps without the last position in which we have the wanted princess 
    for idx,step in enumerate(steps[1:max_size]):
        if 'd ' in step:
            dragon(int(step.replace('d ', '')), idx+1,idx+1)
        elif 'p ' in step:
            princess(int(step.replace('p ', '')))
        else:
            raise Exception('unvalid option ' + step + ' in the index '+ str(idx) + '\nmaybe you forgot the space?')
    
    final(num_of_needed_kiled_dragon)
 
def check_file(file):
    if not (os.path.exists(file)):
        raise Exception('could not find path/file '+ file)
     
    
if __name__ == '__main__':
    try:
        
        #for personal debugging:
        #steps = [7, 'd 10', 'd 10', 'p 2','d 1', 'd 1','p 4']
        #steps = [7, 'd 10', 'd 10', 'p 2','d 1', 'd 1','p 2']
        
        file_name=input()
        check_file(file_name)        
        with open(file_name, 'r') as stream:
            steps = yaml.safe_load(stream)
        max_size = steps[0]-1
        starting(steps)
    except:
        raise
