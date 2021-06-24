""" Test day3 programs """
import re
import logging
#import pytest
import config as cfg

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

class TestClass:

    """ This is TestClass """
    @classmethod
    def read(cls):
        """ This is read function """
        x_i="vas.txt"
        with open(x_i, 'r')as txt_file:
            file = txt_file.read()
        return file

    @classmethod
    def read1(cls):
        """ This is read1 function """
        x_i = "vas.txt"
        with open(x_i, 'r')as txt_file:
            file = txt_file.readlines()
        return file

    @classmethod
    def write(cls, vas):
        """ This is write function """
        with open(Y, 'w') as f_i:
            for items in vas:
                f_i.write('%s ' % items)
            print("File written successfully. Check out \"output.txt\" file")
        f_i.close()

    @classmethod
    def print(cls, vas):
        """ This is print function """
        print(vas)


class TestDerived(TestClass):
    """ This is TestDerived class """

    def third_cap(self):
        """ This is thirdCap function """
        vas = []
        file = self.read1()
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s_i in string:
                if s_i != "":
                    if len(s_i) >= 3:
                        o_i = []
                        for i in s_i:
                            o_i.append(i)
                        t_i = o_i[2]
                        o_i[2] = t_i.upper()
                        str1 = ""
                        q_i = str1.join(o_i)
                        vas.append(q_i)
                    else:
                        vas.append(s_i)
        self.print(vas)
        self.write(vas)
        logging.debug("Starting with to")
        return vas

    def blankreplace(self):
        """ This is blankreplace function """
        vas = []
        file = self.read()
        words = file.split()
        k = len(words)
        e_i = ""
        count = 0
        for i in words:
            if count <= k - 2:
                e_i = e_i + i + "-"
            else:
                e_i = e_i + i
            count = count + 1
        vas.append(e_i)
        self.print(vas)
        self.write(vas)
        logging.debug("Starting with to")
        return vas

    def vowels(self):
        """ This is vowels function """
        vas = []
        file = self.read()
        words = re.sub("[aeiouAEIOU]"," ", file).split(" ")
        for h_u in words:
            if h_u != "":
                vas.append(h_u)
        self.print(vas)
        self.write(vas)
        logging.debug("Starting with to")
        return vas

    def putsemicolon(self):
        """ This is putsemicolon function """
        vas = []
        file = self.read()
        words = re.sub("[\n]", "$", file).split("$")
        for h_u in words:
            if h_u != "":
                t_i = h_u + ";"
                vas.append(t_i)
        self.print(vas)
        self.write(vas)
        logging.debug("Starting with to")
        return vas

    def toprefix(self):
        """ This is toprefix function """
        file = self.read1()
        count = 0
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s_i in string:
                if s_i.startswith("To"):
                    count = count + 1
        self.print(count)
        logging.debug("Starting with to")
        return count

    def ingsuffix(self):
        """ This is ingsuffix function """
        file = self.read1()
        count = 0
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s_i in string:
                if s_i.endswith("ing"):
                    count = count + 1
        self.print(count)
        logging.debug("Starting with to")
        return count

    def maxtimes(self):
        """ This is maxtimes function """
        vas = []
        file = self.read1()
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s_i in string:
                vas.append(s_i)
        count = 0
        num = vas[0]
        for i in vas:
            freq = vas.count(i)
            if (freq > count): #pylint: disable = superfluous-parens
                count = freq
                num = i
        vas1 = []
        vas1.append(num)
        self.print(vas1)
        self.write(vas1)
        logging.debug("Starting with to")
        return vas1

    def palindrome(self):
        """ This is palindrome function """
        vas = []
        file = self.read1()
        print(file[0])
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s_i in string:
                s_ii = s_i[::-1]
                if s_ii == s_i and s_i!= "":
                    vas.append(s_i)
        self.print(vas)
        self.write(vas)
        logging.debug("Starting with to")
        return vas

    def uniquewords(self):
        """ This is uniquewords function """
        vas = set({})
        file = self.read1()
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s_i in string:
                if s_i != "":
                    vas.add(s_i)
        l_i = list(vas)
        self.print(l_i)
        self.write(l_i)
        logging.debug("Starting with to")
        return l_i

    def counterdict(self):
        """ This is counterdict function """
        vas = []
        file = self.read1()
        for line in file:
            line = line.strip()
            string = re.sub("[^0-9a-zA-Z]", " ", line).split(" ")
            for s_i in string:
                if s_i != "":
                    vas.append(s_i)
        for ele in enumerate(vas):
            print(ele)
        logging.debug("Starting with to")

# class TestClasses(TestDerived):
#     """ This is test class """
#     def test_toprefix(self):
#         """ This is test_toprefix function """
#         vas1=self.toprefix()
#         vas2=2
#         assert vas1==vas2
#
#     def test_ingsuffix(self):
#         """ This is test_ingsuffix function """
#         vas3 = self.ingsuffix()
#         vas4 = 2
#         assert vas3 == vas4
#
#     def test_maxtimes(self):
#         """ This is test_maxtimes function """
#         vas1 = self.maxtimes()
#         vas2 = ['Do']
#         assert vas1 == vas2
#
#     def test_palindrome(self):
#         """ This is test_palindrome function """
#         vas1 = self.palindrome()
#         vas2 = ['madam','mam']
#         assert vas1 == vas2
#
#     def test_uniquewords(self):
#         """ This is test_uniquewords function """
#         vas1 = sorted(self.uniquewords())
#         vas2 = sorted(['Today','Tomorrow','Pulling','Pushing','Do','madam','mam','the', 'then'])
#         assert vas1 == vas2
#
#     def test_vowels(self):
#         """ This is test_vowels function """
#         vas1 = self.vowels()
#         vas2 = ['T','d','y','T','m','rr','w','P','ll','ng','P','sh',
#                 'ng','D','D','D','m','d','m','m','m','th','th','n']
#         assert vas1 == vas2
#
#     def test_thirdcap(self):
#         """ This is test_thirdcap function """
#         vas1 = self.third_cap()
#         vas2 = ['ToDay', 'ToMorrow', 'PuLling', 'PuShing',
#                 'Do', 'Do', 'Do', 'maDam', 'maM', 'thE', 'thEn']
#         assert vas1 == vas2
#
#     def test_blankreplace(self):
#         """ This is test_blankreplace function """
#         vas1 = self.blankreplace()
#         vas2 = ['Today-Tomorrow-Pulling-Pushing-Do-Do-Do-madam-mam-the-then']
#         assert vas1 == vas2
#
#     def test_putsemicolon(self):
#         """ This is test_putsemicolon function """
#         vas1 = self.putsemicolon()
#         vas2 = ['Today Tomorrow Pulling Pushing Do Do Do madam mam the then;']
#         assert vas1 == vas2

Y = cfg.names["outputfilename"]
d = TestDerived()
d.toprefix()
d.ingsuffix()
d.maxtimes()
d.uniquewords()
d.counterdict()
d.vowels()
d.third_cap()
d.palindrome()
d.blankreplace()
d.putsemicolon()
