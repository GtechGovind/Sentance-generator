# Using ElementTree
import xml.etree.ElementTree as Et
import random


def how_drink():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_how\how-drink.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for child in sentence:
            if child.tag=="PREFIX":
                arr1.append(child.text)
            if child.tag=="ADVERB":
                class0=child.attrib
                adverb_dict = open(
                    "Data\exc\\adverb_dict"
                    "\\adverb.txt")
                f1 = adverb_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp=i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[2:]))
            if child.tag == "PRONOUN":
                class0=child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\pronouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[2:]))

            if child.tag == "SNOUN":
                class0=child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\proper_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[3:]))

            if child.tag == "VERB":
                class0 = child.attrib
                verb_dict = open("Data\exc\\verb_dict\\verbs.txt")
                f1 = verb_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[1:]))
            if child.tag == "ARTICLE":
                arr1.append("the")
            if child.tag=="CNOUN":
                class0 = child.attrib
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
            if child.tag=="CNOUN1":
                class0 = child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\common_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp=i.split(":")
                        temp.remove("\n")

                        break
                arr1.append(random.choice(temp[3:]))
        listToStr = ' '.join(map(str, arr1))
        if listToStr.find("!")==-1:
            listToStr+="!"
    print(listToStr)
    return listToStr

def how_eat():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_how\how-eat.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for child in sentence:
            if child.tag=="PREFIX":
                arr1.append(child.text)
            if child.tag=="ADVERB":
                class0=child.attrib
                adverb_dict = open(
                    "Data\exc\\adverb_dict"
                    "\\adverb.txt")
                f1 = adverb_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp=i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[2:]))
            if child.tag == "PRONOUN":
                class0=child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\pronouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[2:]))

                # arr1.append("your")
            if child.tag == "SNOUN":
                class0=child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\proper_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[3:]))

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
                        break
                arr1.append(random.choice(temp[1:]))
            if child.tag == "ARTICLE":
                arr1.append("the")
            if child.tag=="CNOUN":
                class0 = child.attrib
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
            if child.tag=="CNOUN1":
                class0 = child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\common_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp=i.split(":")
                        temp.remove("\n")

                        break
                arr1.append(random.choice(temp[3:]))
        listToStr = ' '.join(map(str, arr1))
        if listToStr.find("!")==-1:
            listToStr+="!"
    return listToStr


def how_fly():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_how\how-fly.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for child in sentence:
            if child.tag=="PREFIX":
                arr1.append(child.text)
            if child.tag=="ADVERB":
                class0=child.attrib
                adverb_dict = open(
                    "Data\exc\\adverb_dict"
                    "\\adverb.txt")
                f1 = adverb_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp=i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[2:]))
            if child.tag == "PRONOUN":
                class0=child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\pronouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[2:]))

                # arr1.append("your")
            if child.tag == "SNOUN":
                class0=child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\proper_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[3:]))

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
                        break
                arr1.append(random.choice(temp[1:]))
            if child.tag == "ARTICLE":
                arr1.append("the")
            if child.tag=="CNOUN":
                class0 = child.attrib
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
            if child.tag=="CNOUN1":
                class0 = child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\common_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp=i.split(":")
                        temp.remove("\n")

                        break
                arr1.append(random.choice(temp[3:]))
        listToStr = ' '.join(map(str, arr1))
        if listToStr.find("!")==-1:
            listToStr+="!"
    return listToStr


def how_literary1():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_how\how-literary.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for child in sentence:
            if child.tag=="PREFIX":
                arr1.append(child.text)
            if child.tag=="ADVERB":
                class0=child.attrib
                adverb_dict = open(
                    "Data\exc\\adverb_dict"
                    "\\adverb.txt")
                f1 = adverb_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp=i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[2:]))
            if child.tag == "PRONOUN":
                class0=child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\pronouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[2:]))

                # arr1.append("your")
            if child.tag == "SNOUN":
                class0=child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\proper_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[3:]))

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
                        break
                arr1.append(random.choice(temp[1:]))
            if child.tag == "ARTICLE":
                arr1.append("the")
            if child.tag=="CNOUN":
                class0 = child.attrib
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
            if child.tag=="CNOUN1":
                class0 = child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\common_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp=i.split(":")
                        temp.remove("\n")

                        break
                arr1.append(random.choice(temp[3:]))
        listToStr = ' '.join(map(str, arr1))
        if listToStr.find("!")==-1:
            listToStr+="!"
    return listToStr

# Using ElementTree
import xml.etree.ElementTree as Et
import random


def how_literary2():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_how\how-literary1.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for child in sentence:
            if child.tag=="PREFIX":
                arr1.append(child.text)
            if child.tag=="ADVERB":
                class0=child.attrib
                adverb_dict = open(
                    "Data\exc\\adverb_dict"
                    "\\adverb.txt")
                f1 = adverb_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp=i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[2:]))
            if child.tag == "PRONOUN":
                class0=child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\pronouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[2:]))

                # arr1.append("your")
            if child.tag == "SNOUN":
                class0=child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\proper_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[3:]))

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
                        break
                arr1.append(random.choice(temp[1:]))
            if child.tag == "ARTICLE":
                arr1.append("the")
            if child.tag=="CNOUN":
                class0 = child.attrib
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
            if child.tag=="CNOUN1":
                class0 = child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\common_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp=i.split(":")
                        temp.remove("\n")

                        break
                arr1.append(random.choice(temp[3:]))
        listToStr = ' '.join(map(str, arr1))
        if listToStr.find("!")==-1:
            listToStr+="!"
    return listToStr

def how_literary():
    sentances = how_literary1(), how_literary2()
    n = random.randint(0, 1)
    return sentances[n]

def how_movement1():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_how\how-movement.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for child in sentence:
            if child.tag=="PREFIX":
                arr1.append(child.text)
            if child.tag=="ADVERB":
                class0=child.attrib
                adverb_dict = open(
                    "Data\exc\\adverb_dict"
                    "\\adverb.txt")
                f1 = adverb_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp=i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[2:]))
            if child.tag == "PRONOUN":
                class0=child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\pronouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[2:]))

                # arr1.append("your")
            if child.tag == "SNOUN":
                class0=child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\proper_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[3:]))

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
                        break
                arr1.append(random.choice(temp[1:]))
            if child.tag == "ARTICLE":
                arr1.append("the")
            if child.tag=="CNOUN":
                class0 = child.attrib
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
            if child.tag=="CNOUN1":
                class0 = child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\common_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp=i.split(":")
                        temp.remove("\n")

                        break
                arr1.append(random.choice(temp[3:]))
        listToStr = ' '.join(map(str, arr1))
        if listToStr.find("!")==-1:
            listToStr+="!"
    return listToStr

def how_movement2():
    doc = Et.parse("Data\exc\\templates\Exclamatory\exc_how\how-movement1.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []
        arr1 = []
        for child in sentence:
            if child.tag=="PREFIX":
                arr1.append(child.text)
            if child.tag=="ADVERB":
                class0=child.attrib
                adverb_dict = open(
                    "Data\exc\\adverb_dict"
                    "\\adverb.txt")
                f1 = adverb_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp=i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[2:]))
            if child.tag == "PRONOUN":
                class0=child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\pronouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[2:]))

                # arr1.append("your")
            if child.tag == "SNOUN":
                class0=child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\proper_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp = i.split(":")
                        temp.remove("\n")
                        break
                arr1.append(random.choice(temp[3:]))

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
                        break
                arr1.append(random.choice(temp[1:]))
            if child.tag == "ARTICLE":
                arr1.append("the")
            if child.tag=="CNOUN":
                class0 = child.attrib
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
            if child.tag=="CNOUN1":
                class0 = child.attrib
                noun_dict = open(
                    "Data\exc\\noun_dict"
                    "\\common_nouns.txt")
                f1 = noun_dict.readlines()
                for i in f1:
                    if i.find(class0["class"] + ":", 0) >= 0:
                        temp=i.split(":")
                        temp.remove("\n")

                        break
                arr1.append(random.choice(temp[3:]))
        listToStr = ' '.join(map(str, arr1))
        if listToStr.find("!")==-1:
            listToStr+="!"
    return listToStr

def how_movement():
    sentances = how_movement1(), how_movement2()
    n = random.randint(0, 1)
    return sentances[n]

def exclamatory_how():
    how_drink()
    how_eat()
    how_fly()
    how_literary()
    how_movement()

if __name__ == '__main__':
    exclamatory_how()