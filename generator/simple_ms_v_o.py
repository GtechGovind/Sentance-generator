import xml.etree.ElementTree as Et
import random

def AskSsvo():
    doc = Et.parse("Data\\templates\simple\ssvo\Ask.xml")
    root = doc.getroot()
 
    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence
        gender_list = ["male", "female"]
     
        for phrase in sentence:
         
            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:

                    if child.tag == "SNOUN1":
                        class0 = child.attrib
                        if class0["class"] == "name":
                            noun_dict = open("Data/noun_dict/proper_nouns.txt")

                            f1 = noun_dict.readlines()
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")
                                    arr0.extend(temp[3:-1])

                            arr1.append(random.choice(arr0))
                            print(arr1)

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
                        if class0["class"] == "name":

                            noun_dict = open("Data/noun_dict/proper_nouns.txt")

                            f1 = noun_dict.readlines()
                            arr0 = []
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")

                                    arr0.extend(temp[3:-1])
                         
                            arr0.remove(arr1[0])
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
                              
                                arr1.append(random.choice(temp[1:-1]))
                                print(arr1)

                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr + ".")
    return listToStr + "."

def BuySsvo():
    doc = Et.parse("Data\\templates/simple/SSVO/Buy.xml")
    
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence
        gender_list = ["male", "female"]
      
        for phrase in sentence:
          

            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:

                    if child.tag == "SNOUN1":
                        class0 = child.attrib
                        if class0["class"] == "name":
                            noun_dict = open("Data/noun_dict/proper_nouns.txt")

                            f1 = noun_dict.readlines()
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")
                                    arr0.extend(temp[3:-1])
                            #print(arr0)
                            arr1.append(random.choice(arr0))
                            print(arr1)

                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open("Data/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                #print(temp)
                                #print(arr0)
                        arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "SNOUN2":
                        class0 = child.attrib
                        if class0["class"] == "name":

                            noun_dict = open("Data/noun_dict/proper_nouns.txt")

                            f1 = noun_dict.readlines()
                            arr0 = []
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")

                                    arr0.extend(temp[3:-1])
                            #print(arr0)
                            arr0.remove(arr1[0])
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
                               
                                arr1.append(random.choice(temp[1:-1]))
                                print(arr1)

                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr + ".")

    return listToStr + "."

def CloseSsvo():
    doc = Et.parse("Data\\templates\simple\ssvo\Close.xml")
    root = doc.getroot()


    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence
        gender_list = ["male", "female"]
    
        for phrase in sentence:
          
            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:

                    if child.tag == "SNOUN1":
                        class0 = child.attrib
                        if class0["class"] == "name":
                            noun_dict = open("Data/noun_dict/proper_nouns.txt")

                            f1 = noun_dict.readlines()
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")
                                    arr0.extend(temp[3:-1])
                            #print(arr0)
                            arr1.append(random.choice(arr0))
                            print(arr1)

                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open("Data/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                #print(temp)
                                #print(arr0)
                        arr1.append(temp[1])
                        print(arr1)

                    if child.tag == "SNOUN2":
                        class0 = child.attrib
                        if class0["class"] == "name":

                            noun_dict = open("Data/noun_dict/proper_nouns.txt")

                            f1 = noun_dict.readlines()
                            arr0 = []
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")

                                    arr0.extend(temp[3:-1])
                            #print(arr0)
                            arr0.remove(arr1[0])
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
                               

                        arr0 = []
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
                            
                                arr1.append(random.choice(temp[1:-1]))
                                #print(arr1)

                                listToStr = ' '.join(map(str, arr1))
                                print(listToStr + ".")
                     
    return listToStr + "."

def DrinkSsvo():
    doc = Et.parse("Data\\templates/simple/SSVO/Drink.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence
        gender_list = ["male", "female"]
      
        for phrase in sentence:

            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:

                    if child.tag == "SNOUN1":
                        class0 = child.attrib
                        if class0["class"] == "name":
                            noun_dict = open("Data/noun_dict/proper_nouns.txt")

                            f1 = noun_dict.readlines()
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")
                                    arr0.extend(temp[3:-1])
                           
                            arr1.append(random.choice(arr0))
                            #print(arr1)

                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open("Data/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                                #print(temp)
                                #print(arr0)
                        arr1.append(temp[1])
                        #print(arr1)

                    if child.tag == "SNOUN2":
                        class0 = child.attrib
                        if class0["class"] == "name":

                            noun_dict = open("Data/noun_dict/proper_nouns.txt")

                            f1 = noun_dict.readlines()
                            arr0 = []
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")

                                    arr0.extend(temp[3:-1])
                        
                            arr0.remove(arr1[0])
                            arr1.append(random.choice(arr0))
                            #print(arr1)

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
                        #print(arr1)

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:

                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                            
                                arr1.append(random.choice(temp[1:-1]))
                        #print(arr1)

                    if child.tag == "PREPOSITION":
                        class0 = child.attrib
                        arr1.append("at")
                        #print(arr1)

                    if child.tag == "ARTICLE":
                        class0 = child.attrib
                        arr1.append("the")
                        #print(arr1)

                    if child.tag == "CNOUN1":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))
                                #print(arr1)

                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr + ".")
    return listToStr + "."

def EatSsvo():
    doc = Et.parse("Data\\templates\simple\ssvo\Eat.xml")
    root = doc.getroot()

    for sentence in root:
        arr0 = []  # for storing class and tags
        arr1 = []  # for storing sentence
        gender_list = ["male", "female"]
       
        for phrase in sentence:

            if phrase.tag == "SUBJECTPHRASE":
                for child in phrase:

                    if child.tag == "SNOUN1":
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
                            #print(arr1)

                    if child.tag == "CONJUNCTION":
                        class0 = child.attrib
                        conj = open("Data/conjunction.txt")
                        f1 = conj.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                               
                        arr1.append(temp[1])
                        #print(arr1)

                    if child.tag == "SNOUN2":
                        class0 = child.attrib
                        if class0["class"] == "name":
                            noun_dict = open("Data/noun_dict/proper_nouns.txt")

                            f1 = noun_dict.readlines()
                            for i in f1:
                                if i.find(class0["class"] + ":", 0) == 0:
                                    temp = i.split(":")
                                    arr0.extend(temp[3:-1])
                            #print(arr0)
                            arr0.remove(arr1[0])
                            arr1.append(random.choice(arr0))
                            #print(arr1)
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
                        #print(arr1)

            if phrase.tag == "OBJECTPHRASE":
                for child in phrase:

                    if child.tag == "CNOUN":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) == 0:
                                temp = i.split(":")
                              
                                arr1.append(random.choice(temp[1:-1]))
                        #print(arr1)

                    if child.tag == "PREPOSITION":
                        class0 = child.attrib
                        arr1.append("at")
                        #print(arr1)

                    if child.tag == "ARTICLE":
                        class0 = child.attrib
                        arr1.append("the")
                        #print(arr1)

                    if child.tag == "CNOUN1":
                        class0 = child.attrib
                        noun_dict = open("Data/noun_dict/common_nouns.txt")
                        f1 = noun_dict.readlines()
                        for i in f1:
                            if i.find(class0["class"] + ":", 0) >= 0:
                                temp = i.split(":")
                                arr1.append(random.choice(temp[1:-1]))
                                #print(arr1)

                        listToStr = ' '.join(map(str, arr1))
                        print(listToStr + ".")
    return listToStr + "."

def sentances():
    sen1 = AskSsvo()
    sen2 = BuySsvo()
    sen3 = CloseSsvo()
    sen4 = DrinkSsvo()
    sen5 = EatSsvo()
    sentances = sen1 , sen2, sen3, sen4, sen5
    return sentances

if __name__ == "__main__":
    sentances()