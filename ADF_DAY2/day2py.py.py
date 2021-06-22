import re
try:

    # Capitalize 3rd letter of every word

    def thirdCap():
        vas=[]
        x = input("Enter file name ")
        txt_file = open(x, 'r')
        file = txt_file.readlines()
        for line in file:
            line=line.strip()
            string = re.sub("[^0-9a-zA-Z]"," ",line).split(" ")
            for s in string:
             if s!="":
               if len(s)>=3:
                 o=[]
                 for i in s:
                    o.append(i)
                 t=o[2]
                 o[2]=t.upper()
                 str1=""
                 q=str1.join(o)
                 vas.append(q)
               else:
                 vas.append(s)
        print(vas)
        with open('output.txt', 'w') as f:
            for items in vas:
                f.write('%s ' % items)
            print("File written successfully. Check out \"3rd.txt\" file")
        f.close()



    # Capitalize all characters of every 5th word in the file.

    def fifthword():
        vas = []
        x = input("Enter file name ")
        txt_file = open(x, 'r')
        file = txt_file.readlines()
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            count=0
            for s in string:
                if count==4:
                  t=s.upper()
                  if t!="":
                   vas.append(t)
                else:
                    if s != "":
                       vas.append(s)
                count=count+1
        print(vas)
        with open('output.txt', 'w') as f:
            for items in vas:
                f.write('%s ' % items)
            print("File written successfully. Check out \"5th.txt\" file")
        f.close()


    # Use – in place of blank space

    def blankreplace():
        vas = []
        x = input("Enter file name ")
        txt_file = open(x, 'r')
        file = txt_file.read()
        words=file.split(" ")
        k=len(words)
        e=""
        count=0
        for i in words:
         if count<=k-2:
            e=e+i+"-"
         else:
            e=e+i
         count=count+1
        print(e)
        vas.append(e)
        with open('output.txt', 'w') as f:
            for items in vas:
                f.write('%s ' % items)
            print("File written successfully. Check out \"blank.txt\" file")
        f.close()


    # Split the words based on the vowels

    def vowels():
        vas = []
        x = input("Enter file name ")
        txt_file = open(x, 'r')
        file = txt_file.read()
        words = re.sub("[aeiouAEIOU]", " ",file).split(" ")
        for hu in words:
          if hu!="":
            vas.append(hu)
        print(vas)
        with open('output.txt', 'w') as f:
            for items in vas:
                f.write('%s ' % items)
            print("File written successfully. Check out \"vowels.txt\" file")
        f.close()


    # Use ; (semi-colon) for new line.

    def putsemicolon():
        vas = []
        x = input("Enter file name ")
        txt_file = open(x, 'r')
        file = txt_file.read()
        words = re.sub("[\n]", "$", file).split("$")
        for hu in words:
            if hu != "":
                t=hu+";\n"
                vas.append(t)
        with open('output.txt', 'w') as f:
            for items in vas:
                f.write('%s' % items)
            print("File written successfully. Check out \"semi.txt\" file")
        f.close()

    # Print the number of words having prefix with “To” in the input file.

    def toprefix():
        x=input("Enter file name ")
        txt_file=open(x,'r')
        file=txt_file.readlines()
        vas=[]
        count=0
        for line in file:
            line=line.strip()
            string = re.sub("[^0-9a-zA-Z]"," ",line).split(" ")
            for s in string:
                 if s.startswith("To")==True:
                  count=count+1
        print(count)


    # Print the number of words ending with “ing” in the input file.

    def ingsuffix():
        x = input("Enter file name ")
        txt_file = open(x, 'r')
        file = txt_file.readlines()
        vas = []
        count = 0
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s in string:
                if s.endswith("ing") == True:
                    count = count + 1
        print(count)


    # Print the word that was repeated maximum number of times.

    def maxtimes():
        vas = []
        x = input("Enter file name ")
        txt_file = open(x, 'r')
        file = txt_file.readlines()
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s in string:
                vas.append(s)
        count = 0
        num = vas[0]
        for i in vas:
            freq = vas.count(i)
            if (freq > count):
                count = freq
                num = i
        vas1 = []
        vas1.append(num)
        print(num)
        with open('output.txt', 'w') as f:
            for items in vas1:
                f.write('%s ' % items)
            print("File written successfully")
        f.close()


    # Print the palindrome present in the file.

    def palindrome():
        vas = []
        x = input("Enter file name ")
        txt_file = open(x, 'r')
        file = txt_file.readlines()
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s in string:
                s1 = s[::-1]
                # print(s1)
                if s1 == s and s != "":
                    vas.append(s)
        with open('output.txt', 'w') as f:
            for items in vas:
                f.write('%s ' % items)
            print("File written successfully")
        f.close()


    # Convert all words into unique list and print in command line

    def uniquewords():
        vas = set({})
        x = input("Enter file name ")
        txt_file = open(x, 'r')
        file = txt_file.readlines()
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s in string:
                if s != "":
                    vas.add(s)
        l = list(vas)
        with open('output.txt', 'w') as f:
            for items in l:
                f.write('%s ' % items)
            print("File written successfully")
        f.close()


    # Create a Word dict with Key as counter index and value as the words present in file and print them on screen.

    def counterdict():
        vas = []
        x = input("Enter file name ")
        txt_file = open(x, 'r')
        file = txt_file.readlines()
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s in string:
                if s != "":
                    vas.append(s)
        for ele in enumerate(vas):
            print(ele)


    # MAIN FUNCTION

    n=int(input())
    if n==1:
       toprefix()
    elif n==2:
       ingsuffix()
    elif n==3:
        maxtimes()
    elif n==4:
        palindrome()
    elif n==5:
        uniquewords()
    elif n==6:
        counterdict()
    elif n==7:
        vowels()
    elif n==8:
        thirdCap()
    elif n==9:
        fifthword()
    elif n==10:
        blankreplace()
    elif n==11:
        putsemicolon()
    else:
        print("Please enter valid option")



except:
    print("Exception found")