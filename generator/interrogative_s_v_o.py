import xml.etree.ElementTree as Et
import random

# what
def DrinkSvo():
    doc = Et.parse("Data/templates/interrogative/what/svo/drink.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:
            if phrase.tag == "PREFIX":
                arr1.append(phrase.text)  # adding "what"
                print(arr1)
            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                temp.remove("\n")
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
                        arr1.append(random.choice(temp[1:-1]))

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:
                    if child.tag == "PREPOSITION":
                        class0 = child.attrib
                        arr1.append("from")
                    if child.tag == "ARTICLE":
                        class0 = child.attrib
                        arr1.append("the")
                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))
                        arr1.append("?")

                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr)
    return listToStr + "."

def EatSvo():
    doc = Et.parse("Data/templates/interrogative/what/svo/eat.xml")
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
                                temp.remove("\n")
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
                        arr1.append(random.choice(temp[1:-1]))

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:
                    if child.tag == "PREPOSITION":
                        class0 = child.attrib
                        arr1.append("from")
                    if child.tag == "ARTICLE":
                        class0 = child.attrib
                        arr1.append("the")
                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")

                                arr1.append(random.choice(temp[1:-1]))
                        arr1.append("?")

                        listToStr = ' '.join(map(str, arr1))
    return listToStr + "."

# when
def CloseSvo():
    doc = Et.parse("Data/templates/interrogative/when/svo/close.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:
            if phrase.tag == "PREFIX":
                arr1.append(phrase.text)  # adding "what"
                print(arr1)
            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                temp.remove("\n")

                                break
                        arr1.append(temp[1])


                    if child.tag == "PRONOUN":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/pronouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[1:-1])
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
                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))
                        arr1.append("?")

                        listToStr = ' '.join(map(str, arr1))
    return listToStr + "."

def OpenSvo():
    doc = Et.parse("Data/templates/interrogative/when/svo/open.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:

            if phrase.tag == "PREFIX":
                arr1.append(phrase.text)  # adding "what"
                print(arr1)
            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                temp.remove("\n")
                                break
                        arr1.append(temp[1])


                    if child.tag == "PRONOUN":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/pronouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[1:-1])

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
                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")

                                arr1.append(random.choice(temp[1:-1]))
                        arr1.append("?")

                        listToStr = ' '.join(map(str, arr1))
    return listToStr + "."

#where
def BuySvo():
    doc = Et.parse("Data/templates/interrogative/where/svo/buy.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:
            if phrase.tag == "PREFIX":
                arr1.append(phrase.text)  # adding "what"
                print(arr1)
            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                temp.remove("\n")
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


                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))
                        arr1.append("?")

                        listToStr = ' '.join(map(str, arr1))
    return listToStr + "."

def GoSvo():
    doc = Et.parse("Data/templates/interrogative/where/svo/go.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:
            if phrase.tag == "PREFIX":
                arr1.append(phrase.text)  # adding "what"
                print(arr1)
            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")

                        arr1.append(temp[1])


                    if child.tag == "SNOUN1":
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
                                arr1.append(random.choice(temp[1:-1]))
                        arr1.append("?")

                        listToStr = ' '.join(map(str, arr1))
    return listToStr + "."

def sentances():
    sen1 = DrinkSvo()
    sen2 = EatSvo()
    sen3 = CloseSvo()
    sen4 = OpenSvo()
    sen5 = BuySvo()
    sen6 = GoSvo()
    sentances = sen1, sen2, sen3, sen4, sen5, sen6
    return sentances

if __name__ == "__main__":
    sentances()