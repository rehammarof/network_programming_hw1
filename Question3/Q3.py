import json

words={}

def load():
    f = open("db.json", "r")
    db=f.read()
    words.update(json.loads(db))

def save():
    db = json.dumps(words)
    f = open("db.json", "w")
    f.write(db)
    f.close()

load()

print("Welcome to Translator app")
developer = input("Are you a translator developer? (y/n): ")

if developer=='y':
    en_word=""
    while en_word!="exit":
        en_word=input("Enter a new word or 'save' or 'exit': ")
        if en_word=="save":
            save()
            print('The db is successfully saved')
        elif en_word!="exit":
            ar_word=input("What the translation of '{0}' to Arabic: ".format(en_word))
            words[en_word]=ar_word
else:
    en_word=""
    while en_word!="exit":
        en_word=input("Enter a word to translate or 'exit': ")
        if en_word!="exit":
            if en_word in words:
                ar_word=words[en_word]
                print("'{0}' in arabic is: {1}".format(en_word,ar_word))
            else:
                print('No Translation')
