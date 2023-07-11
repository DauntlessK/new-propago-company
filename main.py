# Propago web scraper company setup
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tkinter import *
import time

window = Tk()
driver = webdriver.Chrome()
def login(t1, t2):
    driver.get("https://admin.mypropago.com")
    time.sleep(5)
    try:
        username_element = driver.find_element(By.ID, "txtUserName")
        username_element.send_keys(t1.get())
    except:
        print("Failed to find username. Did the site load correctly?")
    pw_element = driver.find_element(By.ID, "txtPassword")
    pw_element.send_keys(t2.get())
    pw_element.send_keys(Keys.RETURN)
    time.sleep(5)
    try:
        username_element2 =  driver.find_element(By.ID, "txtUserName")
    except:
        window.destroy()
    else:
        messagebox.showerror(title="Login Error", message="Username/Password is incorrect")


def navigate_to_portals():
    driver.get("https://admin.mypropago.com/site/customerlist.aspx#last-search")

def startup():
    window.title("Propago Login")
    window.geometry("500x200")

    l1 = Label(window, text="Username:", font=(14))
    l2 = Label(window, text="Password:", font=(14))
    l1.grid(row=0, column=0, padx=5, pady=5)
    l2.grid(row=1, column=0, padx=5, pady=5)

    username = StringVar()
    password = StringVar()

    t1 = Entry(window, textvariable=username, font=(14))
    t2 = Entry(window, textvariable=password, font=(14), show="*")

    t1.grid(row=0, column=1)
    t2.grid(row=1, column=1)

    b1 = Button(window, command= lambda: login(t1, t2), text="Login", font=(14))
    b1.grid(row=2, column =1, sticky=W)

    window.mainloop()

def get_existing_company_name():
    companynamewindow = Tk()
    companynamewindow.title("Existing Company Name")
    companynamewindow.geometry("500x200")

    companyName = StringVar()
    l3 = Label(companynamewindow, text="Company Name:", font=(14))
    t3 = Entry(companynamewindow, textvariable=companyName, font=(14))

    l3.grid(row=0, column=0)
    t3.grid(row=0, column=1)

    b2 = Button(companynamewindow, command= lambda: company_select(t3))

def company_select(company):
    companyfield = driver.find_element(By.ID, "txtCompanyName")
    companyfield.send_keys(company)
    companyfield.send_keys(Keys.RETURN)
    time.sleep(5)
    try:
        driver.find_element(By.LINK_TEXT, company)
    except:
        messagebox.showerror(title="Company Error", message="The company you typed was not found.")
    else:
        driver.find_element(By.LINK_TEXT, company).click()

def get_new_customer_info():
        print("TO DO - new company info dialog")
def get_customer():
    status = messagebox.askyesno(title="Customer Prompt", message="Is this a new customer portal?")
    if status == True:
        get_new_customer_info()
    else:
        get_existing_company_name()

startup()
navigate_to_portals()
get_customer()
time.sleep(5)