import xml.etree.ElementTree as Et
import random


import xml.etree.ElementTree as Et
import random


def order_bring():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_order\order-bring.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for phrase in sentence:
            if phrase.tag=="ORDERPHRASE":
                for child in phrase:
                    if child.tag=="EXPRESSION":
                        arr1.append(child.text)
                    if child.tag == "PERSONALPRONOUN":
                        arr1.append("your")

                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data\exc\\verb_dict\\verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[1:]))
                                break
                    if child.tag == "ARTICLE":
                        arr1.append("the")
                    if child.tag=="CNOUN":
                        class0 = child.attrib
                        temp = []
                        noun_dict = open("Data\exc\\noun_dict\common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp=i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[3:]))
                                arr1.append("!")
                                break

        listToStr = ' '.join(map(str, arr1))
        print(listToStr)
    return listToStr

def order_drink():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_order\order-drink.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for phrase in sentence:
            if phrase.tag=="ORDERPHRASE":
                for child in phrase:
                    if child.tag=="EXPRESSION":
                        arr1.append(child.text)
                    if child.tag == "PERSONALPRONOUN":
                        arr1.append("your")

                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data\exc\\verb_dict"
                            "\\verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[1:]))
                                break
                    if child.tag == "ARTICLE":
                        arr1.append("the")
                    if child.tag=="CNOUN":
                        class0 = child.attrib
                        temp = []
                        noun_dict = open(
                            "Data\exc\\noun_dict"
                            "\\common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp=i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[3:]))
                                arr1.append("!")
                                break

        listToStr = ' '.join(map(str, arr1))
        return listToStr

def order_eat():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_order\order-eat.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for phrase in sentence:
            if phrase.tag=="ORDERPHRASE":
                for child in phrase:
                    if child.tag=="EXPRESSION":
                        arr1.append(child.text)
                    if child.tag == "PERSONALPRONOUN":
                        arr1.append("your")

                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data\exc\\verb_dict"
                            "\\verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[1:]))
                                break
                    if child.tag == "ARTICLE":
                        arr1.append("the")
                    if child.tag=="CNOUN":
                        class0 = child.attrib
                        temp = []
                        noun_dict = open(
                            "Data\exc\\noun_dict"
                            "\\common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp=i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[3:]))
                                arr1.append("!")
                                break

        listToStr = ' '.join(map(str, arr1))
    return listToStr

def order_open():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_order\order-open.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for phrase in sentence:
            if phrase.tag=="ORDERPHRASE":
                for child in phrase:
                    if child.tag=="EXPRESSION":
                        arr1.append(child.text)
                    if child.tag == "PERSONALPRONOUN":
                        arr1.append("your")

                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data\exc\\verb_dict"
                            "\\verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[1:]))
                                break
                    if child.tag == "ARTICLE":
                        arr1.append("the")
                    if child.tag=="CNOUN":
                        class0 = child.attrib
                        temp = []
                        noun_dict = open(
                            "Data\exc\\noun_dict"
                            "\\common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp=i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[3:]))
                                arr1.append("!")
                                break

        listToStr = ' '.join(map(str, arr1))
    return listToStr

def order_pick():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_order\order-pick.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for phrase in sentence:
            if phrase.tag=="ORDERPHRASE":
                for child in phrase:
                    if child.tag=="EXPRESSION":
                        arr1.append(child.text)
                    if child.tag == "PERSONALPRONOUN":
                        arr1.append("your")

                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data\exc\\verb_dict"
                            "\\verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[1:]))
                                break
                    if child.tag == "ARTICLE":
                        arr1.append("the")
                    if child.tag=="CNOUN":
                        class0 = child.attrib
                        temp = []
                        noun_dict = open(
                            "Data\exc\\noun_dict"
                            "\\common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp=i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[3:]))
                                arr1.append("!")
                                break

        listToStr = ' '.join(map(str, arr1))
    return listToStr

def order_read():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_order\order-read.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for phrase in sentence:
            if phrase.tag=="ORDERPHRASE":
                for child in phrase:
                    if child.tag=="EXPRESSION":
                        arr1.append(child.text)
                    if child.tag == "PERSONALPRONOUN":
                        arr1.append("your")

                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data\exc\\verb_dict"
                            "\\verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[1:]))
                                break
                    if child.tag == "ARTICLE":
                        arr1.append("the")
                    if child.tag=="CNOUN":
                        class0 = child.attrib
                        temp = []
                        noun_dict = open(
                            "Data\exc\\noun_dict"
                            "\\common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp=i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[3:]))
                                arr1.append("!")
                                break

        listToStr = ' '.join(map(str, arr1))
    return listToStr    

import xml.etree.ElementTree as Et
import random


def order_shutup():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_order\order-shutup.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for phrase in sentence:
            if phrase.tag=="ORDERPHRASE":
                for child in phrase:
                    if child.tag=="EXPRESSION":
                        arr1.append(child.text)
                    if child.tag == "PERSONALPRONOUN":
                        arr1.append("your")

                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open(
                            "Data\exc\\verb_dict"
                            "\\verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[1:]))
                                break
                    if child.tag == "ARTICLE":
                        arr1.append("the")
                    if child.tag=="CNOUN":
                        class0 = child.attrib
                        temp = []
                        noun_dict = open(
                            "Data\exc\\noun_dict"
                            "\\common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp=i.split(":")
                                temp.remove("\n")
                                arr1.append(random.choice(temp[3:]))
                                arr1.append("!")
                                break

        listToStr = ' '.join(map(str, arr1))
    return listToStr

def exclamatory_order():
    order_bring()
    order_drink()
    order_eat()
    order_open()
    order_pick()
    order_read()
    order_shutup()

if __name__ == "__main__":
    exclamatory_order()