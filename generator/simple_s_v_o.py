import xml.etree.ElementTree as Et
import random

def AskSvo():
    doc = Et.parse("Data/templates/simple/svo/Ask.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence
        gender_list = ["male", "female"]
     
        for phrase in sentence:
       

            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:

                    if child.tag == "SNOUN":
                        class0 = child.attrib
                        if class0["class"] == "name":
                            noun_dict = open(
                                "Data/noun_dict"
                                "/proper_nouns.txt")

                            f1 = noun_dict.readlines()
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")
                                    arr0.extend(temp[3:-1])
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
                                break
                        arr0=[]
                        arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:
                
                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open(
                            "Data/noun_dict"
                            "/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

                    if child.tag == "PREPOSITION":
                        class0 = child.attrib
                        arr1.append("in")
                        print(arr1)

                    if child.tag == "ARTICLE1":
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
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))
                                print(arr1)

                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr + ".")
    return listToStr + "."

def BuySvo():
    doc = Et.parse("Data/templates/simple/SVO/Buy.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence
        gender_list = ["male", "female"]
       
        for phrase in sentence:
          
            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:

                    if child.tag == "SNOUN":
                        class0 = child.attrib
                        if class0["class"] == "name":
                            noun_dict = open("Data/noun_dict/proper_nouns.txt")

                            f1 = noun_dict.readlines()
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")
                                    arr0.extend(temp[3:-1])
                            # print(arr0)
                            arr1.append(random.choice(arr0))
                            print(arr1)

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
                        arr0=[]
                        arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:
                   
                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                               # temp.remove("\n")
                                arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

                    if child.tag == "PREPOSITION":
                        class0 = child.attrib
                        arr1.append("from")
                        print(arr1)

                    if child.tag == "ARTICLE":
                        class0 = child.attrib
                        arr1.append("the")
                        print(arr1)

                    if child.tag == "CNOUN1":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                #temp.remove("\n")
                                arr1.append(random.choice(temp[1:-1]))
                                print(arr1)

                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr + ".")

    return listToStr + "."

def CloseSvo():
    doc = Et.parse("Data/templates/simple/SVO/Close.xml")
    root = doc.getroot()

  
    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence
        gender_list = ["male", "female"]
       
        for phrase in sentence:

            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:

                    if child.tag == "SNOUN":
                        class0 = child.attrib
                        if class0["class"] == "name":
                            noun_dict = open("Data/noun_dict/proper_nouns.txt")

                            f1 = noun_dict.readlines()
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")
                                    arr0.extend(temp[3:-1])
                            # print(arr0)
                            arr1.append(random.choice(arr0))
                            print(arr1)

            if phrase.tag == "VERBPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                #temp.remove("\n")
                                # print(temp)
                                break
                        arr0=[]
                        arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:
                  
                    if child.tag == "ARTICLE":
                        class0 = child.attrib
                        arr1.append("the")
                        print(arr1)

                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                               # temp.remove("\n")
                                arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

                    if child.tag == "PREPOSITION":
                        class0 = child.attrib
                        arr1.append("of")
                        print(arr1)

                    if child.tag == "ARTICLE1":
                        class0 = child.attrib
                        arr1.append("the")
                        print(arr1)

                    if child.tag == "CNOUN1":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                #temp.remove("\n")
                                arr1.append(random.choice(temp[1:-1]))
                                print(arr1)



                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr + ".")
    return listToStr + "."

def DrinkSvo():
    doc = Et.parse("Data/templates/simple/SVO/Drink.xml")
    root = doc.getroot()


    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence
        gender_list = ["male", "female"]

        for phrase in sentence:
            
            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:

                    if child.tag == "SNOUN":
                        class0 = child.attrib
                        if class0["class"] == "name":
                            noun_dict = open("Data/noun_dict/proper_nouns.txt")

                            f1 = noun_dict.readlines()
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")
                                    arr0.extend(temp[3:-1])
                            # print(arr0)
                            arr1.append(random.choice(arr0))
                            print(arr1)

            if phrase.tag == "VERBPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                #temp.remove("\n")
                                # print(temp)
                                break
                        arr0=[]
                        arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:

                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                               # temp.remove("\n")
                                arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

                    if child.tag == "PREPOSITION":
                        class0 = child.attrib
                        arr1.append("in")
                        print(arr1)

                    if child.tag == "ARTICLE":
                        class0 = child.attrib
                        arr1.append("the")
                        print(arr1)

                    if child.tag == "CNOUN1":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                #temp.remove("\n")
                                arr1.append(random.choice(temp[1:-1]))
                                print(arr1)

                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr + ".")

    return listToStr + "."

def EatSvo():
    doc = Et.parse("Data/templates/simple/SVO/Eat.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence
        gender_list = ["male", "female"]
       
        for phrase in sentence:

            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:

                    if child.tag == "SNOUN":
                        class0 = child.attrib
                        if class0["class"] == "name":
                            noun_dict = open("Data/noun_dict/proper_nouns.txt")

                            f1 = noun_dict.readlines()
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")
                                    arr0.extend(temp[3:-1])
                            # print(arr0)
                            arr1.append(random.choice(arr0))
                            print(arr1)

            if phrase.tag == "VERBPHRASE":
                for child in phrase:
                    if child.tag == "VERB":
                        class0 = child.attrib
                        verb_dict = open("Data/verb_dict/verbs.txt")
                        f1 = verb_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                #temp.remove("\n")
                                # print(temp)
                                break
                        arr0=[]
                        arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:
                 
                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                               # temp.remove("\n")
                                arr1.append(random.choice(temp[1:-1]))
                        print(arr1)

                    if child.tag == "PREPOSITION":
                        class0 = child.attrib
                        arr1.append("in")
                        print(arr1)

                    if child.tag == "ARTICLE1":
                        class0 = child.attrib
                        arr1.append("the")
                        print(arr1)

                    if child.tag == "CNOUN1":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                #temp.remove("\n")
                                arr1.append(random.choice(temp[1:-1]))
                                print(arr1)

                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr + ".")
    return listToStr + "."


def sentances():
    sen1 = AskSvo()
    sen2 = BuySvo()
    sen3 = CloseSvo()
    sen4 = DrinkSvo()
    sen5 = EatSvo()
    sentances = sen1 , sen2, sen3, sen4, sen5
    return sentances

if __name__ == "__main__":
    sentances()