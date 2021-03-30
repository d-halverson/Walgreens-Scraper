from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import smtplib

def watchZipCode(zips, number, carrier, fromEmail, fromEmailPass):
    hasBeenSeen = {}
    for zipCode in zips:
        hasBeenSeen[zipCode] = False

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.walgreens.com/findcare/vaccination/covid-19")
    btn = driver.find_element_by_css_selector('span.btn.btn__blue')
    btn.click()
    driver.get("https://www.walgreens.com/findcare/vaccination/covid-19/location-screening")
    while True:

        for zipCode in zips:
            driver.get("https://www.walgreens.com/findcare/vaccination/covid-19/location-screening")
            element = driver.find_element_by_id("inputLocation")
            element.clear()
            element.send_keys(zipCode)
            button = driver.find_element_by_css_selector("button.btn")
            button.click()

            time.sleep(0.75)
            alertElement = getAlertElement(driver)
            aptFound = alertElement.text == "Appointments available!"

            if aptFound and not hasBeenSeen[zipCode]:
                print("======================APPOINTMENT FOUND! ZIP CODE: "+zipCode+"======================")
                message = "APPOINTMENT FOUND! ZIP CODE: "+zipCode
                sendText(number, carrier, fromEmail, fromEmailPass, message)
                hasBeenSeen[zipCode] = True
            elif not aptFound:
                hasBeenSeen[zipCode] = False

            time.sleep(5)


def getAlertElement(driver):
    while True:
        try:
            alertElement = driver.find_element_by_css_selector("p.fs16")
            return alertElement
        except NoSuchElementException:
            time.sleep(0.5)


def sendText(number, carrier, fromEmail, fromEmailPass, message):
    carriers = {
        'att': '@mms.att.net',
        'tmobile': ' @tmomail.net',
        'verizon': '@vtext.com',
        'sprint': '@page.nextel.com'
    }

    to_number = number+'{}'.format(carriers[carrier])
    Subject = 'Subject: Covid Vaccine:\n\n'
    footer = '- Test'  # add test footer
    conn = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
    conn.ehlo()
    conn.login(fromEmail, fromEmailPass)
    conn.sendmail(fromEmail, to_number, Subject + message)
    conn.quit()


if __name__ == "__main__":
    zips = ["zip1", "zip2"]
    watchZipCode(zips, "<phone_number>", "<carrier>", "<from_email>",  "<from_email_password>")
