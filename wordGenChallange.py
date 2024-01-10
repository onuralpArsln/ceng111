# create a function that prints the first paramter by starting from
#a and trying every character
# only lowercase will be used 
# example  bad
# a 
# b
# ba
# baa
# bad

import time #it is just to make print look better you dont have to use delay 
import os #it is to clear terminal before printing next word just to look pretty not necessary  for solution 

def wordGen(word):
    word = word.lower() # change innput into lowercase 
    
    printWord = ""  #it is an empty string now we will add every letter to it 
    printChar = ""   #we will use it as a temporaray variable to store curent changing letter

    # i ave used chatgpt to generate this array, it was to long to write by hand 
    chars = [" ",'a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'ş', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', '<', '>', ',', '.', '/', '?']

    


    for index, value in enumerate(word):  # index will give us which step we are printing and value gives us target letter
        stepCounter=0 # we will use it in while to iterate inside chars, we need to reset it before each next letter
        #for each step first we will add blank space in chars to printWord
        printChar = chars[stepCounter]
      
        while printChar !=value:
            stepCounter += 1 #go to next step 
            printChar = chars[stepCounter] #added next char in array, beaware that we didnt check for while condition for this value during current step
            
            time.sleep(0.05)  #it is in secods 
            os.system("cls") #it allows me to clean terminal output, in unix (macos linux) yo would use clear instead cls
            print(printWord+printChar)  #we change printchar every step
        printWord += printChar   # when we find suitable char while loop ends and you add at the end of wour word 

        
wordGen("herhangi bir şey mi merhaba ") 



s