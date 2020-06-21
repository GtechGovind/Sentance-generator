# import xml.dom.minidom
# Using ElementTree
import xml.etree.ElementTree as Et
import random

def wish_ms_v_o1():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_wish\ms_v_o\wish-multsvo.xml")
    root = doc.getroot()
    for sentence in root:
        arr0 = []
        arr1 = []
        for phrase in sentence:
            if phrase.tag == "SUBJECTPHRASE":
                class0 = phrase.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\abstract.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) == 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        arr0.append(random.choice(temp[1:]))
                        arr0.append(",")
                        arr1.append(temp[0])

                        break

            if phrase.tag == "SNOUN":
                class0 = phrase.attrib
                if class0["class"] == "wish-subject":
                    class0 = phrase.attrib
                    noun_dict = open(
                        "Data\exc\\noun_dict"
                        "\\abstract.txt")
                    f1 = noun_dict.readlines()
                    for i in f1:
                        if i.find(class0["class"] + ":", 0) == 0:
                            temp = i.split(":")
                            temp.remove("\n")
                            arr0.append(random.choice(temp[1:]))
                            check_str=arr0[-1]
                            arr0.append("!")
                            if check_str.find("to")>=0:
                                arr0.remove(",")
                            listToStr02 = ' '.join(map(str, arr0))
    return listToStr02

wish_ms_v_o1

def wish_ms_v_o2():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_wish\ms_v_o\wish-ssvo.xml")
    root = doc.getroot()
    for sentence in root:
        arr0 = []
        arr1 = []
        gender_list = ["male", "female"]

        for phrase in sentence:
            if phrase.tag == "SUBJECTPHRASE":

                class0 = phrase.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\abstract.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) == 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        arr0.append(random.choice(temp[1:]))
                        arr0.append(",")
                        arr02 = arr0[:]
                        arr1.append(temp[0])
            class0=phrase.attrib
            if phrase.tag == "SNOUN":
                if  class0["class"] == "name":
                    class0 = phrase.attrib
                    noun_dict = open(
                        "Data\exc\\noun_dict"
                        "\\proper_nouns.txt")

                    f1 = noun_dict.readlines()
                    for i in f1:
                        if i.find(class0["class"] + ":", 0) == 0:
                            if i.find(random.choice(gender_list), 0) >= 0:
                                temp = i.split(":")
                                temp.remove("\n")
                                arr0.append(random.choice(temp[3:]))
                                arr01 = arr0[:]
                                arr0.append("!")
                                arr01.append("and")
                                t=random.choice(temp[3:])
                                while t == arr01[-2]:
                                    t=random.choice(temp[3:])
                                arr01.append(t)
                                arr01.append("!")
                                arr1.append(temp[1])
                                listToStr01 = ' '.join(map(str, arr01))
                                break
    return listToStr01

def wish_ms_v_o():
    sentances = wish_ms_v_o1(), wish_ms_v_o2()
    n = random.randint(0, 1)
    return sentances[n]

def wish_s_v_o():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_wish\s_v_o\wish-svo.xml")
    root = doc.getroot()
    for sentence in root:
        arr0 = []
        arr1 = []
        gender_list = ["male", "female"]
        for phrase in sentence:
            if phrase.tag == "SUBJECTPHRASE":
                class0 = phrase.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\abstract.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) == 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        arr0.append(random.choice(temp[1:]))
                        arr0.append(",")
                        arr1.append(temp[0])
            if phrase.tag == "SNOUN":
                class0 = phrase.attrib
                if  class0["class"] == "name":
                    class0 = phrase.attrib
                    noun_dict = open(
                        "Data\exc\\noun_dict"
                        "\\proper_nouns.txt")

                    f1 = noun_dict.readlines()
                    for i in f1:
                        if i.find(class0["class"] + ":", 0) == 0:
                            if i.find(random.choice(gender_list), 0) >= 0:
                                temp = i.split(":")
                                temp.remove("\n")
                                arr0.append(random.choice(temp[3:]))
                                arr0.append("!")
                                t=random.choice(temp[3:])
                                arr1.append(temp[1])
                                listToStr0 = ' '.join(map(str, arr0))
                                print(listToStr0)
                                break
    return listToStr0