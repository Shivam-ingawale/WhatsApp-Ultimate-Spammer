import time
from random import randint

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as Condition
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# name -> Name of the Individual or Group Chat Account
# message -> spam message
# spam_number -> number of spam messages
def spam_message(message, name, spam_number):
    if message is not None and name is not None:
        try:
            # Selecting Individual or Group Chat in the whatsapp
            x_arg = '//span[contains(@title,\'' + name + '\')]'
            group_title = wait.until(Condition.presence_of_element_located((By.XPATH, x_arg)))
            group_title.click()

            # Clicking on the input box in Individual or Group Chat in the chrome (whatsapp.com)
            inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
            input_box = wait.until(Condition.presence_of_element_located((By.XPATH, inp_xpath)))

            # Spamming the message in Individual or Group Chat
            for i in range(spam_number):
                input_box.send_keys(message + Keys.ENTER)
                time.sleep(1)
        except:
            print("Something went wrong")
    return


# name -> Name of the Individual or Group Chat Account
# emoji_name -> name of emoji
# spam_number -> number of spam messages
def spam_specific_emoji(emoji_name, name, spam_number):
    if name is not None:

        # Selecting Individual or Group Chat in the whatsapp
        x_arg = '//span[contains(@title,\'' + name + '\')]'
        group_title = wait.until(Condition.presence_of_element_located((By.XPATH, x_arg)))
        group_title.click()

        # For spamming "spam_number" of times
        for i in range(0, spam_number):

            # Opening emoji panel
            data_icon = "smiley"
            x_arg = '//span[contains(@data-icon,\'' + data_icon + '\')]'
            group_title = wait.until(Condition.presence_of_element_located((By.XPATH, x_arg)))
            group_title.click()
            try:
                # Searching and clicking for emoji in emoji panel
                inp_xpath = '//input[@class="_3K9QW copyable-text selectable-text"]'
                input_box = wait.until(Condition.presence_of_element_located((By.XPATH, inp_xpath)))
                input_box.send_keys(emoji_name + Keys.ENTER)
            except:
                print("no emoji found for " + emoji_name)

            # Sending the emoji in Individual or Group Chat
            inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
            input_box = wait.until(Condition.presence_of_element_located((By.XPATH, inp_xpath)))
            input_box.send_keys(Keys.ENTER)
            time.sleep(1)
    return


# name -> Name of the Individual or Group Chat Account
# spam_number -> number of spam messages
def spam_random_emojis(name, spam_number):
    if name is not None:

        # Selecting Individual or Group Chat in the whatsapp
        x_arg = '//span[contains(@title,\'' + name + '\')]'
        group_title = wait.until(Condition.presence_of_element_located((By.XPATH, x_arg)))
        group_title.click()
        time.sleep(2)

        # For spamming emojis spam_number of times
        i = 0
        while i <= spam_number:
            try:

                # Opening Emoji panel
                data_icon = "smiley"
                x_arg = '//span[contains(@data-icon,\'' + data_icon + '\')]'
                group_title = wait.until(Condition.presence_of_element_located((By.XPATH, x_arg)))
                group_title.click()

                # Selecting and clicking random Emoji from panel
                j = randint(0, 7)
                emoji_xpath = '//span[@data-emoji-index=\"' + str(j) + '\"]'
                all_elements = driver.find_elements(By.XPATH, emoji_xpath)
                k = randint(0, len(all_elements))
                all_elements[k].click()

                # Sending the emoji in Individual or Group Chat
                inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
                input_box = wait.until(Condition.presence_of_element_located((By.XPATH, inp_xpath)))
                input_box.send_keys(Keys.ENTER)
                time.sleep(1)

                i = i + 1
            except:
                print("error in random emoji")
    return


if __name__ == '__main__':
    # Load the chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # Open WhatsApp URL in chrome browser
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 600)
    time.sleep(5)

    contact_name = "Shivam Self"
    message_string = "hello there!"
    spam_count = 5

    # Spamming message
    spam_message(message=message_string, name=contact_name, spam_number=spam_count)

    # For spamming specific emoji
    spam_specific_emoji(emoji_name="smile", name=contact_name, spam_number=spam_count)

    # For spamming random emoji
    spam_random_emojis(name=contact_name, spam_number=spam_count)

    # Close Chrome browser
    # driver.quit()
