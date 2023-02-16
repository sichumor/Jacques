# command list for Jacques, the cooking Golem
import os
import datetime
from random import choice
from time import sleep
from textwrap import fill

TEXT_FILE_PATH = os.getcwd() + "/Speech_Files/"
RECIPE_PATH = os.getcwd() + "/Recipes/"

#---------- Initialize Golem ----------#
def do_nothing(golem):
    pass

def load_commands():
    commands = {'dismiss':do_nothing,
                'help':list_commands,
                'new recipe':new_recipe,
                'read recipe':read_recipe,
                'random':random_vocab,
                'search':search_recipes}
    return commands

#----------- DIALOGUE ----------#
PROMPT = "(Jacques) "

def random_file_line(filename):
    f = open(TEXT_FILE_PATH + filename,'r')
    line = choice(f.readlines()).strip()
    f.close()
    return line

def message(s,delay=1.5):
    print(fill(PROMPT + s,width=75))
    sleep(delay)

def generate_greeting():
    message(random_file_line("GREETINGS.txt"))

def generate_farewell():
    message(random_file_line("FAREWELLS.txt"))

def random_vocab(golem):
    line = random_file_line("VOCAB.txt").split(';')
    message(line[0],0.8)
    message(line[1])

def list_commands(golem):
    message("Ce sont les commandes disponibles...",0.8)
    print("new recipe",'\t',"Record something tres delicieux.")
    print("search",'\t\t',"Search your recipes for a keyword.")
    print("read recipe",'\t',"View one of your recipes.")
    print("random",'\t\t',"See a random French word")
    print("help",'\t\t',"See this list again.")
    print("dismiss",'\t',"Send me on my way.")

#---------- File manipulation ----------#
def make_text_file(path):
    message("Type as many lines as you wish, then a final line of 'STOP'.",1)
    lines = []
    next_line = ""
    while next_line != "STOP":
        next_line = input("(editor) ").strip()
        lines.append(next_line)
    file = open(path,'w')
    for line in lines[:-1]:
        file.write(line + "\n")
    file.close()

def new_recipe(golem):
    message("Oui, let me get the rolodex...")
    recipe = input("Et que faisons-nous? ").replace(" ","_")
    make_text_file(RECIPE_PATH + recipe + ".txt")
    message("Parfait! Your recipe has been saved.")

def file_contains(recipe,word):
    f = open(RECIPE_PATH + '/' + recipe,'r')
    result = word in f.read()
    f.close()
    return result

def search_recipes(golem):
    word = input("What would like to search for? ")
    recipes = [x for x in os.listdir(RECIPE_PATH)
               if ".txt" in x and file_contains(x,word)]
    if not recipes:
        message("Je suis desole, but there were no results.")
    else:
        message("The following recipes contained the word "+ word + ":")
        for recipe in recipes:
            print(recipe.replace("_"," ").replace(".txt",""))

def read_recipe(golem):
    recipe = input("Pour quoi? ").replace(" ","_") + ".txt"
    try:
        f = open(RECIPE_PATH + '/' + recipe,'r')
        message("Let me see...ah, c'est ici.",0.5)
        print(f.read().strip())
        f.close()
    except IOError:
        message("Je suis desole, I cannot find that.")

if __name__ == "__main__":
    pass
