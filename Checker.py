import selenium
from selenium import webdriver
# get the chromedriver from my mac's bin
browser = webdriver.Chrome('/usr/local/bin/chromedriver')
# take the names you want to check from
# names.txt, and it will output which ones
# are avilable to available.txt and all
# unavailable to not_available.txt
names = open('names.txt', 'r')
available = open('available.txt', 'w')
not_available = open('not_available.txt', 'w')

def checkthatshit(string) :
    # check the grailed URL for the word
    # dont even need time.sleep, page doesnt need
    # to load for a 404 redirect.
    browser.get('https://www.grailed.com/' + string)
    # if its 404 (unmade URL link) then write to the text file
    if (browser.current_url == 'https://www.grailed.com/404') :
        string.strip()
        available.write(string)
    elif not (browser.current_url == 'https://www.grailed.com/404') :
        string.strip()  
        not_available.write(string)
        
        
# check the list
for line in names :
    checkthatshit(line)

# close the files
names.close()
available.close()
not_available.close()
print("Checker finished.")
