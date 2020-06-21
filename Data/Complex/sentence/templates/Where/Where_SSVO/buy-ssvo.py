#import xml.dom.minidom
#using ElementTree
import xml.etree.ElementTree as Et
import random


class BuySsvo:
    doc = Et.parse("B:/fyp/code/sentence/templates/Where/Where_SSVO/buy.xml")
    # doc = Et.parse("C:\\Users\\payal\\Desktop\\Navkar\\Smart_Learning\\code\\sentence\\templates\\simple0.xml")
    root = doc.getroot()

    # print(root.tag)
    # print(root.attrib)
    # print(et.tostring(root, encoding='utf8').decode('utf8'))
    # print([elem.tag for elem in root.iter()])
    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence
        gender_list = ["male", "female"]
        # print(sentence.tag)
        # print(sentence.attrib)
        # print()
        for phrase in sentence:
            # print(phrase.tag)
            # print(phrase.attrib)
            # print()
            if phrase.tag == "PREFIX":
                arr1.append(phrase.text) #adding "what"
                print(arr1)
            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "B:/fyp/code/sentence/verb_dict"
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

                    if child.tag == "SNOUN1":
                        class0 = child.attrib

                        noun_dict = open(
                            "B:/fyp/code/sentence/noun_dict"
                            "/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                                #print(arr0)
                        #print(arr0)
                        arr1.append(random.choice(arr0))
                        print(arr1)

                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open(
                            "B:/fyp/code/sentence/conjunction"
                            "/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                #temp.remove("\n")
                                arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "SNOUN2":
                        class0 = child.attrib

                        noun_dict = open(
                            "B:/fyp/code/sentence/noun_dict"
                            "/proper_nouns.txt")

                        f1 = noun_dict.readlines()
                        arr0 = []
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr0.extend(temp[3:-1])
                                #print(arr0)
                        #print(arr0)
                        arr1.append(random.choice(arr0))
                        if arr1[4] == arr1[2]:
                            arr0.remove(arr1[2])
                            arr1.remove(arr1[4])
                            arr1.append(random.choice(arr0))
                        print(arr1)

            if phrase.tag == "VERBPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "B:/fyp/code/sentence/verb_dict"
                            "/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                #temp.remove("\n")
                                # print(temp)
                        arr0 = []
                        arr1.append(temp[1])
                        print(arr1)

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:
                    if child.tag == "ADJECTIVE":
                        class0 = child.attrib
                        noun_dict = open(
                            "B:/fyp/code/sentence/adjective_dict"
                            "/adjective.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                              #  temp.remove("\n")
                                arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open(
                            "B:/fyp/code/sentence/noun_dict"
                            "/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                              #  temp.remove("\n")
                                arr1.append(random.choice(temp[1:-1]))
                        arr1.append("?")
                        print(arr1)
        listToStr = ' '.join(map(str, arr1))
        print(listToStr)