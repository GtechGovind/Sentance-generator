import xml.etree.ElementTree as Et
import random

def buy():
    doc = Et.parse("Data/Complex/sentence/templates/compound/bought.xml")
    root = doc.getroot()
    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:
            if phrase.tag == "CLAUSE1":
                for child in phrase:
                    if child.tag == "SNOUN":
                        class0 = child.attrib
                        noun_dict = open(
                            "Data/Complex/sentence/noun_dict"
                            "/proper_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                break
                        arr1.append(random.choice(temp[3:-1]))
                        print(arr1)

                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data/Complex/sentence/verb_dict"
                            "/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                        arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "PREPOSITION":
                        class0 = child.attrib
                        preposition = open(
                            "Data/Complex/sentence/preposition" 
                            "/preposition.txt")
                        f1 = preposition.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                        arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "ARTICLE":
                        class0 = child.attrib
                        arr1.append("the")
                        print(arr1)

                    if child.tag == "CNOUN":
                        class0 = child.attrib

                        noun_dict = open(
                            "Data/Complex/sentence/noun_dict"
                            "/common_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                        arr1.append(random.choice(temp[1:-1]))
                        break
                        print(arr1)

            if phrase.tag == "CONJUNCTION":
                arr1.append("and")
                print(arr1)

            if phrase.tag == "CLAUSE2":
                for child in phrase:
                    if child.tag == "PRONOUN":
                        class0 = child.attrib
                        noun_dict = open(
                            "Data/Complex/sentence/noun_dict"
                            "/pronouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data/Complex/sentence/verb_dict"
                            "/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                break
                        arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "ADJECTIVE":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data/Complex/sentence/adjective_dict"
                            "/adjective.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                        arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open(
                            "Data/Complex/sentence/noun_dict"
                            "/common_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

        listToStr = ' '.join(map(str, arr1))
    return listToStr + "."

def went():
    doc = Et.parse("Data/Complex/sentence/compound/went.xml")
    #C:\Users\Govind\Desktop\sentomaker\Data\Complex\sentence\Compound
    root = doc.getroot()
    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:
            if phrase.tag == "CLAUSE1":
                for child in phrase:
                    if child.tag == "SNOUN":
                        class0 = child.attrib
                        noun_dict = open(
                            "Data/Complex/sentence/noun_dict"
                            "/proper_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                break
                        arr1.append(random.choice(temp[3:-1]))
                        print(arr1)

                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data/Complex/sentence/verb_dict"
                            "/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = 'went'
                        arr1.append(temp)
                        print(arr1)

                    if child.tag == "PREPOSITION":
                        class0 = child.attrib
                        preposition = open(
                            "Data/Complex/sentence/preposition" 
                            "/preposition.txt")
                        f1 = preposition.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                        arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "ARTICLE":
                        class0 = child.attrib
                        arr1.append("the")
                        print(arr1)

                    if child.tag == "CNOUN":
                        class0 = child.attrib

                        noun_dict = open(
                            "Data/Complex/sentence/noun_dict"
                            "/common_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                        arr1.append(random.choice(temp[1:-1]))
                        break
                        print(arr1)

            if phrase.tag == "CONJUNCTION":
                arr1.append("and")
                print(arr1)

            if phrase.tag == "CLAUSE2":
                for child in phrase:
                    if child.tag == "PRONOUN":
                        class0 = child.attrib
                        noun_dict = open(
                            "Data/Complex/sentence/noun_dict"
                            "/pronouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data/Complex/sentence/verb_dict"
                            "/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                break
                        arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "ADJECTIVE":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data/Complex/sentence/adjective_dict"
                            "/adjective.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                        arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open(
                            "Data/Complex/sentence/noun_dict"
                            "/common_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

        listToStr = ' '.join(map(str, arr1))
    return listToStr + "."

def study():
    doc = Et.parse("Data/Complex/sentence/compound/study.xml")
    root = doc.getroot()
    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:
            if phrase.tag == "CLAUSE1":
                for child in phrase:
                    if child.tag == "SNOUN":
                        class0 = child.attrib
                        noun_dict = open(
                            "Data/Complex/sentence/noun_dict"
                            "/proper_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                break
                        arr1.append(random.choice(temp[3:-1]))
                        print(arr1)

                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data/Complex/sentence/verb_dict"
                            "/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = 'went'
                        arr1.append(temp)
                        print(arr1)

                    if child.tag == "PREPOSITION":
                        class0 = child.attrib
                        preposition = open(
                            "Data/Complex/sentence/preposition" 
                            "/preposition.txt")
                        f1 = preposition.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                        arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "CNOUN":
                        class0 = child.attrib

                        noun_dict = open(
                            "Data/Complex/sentence/noun_dict"
                            "/common_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                        arr1.append(temp[1])
                        break
                        print(arr1)

            if phrase.tag == "CONJUNCTION":
                arr1.append("and")
                print(arr1)

            if phrase.tag == "CLAUSE2":
                for child in phrase:
                    if child.tag == "PRONOUN":
                        class0 = child.attrib
                        noun_dict = open(
                            "Data/Complex/sentence/noun_dict"
                            "/pronouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data/Complex/sentence/verb_dict"
                            "/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                break
                        arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open(
                            "Data/Complex/sentence/noun_dict"
                            "/common_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

        listToStr = ' '.join(map(str, arr1))
    return listToStr + "."