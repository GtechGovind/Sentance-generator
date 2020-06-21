import xml.etree.ElementTree as Et
import random

# what
def DrinkSvoo():
    doc = Et.parse("Data/templates/interrogative/what/svoo/drink.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:
            if phrase.tag == "PREFIX":
                arr1.append(phrase.text)  # adding "what"

            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                break
                        arr1.append(temp[1])

                    if child.tag == "SNOUN":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                        arr1.append(random.choice(arr0))

            if phrase.tag == "VERBPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                break
                        arr0 = []
                        arr1.append(random.choice(temp[1:-1]) + ",")

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:
                    if child.tag == "CNOUN1":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))


                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open("Data/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(temp[1])

                    if child.tag == "CNOUN2":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))
                                if arr1[4] == arr1[6]:
                                    temp.remove(arr1[4])
                                    arr1.remove(arr1[6])
                                    arr1.append(random.choice(temp[1:-1]))

                        arr1.append("?")

                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr)
    return listToStr + "."

def EatSvoo():
    doc = Et.parse("Data/templates/interrogative/what/svoo/eat.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:
            if phrase.tag == "PREFIX":
                arr1.append(phrase.text)  # adding "what"

            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                break
                        arr1.append(temp[1])

                    if child.tag == "SNOUN":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                        arr1.append(random.choice(arr0))


            if phrase.tag == "VERBPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                break
                        arr0 = []
                        arr1.append(random.choice(temp[1:-1]) + ",")

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:
                    if child.tag == "CNOUN1":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))


                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open("Data/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(temp[1])

                    if child.tag == "CNOUN2":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))
                                if arr1[4] == arr1[6]:
                                    temp.remove(arr1[4])
                                    arr1.remove(arr1[6])
                                    arr1.append(random.choice(temp[1:-1]))


                        arr1.append("?")

                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr)
    return listToStr + "."

# when
import xml.etree.ElementTree as Et
import random


def CloseSvoo():
    doc = Et.parse("Data\\templates\\interrogative\\When\\svoo\\close.xml")
    root = doc.getroot()

 
    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence
        gender_list = ["male", "female"]
       
        for phrase in sentence:
           
            if phrase.tag == "PREFIX":
                arr1.append(phrase.text) #adding "what"
                print(arr1)
            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data/verb_dict"
                            "/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                temp.remove("\n")
                                # print(temp)
                                break
                        arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "PRONOUN":
                        class0 = child.attrib

                        noun_dict = open(
                            "Data/noun_dict"
                            "/pronouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[1:-1])
                                #print(arr0)
                        #print(arr0)
                        arr1.append(random.choice(arr0))
                        print(arr1)

            if phrase.tag == "VERBPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data/verb_dict"
                            "/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                #temp.remove("\n")
                                # print(temp)
                        arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:
                    if child.tag == "ARTICLE":
                        class0 = child.attrib
                        arr1.append("the")
                        print(arr1)

                    if child.tag == "CNOUN1":
                        class0 = child.attrib
                        noun_dict = open(
                            "Data/noun_dict"
                            "/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                              #  temp.remove("\n")
                                arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open(
                            "Data/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                              #  temp.remove("\n")
                                arr1.append(temp[1])
                                print(arr1)

                    if child.tag == "CNOUN2":
                        class0 = child.attrib
                        noun_dict = open(
                            "Data/noun_dict"
                            "/common_nouns.txt")
                        f1 = noun_dict.readlines()

                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                #temp.remove("\n")
                                temp.remove(arr1[5])
                                arr1.append(random.choice(temp[1:-1]))
                                print(arr1)

                        arr1.append("?")
                        print(arr1)
        listToStr = ' '.join(map(str, arr1))
        print(listToStr)
    return listToStr

def OpenSvoo():
    doc = Et.parse("Data/templates/interrogative/when/svoo/open.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:
            if phrase.tag == "PREFIX":
                arr1.append(phrase.text)  # adding "what"

            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                break
                        arr1.append(temp[1])


                    if child.tag == "PRONOUN":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/pronouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                        arr1.append(random.choice(arr0))

            if phrase.tag == "VERBPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                        arr1.append(random.choice(temp[1:-1]))

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:
                    if child.tag == "ARTICLE":
                        class0 = child.attrib
                        arr1.append("the")


                    if child.tag == "CNOUN1":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))

                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open("Data/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(temp[1])

                    if child.tag == "CNOUN2":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()

                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                temp.remove(arr1[5])
                                arr1.append(random.choice(temp[1:-1]))

                        arr1.append("?")

                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr)
    return listToStr + "."

# where
def BuySvoo():
    doc = Et.parse("Data/templates/interrogative/where/svoo/buy.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:
            if phrase.tag == "PREFIX":
                arr1.append(phrase.text)  # adding "what"

            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                break
                        arr1.append(temp[1])


                    if child.tag == "SNOUN":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                        arr1.append(random.choice(arr0))

            if phrase.tag == "VERBPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                        arr0 = []
                        arr1.append(temp[1])

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:
                    if child.tag == "ADJECTIVE":
                        class0 = child.attrib
                        noun_dict = open("Data/adjective_dict/adjective.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(temp[1])

                    if child.tag == "CNOUN1":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))

                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open("Data/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(temp[1])

                    if child.tag == "CNOUN2":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()

                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                temp.remove(arr1[5])
                                arr1.append(random.choice(temp[1:-1]))

                        arr1.append("?")

                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr)
    return listToStr + "."

def GoSvoo():
    doc = Et.parse("Data/templates/interrogative/where/svoo/go.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:
            if phrase.tag == "PREFIX":
                arr1.append(phrase.text)  # adding "what"

            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                break
                        arr1.append(temp[1])

                    if child.tag == "SNOUN":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                        arr1.append(random.choice(arr0))

            if phrase.tag == "VERBPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                        arr0 = []
                        arr1.append(temp[1])

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:
                    if child.tag == "PREPOSITION":
                        class0 = child.attrib
                        noun_dict = open("Data/preposition/preposition.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))

                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]) + ",")

                    if child.tag == "CNOUN1":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))

                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open("Data/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(temp[1])

                    if child.tag == "CNOUN2":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()

                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                temp.remove(arr1[6])
                                arr1.append(random.choice(temp[1:-1]))

                        arr1.append("?")

                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr)
    return listToStr + "."

def sentances():
    sen1 = DrinkSvoo()
    sen2 = EatSvoo()
    sen3 = CloseSvoo()
    sen4 = OpenSvoo()
    sen5 = BuySvoo()
    sen6 = GoSvoo()
    sentances = sen1, sen2, sen3, sen4, sen5, sen6
    return sentances

if __name__ == "__main__":
    sentances()