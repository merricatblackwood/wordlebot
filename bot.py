from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint

def getShadowRoot(host):
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", host)
    return shadow_root

driver = webdriver.Safari()
driver.implicitly_wait(10)
driver.get("https://www.powerlanguage.co.uk/wordle/")

game_app = driver.find_element(By.TAG_NAME, "game-app")
game_app_root = getShadowRoot(game_app)

rows = game_app_root.find_elements(By.TAG_NAME, 'game-row')

def main():
    closeModal()
    words = []
    with open("words") as w:
        words = w.readlines()
    
    #TODO: better first guess algorithm
    first_guess = words[randint(0, len(words))]
    populateRow(0, first_guess)

def closeModal():
    game_modal = game_app_root.find_element(By.TAG_NAME, 'game-modal')
    game_modal_root = getShadowRoot(game_modal)
    driver.execute_script("return arguments[0].querySelector('.close-icon').click()", game_modal_root)

def populateRow(row, guess):
    rows[row].send_keys(guess)
    rows[row].send_keys(Keys.ENTER)

    
if __name__ == "__main__":
    main()
