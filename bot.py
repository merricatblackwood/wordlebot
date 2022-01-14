from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint


driver = webdriver.Safari()
driver.implicitly_wait(10)
driver.get("https://www.powerlanguage.co.uk/wordle/")

def main():
    closeModal()
    words = []
    with open("words") as w:
        words = w.readlines()
    
    #TODO: better first guess algorithm
    first_guess = words[randint(0, len(words))]
    print(first_guess)

     

def closeModal():
    game_app = driver.find_element(By.TAG_NAME, "game-app")
    game_app_root = getShadowRoot(game_app)
    game_theme_manager = game_app_root.find_element(By.TAG_NAME, "game-theme-manager")
    game_modal = game_app_root.find_element(By.TAG_NAME, 'game-modal')
    game_modal_root = getShadowRoot(game_modal)
    driver.execute_script("return arguments[0].querySelector('.close-icon').click()", game_modal_root)

def getShadowRoot(host):
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", host)
    return shadow_root
    
if __name__ == "__main__":
    main()
