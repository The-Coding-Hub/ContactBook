# Program Topic: Contact Book using Python and MongoDB

# Importing Required Module

import pymongo
from datetime import datetime
from fpdf import FPDF

# PyMongo Configuration

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ContactBook"]
collection = db["Contacts"]


# Making Required Functions

def throw_error(error):
    """ Function to handle and print the error """

    print(f"An error occurred which is printed below:\n{error}")


def add(name, contact_number, date_time):
    """ Function to add a Contact into the Book """

    try:
        record = {
            "todo": "todo",
            "name": name,
            "contact_number": contact_number,
            date_time: date_time
        }
        collection.insert_one(record)
        print("Contact Number has been added successfully to the Book.")
    except Exception as error:
        throw_error(error)


def view():
    """ Function to view all the Contacts """

    try:
        contacts = collection.find(
            {
                "todo": "todo"
            },
            {
                "_id": 0,
                "name": 1,
                "contact_number": 1,
                "date_time": 1
            }
        )
        print("All Contacts are below:")
        for contact in contacts:
            c = str(contact)
            print(c)
    except Exception as error:
        throw_error(error)


def update(old_name, new_name, new_number):
    """ Function to update a Contact """

    try:
        old = {
            "name": old_name
        }
        new = {
            "$set": {
                "name": new_name,
                "contact_number": new_number
            }
        }
        collection.update_one(old, new)
        print("Contact has been updated successfully.")
    except Exception as error:
        throw_error(error)


def delete(name):
    """ Function to Delete a Contact """

    try:
        to_delete = {
            "name": name
        }
        collection.delete_one(to_delete)
        print("Contact has been deleted successfully.")
    except Exception as error:
        throw_error(error)


def getPDF():
    """ Function to return a PDF File all the Contacts """

    try:
        contacts = collection.find(
            {
                "todo": "todo"
            },
            {
                "_id": 0,
                "name": 1,
                "contact_number": 1,
                "date_time": 1
            }
        )
        text = "ALL CONTACTS ARE BELOW:\n"
        for contact in contacts:
            text += (str(contact) + "\n")
        with open("Contacts.txt", "w") as file:
            file.write(text)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=16)
        f = open("Contacts.txt", "r")
        for t in f:
            pdf.cell(200, 10, txt=t, ln=1, align='L')
        pdf.output("Contacts.pdf")
        print("Your PDF and TXT")
    except Exception as error:
        throw_error(error)


if __name__ == '__main__':
    while True:
        task = int(
            input("Enter the task which you want to perform:\n1. Add a Contact\n2. View all Contacts\n3. Update a "
                  "Contact\n4. Delete a Contact\n5. Get PDF of all Contacts\n6. Exit Application\n"))
        if task == 1:
            name = input("Enter your name: ")
            contact_number = int(input("Enter your Contact Number: "))
            date_time = datetime.now().strftime("%d%B, %Y%H:%M\%p")
            add(name, contact_number, date_time)
        elif task == 2:
            view()
        elif task == 3:
            old_name = input("Enter the name of the person whose contact you want to update: ")
            new_name = input("Enter new name for the Contact: ")
            new_number = input("Enter new number for the Contact: ")
            update(old_name, new_name, new_number)
        elif task == 4:
            name = input("Enter the name of the person whose contact you want to delete: ")
            delete(name)
        elif task == 5:
            getPDF()
        elif task == 6:
            break
        else:
            print("Task Not Found!")
