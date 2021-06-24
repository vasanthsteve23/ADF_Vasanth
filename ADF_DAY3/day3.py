import re
import logging
import config as cfg

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

class Parent:

    def read(self):
        x = input("Enter file name ")
        txt_file = open(x, 'r')
        file = txt_file.read()
        return file

    def read1(self):
        x = input("Enter file name ")
        txt_file = open(x, 'r')
        file = txt_file.readlines()
        return file

    def write(self, vas):
        with open(y, 'w') as f:
            for items in vas:
                f.write('%s ' % items)
            print("File written successfully. Check out \"output.txt\" file")
        f.close()

    def print(self, vas):
        print(vas)


class Derived(Parent):

    # def init(self,vas=[]):
    #   self.vas=vas

    # Capitalize 3rd letter of every word
    def thirdCap(self):
        vas = []
        file = self.read1()
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s in string:
                if s != "":
                    if len(s) >= 3:
                        o = []
                        for i in s:
                            o.append(i)
                        t = o[2]
                        o[2] = t.upper()
                        str1 = ""
                        q = str1.join(o)
                        vas.append(q)
                    else:
                        vas.append(s)
        self.print(vas)
        self.write(vas)
        logging.debug("Starting with to".format())

    # Capitalize all characters of every 5th word in the file.

    # def fifthword(self):
    #     vas = []
    #     file = self.read1()
    #     words = file.split()
    #     count=1
    #     for s in words:
    #         if count%5==0:
    #            t=s.upper()
    #            if t!="":
    #              vas.append(t)
    #            else:
    #               if s != "":
    #                vas.append(s)
    #         count=count+1
    #
    #     self.print(vas)
    #     self.write(vas)

    # Use – in place of blank space

    def blankreplace(self):
        vas = []
        file = self.read()
        words = file.split()
        k = len(words)
        e = ""
        count = 0
        for i in words:
            if count <= k - 2:
                e = e + i + "-"
            else:
                e = e + i
            count = count + 1
        vas.append(e)
        self.print(vas)
        self.write(vas)
        logging.debug("Starting with to".format())

    # Split the words based on the vowels

    def vowels(self):
        vas = []
        file = self.read()
        words = re.sub("[aeiouAEIOU]", " ", file).split(" ")
        for hu in words:
            if hu != "":
                vas.append(hu)
        self.print(vas)
        self.write(vas)
        logging.debug("Starting with to".format())

    # Use ; (semi-colon) for new line.

    def putsemicolon(self):
        vas = []
        file = self.read()
        words = re.sub("[\n]", "$", file).split("$")
        for hu in words:
            if hu != "":
                t = hu + ";\n"
                vas.append(t)
        self.print(vas)
        self.write(vas)
        logging.debug("Starting with to".format())

    # Print the number of words having prefix with “To” in the input file.

    def toprefix(self):
        file = self.read1()
        count = 0
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s in string:
                if s.startswith("To") == True:
                    count = count + 1
        self.print(count)
        logging.debug("Starting with to".format())

    # Print the number of words ending with “ing” in the input file.

    def ingsuffix(self):
        file = self.read1()
        count = 0
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s in string:
                if s.endswith("ing") == True:
                    count = count + 1
        self.print(count)
        logging.debug("Starting with to".format())

    # Print the word that was repeated maximum number of times.

    def maxtimes(self):
        vas = []
        file = self.read1()
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
        self.print(vas1)
        self.write(vas1)
        logging.debug("Starting with to".format())

    # Print the palindrome present in the file.

    def palindrome(self):
        vas = []
        file = self.read1()
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s in string:
                s1 = s[::-1]
                # print(s1)
                if s1 == s and s != "":
                    vas.append(s)
        self.print(vas)
        self.write(vas)
        logging.debug("Starting with to".format())

    # Convert all words into unique list and print in command line

    def uniquewords(self):
        vas = set({})
        file = self.read1()
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s in string:
                if s != "":
                    vas.add(s)
        l = list(vas)
        self.print(l)
        self.write(l)
        logging.debug("Starting with to".format())

    # Create a Word dict with Key as counter index and value as the words present in file and print them on screen.

    def counterdict(self):
        vas = []
        file = self.read1()
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s in string:
                if s != "":
                    vas.append(s)
        for ele in enumerate(vas):
            print(ele)
            logging.debug("Starting with to".format())


# MAIN FUNCTION

# vas=[]
# d=Derived(vas)
y = cfg.names["outputfilename"]

d = Derived()
n = int(input())
if n == 1:
    d.toprefix()
elif n == 2:
    d.ingsuffix()
elif n == 3:
    d.maxtimes()
elif n == 4:
    d.palindrome()
elif n == 5:
    d.uniquewords()
elif n == 6:
    d.counterdict()
elif n == 7:
    d.vowels()
elif n == 8:
    d.thirdCap()
elif n == 9:
    d.fifthword()
elif n == 10:
    d.blankreplace()
elif n == 11:
    d.putsemicolon()
else:
    print("Please enter valid option")