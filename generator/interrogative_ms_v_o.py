import xml.etree.ElementTree as Et
import random

#what
def DrinkSsvo():
    doc = Et.parse("Data/templates/interrogative/what/ssvo/drink.xml")
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


                    if child.tag == "SNOUN1":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                        arr1.append(random.choice(arr0))

                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open("Data/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")

                                arr1.append(temp[1])

                    if child.tag == "SNOUN2":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                        arr1.append(random.choice(arr0))
                        if arr1[4] == arr1[2]:
                            arr0.remove(arr1[2])
                            arr1.remove(arr1[4])
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

def EatSsvo():
    doc = Et.parse("Data/templates/interrogative/what/ssvo/eat.xml")
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


                    if child.tag == "SNOUN1":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                        arr1.append(random.choice(arr0))


                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open("Data/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(temp[1])

                    if child.tag == "SNOUN2":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                        arr1.append(random.choice(arr0))
                        if arr1[4] == arr1[2]:
                            arr0.remove(arr1[2])
                            arr1.remove(arr1[4])
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

#when
def CloseSsvo():
    doc = Et.parse("Data/templates/interrogative/when/ssvo/close.xml")
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

                    if child.tag == "SNOUN1":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])

                        arr1.append(random.choice(arr0))


                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open("Data/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(temp[1])

                    if child.tag == "SNOUN2":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        arr0 = []
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                        arr1.append(random.choice(arr0))
                        if arr1[4] == arr1[2]:
                            arr0.remove(arr1[2])
                            arr1.remove(arr1[4])
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
                        print(listToStr)
    return listToStr + "."

def FlySsvo():
    doc = Et.parse("Data/templates/interrogative/when/ssvo/fly.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence
        gender_list = ["male", "female"]

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


                    if child.tag == "SNOUN1":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                        arr1.append(random.choice(arr0))


                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open("Data/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(temp[1])

                    if child.tag == "SNOUN2":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        arr0 = []
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                        arr1.append(random.choice(arr0))
                        if arr1[4] == arr1[2]:
                            arr0.remove(arr1[2])
                            arr1.remove(arr1[4])
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
                        preposition = open("Data/preposition/preposition.txt")
                        f1 = preposition.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(temp[1])

                    if child.tag == "NOUN":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/proper_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))
                        arr1.append("?")

                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr)
    return listToStr + "."

#where
def BuySsvo():
    doc = Et.parse("Data/templates/interrogative/where/ssvo/buy.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence
        gender_list = ["male", "female"]

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
                        print(arr1)

                    if child.tag == "SNOUN1":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                        arr1.append(random.choice(arr0))


                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open("Data/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "SNOUN2":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        arr0 = []
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                        arr1.append(random.choice(arr0))
                        if arr1[4] == arr1[2]:
                            arr0.remove(arr1[2])
                            arr1.remove(arr1[4])
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
                        print(listToStr)
    return listToStr + "."

def GoSsvo():
    doc = Et.parse("Data/templates/interrogative/where/ssvo/go.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence
        gender_list = ["male", "female"]

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

                    if child.tag == "SNOUN1":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                        arr1.append(random.choice(arr0))

                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open("Data/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(temp[1])

                    if child.tag == "SNOUN2":
                        class0 = child.attrib

                        noun_dict = open("Data/noun_dict/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        arr0 = []
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                        arr1.append(random.choice(arr0))
                        if arr1[4] == arr1[2]:
                            arr0.remove(arr1[2])
                            arr1.remove(arr1[4])
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
                        print(listToStr)
    return listToStr + "."

def sentances():
    sen1 = DrinkSsvo()
    sen2 = EatSsvo()
    sen3 = CloseSsvo()
    sen4 = FlySsvo()
    sen5 = BuySsvo()
    sen6 = GoSsvo()
    sentances = sen1, sen2, sen3, sen4, sen5, sen6
    return sentances

if __name__ == "__main__":
    sentances()