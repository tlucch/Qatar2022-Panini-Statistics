import random
import seaborn as sns
import statistics

#Set variables
count_rounds = []
count = 0 

#start 1000 simulations
for i in range(0,1000):
    
    #A count to keep track de simulations
    count += 1
    
    #Create the "album" using a dictionary
    total_album = {}
    for i in range(0,634):
        total_album[i]= 0
    
    #Set variables
    rounds = 0
    count_missing = {}
    
    #Star iteration until the album is full
    while True:
        
        rounds += 1
        missing = 0
        
        #Creates random stiker
        sticker = random.randint(0,633)
        
        #Adds that sticker to de dict
        total_album[sticker] += 1
        
        #checks how many "stickers" are missing to complete the album
        for i in total_album:
            if total_album[i] == 0:
                missing += 1
        
        #If theres no more sticker missing, the loop stops
        if missing == 0:
            break
        
        #"Count_missing" is a dict that keeps track of the amount of iterations that were made in order to get a new sticker
        try:
            count_missing[missing] += 1
        except:
            count_missing[missing] = 0
        
        if count_missing[missing] == 0:
            count_missing[missing] += 1
    
    #The amount of iterations made is stored into a list to analyze later
    count_rounds.append(rounds)
    
    #To keep track of simulations
    print(f"{count}/1000")

#Generation of histogram
sns.set(style = "white")
p = sns.histplot(data=count_rounds, binwidth = 100, kde = True)
p.set_xlabel("Amount of Stickers")
p.set_ylabel("")

#Print mean and standard deviation
print(statistics.pstdev(count_rounds))
print(sum(count_rounds)/len(count_rounds))


