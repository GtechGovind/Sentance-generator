import xml.etree.ElementTree as Et
import random


def although():
    doc = Et.parse("Data/Complex/sentence/templates/complex/although/movie.xml")
    root = doc.getroot()
    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:
            if phrase.tag == "PREFIX":
                arr1.append(phrase.text)
                print(arr1)

            if phrase.tag == "CLAUSE1":
                for child in phrase:
                    if child.tag == "ARTICLE":
                        class0 = child.attrib
                        arr1.append("the")
                        print(arr1)

                    if child.tag == "NOUN":
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
                        arr1.append(",")

            if phrase.tag == "CLAUSE2":
                for child in phrase:
                    if child.tag == "NOUN":
                        class0 = child.attrib
                        noun_dict = open(
                            "Data/Complex/sentence/noun_dict"
                            "/common_nouns.txt")

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
                        arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "ADVERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data/Complex/sentence/adverb_dict"
                            "/adverb.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
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

        listToStr = ' '.join(map(str, arr1))
    return listToStr + "."

def whenever():
    doc = Et.parse("Data/Complex/sentence/templates/complex/whenever/play.xml")
    root = doc.getroot()
    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:
            if phrase.tag == "PREFIX":
                arr1.append(phrase.text)
                print(arr1)

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
                        arr1.append(",")

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
                                break
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
                        arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "PREPOSITION":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data/Complex/sentence/preposition"
                            "/preposition.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                        arr1.append(temp[1])
                        print(arr1)

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

                    if child.tag == "NOUN":
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

def old():
    doc = Et.parse("Data/Complex/sentence/complex/old.xml")
    #C:\Users\Govind\Desktop\sentomaker\Data\Complex\sentence\Complex
    root = doc.getroot()
    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence

        for phrase in sentence:
            if phrase.tag == "PREFIX":
                arr1.append(phrase.text)
                print(arr1)

            if phrase.tag == "CLAUSE1":
                for child in phrase:

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
                        arr1.append(",")

            if phrase.tag == "CLAUSE2":
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
                                arr0.extend(temp[3:-1])
                                # print(arr0)
                        # print(arr0)
                        arr1.append(random.choice(arr0))
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
                        verb_dict = open(
                            "Data/Complex/sentence/preposition"
                            "/preposition.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                        arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "ARTICLE":
                        arr1.append("a")

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
