from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint

def main():
    words = []
    with open("words") as w:
        words = w.readlines()
    
    #TODO: better first guess algorithm
    first_guess = words[randint(0, len(words))]
    print(first_guess)

     
    driver = webdriver.Safari()
    driver.implicitly_wait(10)
    driver.get("https://www.powerlanguage.co.uk/wordle/")


    
if __name__ == "__main__":
    main()
