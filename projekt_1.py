"""
projekt_1.py

author: Martin Ondrůšek
email: ondrusek.martin89@gmail.com
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

words = TEXTS 
words1 = words[0].split() # Rozsekání stringu na jednotlivá slova
words2 = words[1].split() 
words3 = words[2].split() 

login = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}


print("Welcome to the Text Analysis!")
# Získání uživatelského vstupu
input_username = input("Type your username: \n")
input_password = input("Type your password: \n")

# Ověření uživatele a hesla
if input_username in login and login[input_username] == input_password:
    print("Hello, you have successfuly logged in!")
    text_number = int(input("Choose between 3 texts (1/2/3)\n"))
    if text_number == 1:
        print("you chose text number 1")
        count_words = len(words1)
        print(f"There are {count_words} words")
        count_title = sum(1 for word in words1 if word.istitle())
        print(f"There are {count_title} titlecase words")
        count_upper = sum(1 for word in words1 if word.isupper() and word.isalpha())
        print(f"There are {count_upper} uppercase words")
        count_lower = sum(1 for word in words1 if word.islower())
        print(f"There are {count_lower} lowercase words")
        count_numeric = sum(1 for number in words1 if number.isnumeric())
        print(f"There are {count_numeric} numeric strings") 
        total_sum = 0
        for word in words1:
            if word.isnumeric():
                total_sum += int(word)
        print(f"The sum of all numbers is {total_sum}") 
        
        cleaned_words1 = []
        for word in words1:
            cleaned_word = word.strip(",.")
            if cleaned_word:
                cleaned_words1.append(cleaned_word)
        # zjištění délky slov
        word_lenghts = []
        for word in cleaned_words1:
            word_lenghts.append(len(word))
        # zjištění četnosti slov
        lenght_counts = {}
        for lenght in word_lenghts:
            if lenght in lenght_counts:
                lenght_counts[lenght] += 1
            else:
                lenght_counts[lenght] = 1
        # Seřazení podle délky slov
        sorted_lenghts = sorted(lenght_counts.items())
        print("----------------------------------------")
        print("LEN|  OCCURRENCES  |NR.")
        print("----------------------------------------")
        for lenght, count in sorted_lenghts:
            graph = "*" * count
            print(f"{lenght:>3}|{graph:<13}|{count}")
        print("----------------------------------------")
    elif text_number == 2:
        print("you chose text number 2")
        count_words = len(words2)
        print(f"There are {count_words} words")
        count_title = sum(1 for word in words2 if word.istitle())
        print(f"There are {count_title} titlecase words")
        count_upper = sum(1 for word in words2 if word.isupper() and word.isalpha())
        print(f"There are {count_upper} uppercase words")
        count_lower = sum(1 for word in words2 if word.islower())
        print(f"There are {count_lower} lowercase words")
        count_numeric = sum(1 for number in words2 if number.isnumeric())
        print(f"There are {count_numeric} numeric strings") 
        total_sum = 0
        for word in words2:
            if word.isnumeric():
                total_sum += int(word)
        print(f"The sum of all numbers is {total_sum}") 
        
        cleaned_words2 = []
        for word in words2:
            cleaned_word = word.strip(",.")
            if cleaned_word:
                cleaned_words2.append(cleaned_word)
        # zjištění délky slov
        word_lenghts = []
        for word in cleaned_words2:
            word_lenghts.append(len(word))
        # zjištění četnosti slov
        lenght_counts = {}
        for lenght in word_lenghts:
            if lenght in lenght_counts:
                lenght_counts[lenght] += 1
            else:
                lenght_counts[lenght] = 1
        # Seřazení podle délky slov
        sorted_lenghts = sorted(lenght_counts.items())
        print("----------------------------------------")
        print("LEN|  OCCURRENCES  |NR.")
        print("----------------------------------------")
        for lenght, count in sorted_lenghts:
            graph = "*" * count
            print(f"{lenght:>3}|{graph:<17}|{count}")
        print("----------------------------------------")
    elif text_number == 3:
        print("you chose text number 3")
        count_words = len(words3)
        print(f"There are {count_words} words")
        count_title = sum(1 for word in words3 if word.istitle())
        print(f"There are {count_title} titlecase words")
        count_upper = sum(1 for word in words3 if word.isupper() and word.isalpha())
        print(f"There are {count_upper} uppercase words")
        count_lower = sum(1 for word in words3 if word.islower())
        print(f"There are {count_lower} lowercase words")
        count_numeric = sum(1 for number in words3 if number.isnumeric())
        print(f"There are {count_numeric} numeric strings") 
        total_sum = 0
        for word in words3:
            if word.isnumeric():
                total_sum += int(word)
        print(f"The sum of all numbers is {total_sum}") 
        
        cleaned_words3 = []
        for word in words3:
            cleaned_word = word.strip(",.")
            if cleaned_word:
                cleaned_words3.append(cleaned_word)
        # zjištění délky slov
        word_lenghts = []
        for word in cleaned_words3:
            word_lenghts.append(len(word))
        # zjištění četnosti slov
        lenght_counts = {}
        for lenght in word_lenghts:
            if lenght in lenght_counts:
                lenght_counts[lenght] += 1
            else:
                lenght_counts[lenght] = 1
        # Seřazení podle délky slov
        sorted_lenghts = sorted(lenght_counts.items())
        print("----------------------------------------")
        print("LEN|  OCCURRENCES  |NR.")
        print("----------------------------------------")
        for lenght, count in sorted_lenghts:
            graph = "*" * count
            print(f"{lenght:>3}|{graph:<15}|{count}")
        print("----------------------------------------")
    else:
        print("You have not logged in.")
else:
    print("not successful log in")








    

