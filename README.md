# Walgreens-Scraper
Created because I was looking for a Covid-19 vaccination appointment at a Walgreens in my area, this is a simple script that uses Google Chrome to read information from the Walgreens website, and let me know when an appointment is found through email or text message notifications.

## Dependencies
This project uses Selenium in Python, and I specifically am using the Google Chrome driver for MacOS. If you would like to use my code, you will need to [install Selenium](https://selenium-python.readthedocs.io/installation.html) for your system.

## How to run:
Right now, I am simply making a call to my function in the main area of my Python file, although you could add user input if desired. If you would like to try to use this program, you can simply modify the parameters in the "watchZipCode" function call in main. I am using a yahoo email to send emails to phone numbers and emails. If you would like to use a different service, you will need to modify the sendText function.
