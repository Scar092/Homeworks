"""This file includes function to generate
various variants of first exercise, that is
connected with... """

import random
import pickle #first you need to create a pickle file in main directory

#creating the list with various types of tasks
TYPES_OF_TASK = ['way_to_way','any_random',
'or_even_more_random', 'and_so_on']

#main body of the program
while True:
     NUMBER_OF_TYPE = random.randint(0, len(TYPES_OF_TASK))
     TYPE = TYPES_OF_TASK [NUMBER_OF_TYPE]
     NUMBER_OF_TASK = random.randint(1, 10)
     TASK = [TYPE, NUMBER_OF_TASK]
     
     #the last five ready tasks couldn't repeat
     READY_TASKS = [] #Creating empty list

     #open pickle file from main directoru
     with open('ready.pkl', 'rb') as f:
          READY_TASKS = pickle.load (f)

     READY_TASKS.append(TASK)

     if len(READY_TASKS) > 5:
          READY_TASKS.pop(0) #remove the oldest task
     
     #save new pickle file
     with open('ready.pkl', 'wb') as f:
          pickle.dump (READY_TASKS, f)

     #checking the repeats
     if READY_TASKS.count(TASK) != 0:
          print ('Repeated value, try again!')
          break

     print (TASK)
     break
