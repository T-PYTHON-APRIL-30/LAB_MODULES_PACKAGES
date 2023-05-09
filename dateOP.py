"""# LAB_MODULES_PACKAGES

## Create a new module and name it "dateOP.py" ,  dateOP has the following:
- A function that when called prints the current date.

## Create a new module "main.py" , and do the following:
- import dateOP
- call the function that print the current date

### hint : You should import the date class from the datetime module.
"""
import datetime as date

def current_date():
    print(date.datetime.now())

