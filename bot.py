from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

def getShadowRoot(host):
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", host)
    return shadow_root

driver = webdriver.Safari()
driver.implicitly_wait(10)
driver.get("https://www.powerlanguage.co.uk/wordle/")

game_app = driver.find_element(By.TAG_NAME, "game-app")
game_app_root = getShadowRoot(game_app)

rows = game_app_root.find_elements(By.TAG_NAME, 'game-row')

correct = {} #letters that are in the correct position
absent = set() #letters that are not in the word
present = {} #letters that are in the word but not in the correct position

def main():
    closeModal()
    words = []
    with open("words") as w:
        words = [word.strip() for word in w.readlines()]
    
    guess = 'roate'               
    for i in range(0, len(rows)):
        populateRow(i, guess)
        sleep(2)
        words = trimList(words)
        absent = set()
        present = {}
        guess = words[random.randint(0, len(words))]


    #print(start)
    #print(len(words))

def closeModal():
    #closes the pop up modal that appears when the game starts
    game_modal = game_app_root.find_element(By.TAG_NAME, 'game-modal')
    game_modal_root = getShadowRoot(game_modal)
    driver.execute_script(
        "return arguments[0].querySelector('.close-icon').click()", \
        game_modal_root)

def populateRow(row, guess):
    #populates row with guess
    rows[row].send_keys(guess)
    rows[row].send_keys(Keys.ENTER)
    checkRow(row)

def checkRow(row):
    #checks all the letters in the row to see what letters are absent
    # present or correct and adds them to the appropriate arrays
    row_root = getShadowRoot(rows[row])
    tiles = driver.execute_script(
        "return arguments[0].querySelector('.row')", \
        row_root).find_elements(By.TAG_NAME, 'game-tile')
    
    for i in range(0, len(tiles)):
        status = driver.execute_script(
            "return arguments[0].getAttribute('evaluation')", tiles[i]
        )
        letter = driver.execute_script(
            "return arguments[0].getAttribute('letter')", tiles[i]
        )

        if status == 'correct':
            if letter in correct:
                correct[letter].add(i)
            else:
                present[letter] = {i}
        elif status == 'present':
            if letter in present:
                present[letter].add(i)
            else:
                present[letter] = {i}
        elif status == 'absent' and letter not in present:
            absent.add(letter)

def trimAbsent(wl):
    tmp = []
    if len(absent) > 0:
        for word in wl:
            removed = False
            for letter in absent:
                if letter in word:
                    removed = True
            if removed == False:
                tmp.append(word)
    return tmp

def trimPresent(wl):
    #TODO: needs fixing
    tmp=[]
    if len(present) > 0:
        for word in wl:
            removed = False
            for letter in present:
                for position in present[letter]:
                    if letter not in word:
                        removed = True
                        break
                    elif word[position] == letter:
                        removed = True
                
            if removed == False:
                tmp.append(word)
    return tmp
    
        
def trimList(wl):
    #TODO fix trimPresent
    #TODO seperate and fix trimCorrect
    tmp = wl
    if len(absent) > 0:
        tmp = trimAbsent(wl)
    if len(present) > 0:
        tmp = trimPresent(tmp)
        print(tmp)

#    if len(correct) > 0:
#        for word in wl:
#            removed = False
#            for letter in correct:
#                for position in correct[letter]:
#                    if word[position] != letter:
#                        removed = True
#            if removed == True:
#                tmp.remove(word)

    print(len(tmp))
    return tmp

if __name__ == "__main__":
    main()
