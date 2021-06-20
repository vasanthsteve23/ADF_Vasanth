                                                              
                                                              ADF DAY - 1 

1. Read a file and write only unique words in another file :
      I can intially declare one set. After that i read file from "vas.txt" and store it in "f". Then I iterate every line and split by using regex to get word by word. 
      At that same time, find length of each word concatenate both length and string and finally add in that set.Why I set here means ? It removes all duplicates and got 
      only unique words finally. After that I convert that set to list and perform sort function based on length of the string. This is our exact output of the task.
      
 
 2. Read CSV file and store it in Python Dictionary : 
      Initially create one CSV file in your local computer and import CSV in your python file. Read that file using python file reading and store it in reader. 
      Here i create one dictionary called "people". After that iterate every row in that CSV file. In that ditionary 0th value take it as key and remaining store 
      with the base of that particular key in dictionary.
      
 
 3. Display all prime numbers with the interval of 5 seconds :
      Initially import time.Here "i" is the integer iterating variable upto infinity through while loop. In every iteration, I checked that number is prime or not.
      If I get prime number, then display it and put the program to sleep for 5 seconds using "time.sleep(5)".If it is not prime number number, then proceed for the 
      further iteration.
      
 4. GCD / HCF of 2 numbers :
      Initially get 2 numbers as input from the user and call gcd(x,y) function. First I found smallest of that 2 numbers and iterate for loop from 1 to smaller+1.
      At that same time I checked the condition (x%i==0 && y%i==0) in every iteration.If this condition satisfies, then it that particular "i" is the GCD of that 
      2 numbers. Finally returned from that gcd function to main function.
      
 5.  Decimal to Binary, Octal, Hexadecimal : 
      Initially I get one decimal value as input from the user. And after that I used inbuilt python functions like bin(), oct(), hex() to get binary, octal, hexadecimal 
      value for that input respectively. Finally display it everything.
      
 6.  Ascii value for given character : 
      Intially I get one character value as input from the user. And after that I used inbuilt python function ord() to get ascii value for the input.Finally I displayed 
      that ascii value.
      
7.  User Application (name, age, gender, salary, state, city) :
      Get string as input for name, age, gender, state, city, and also get one float value for salary from the user. Finally I display it everything to the user.
 
