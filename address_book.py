"""

@Author: Alok kumar

@Date: 7-12-23 2:38:30

@Last Modified by: Alok kumar

@Last Modified time: 7-12-2023 3:30:30

@Title : Implementation of Address Book System

"""


class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_no, email_id):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_no = phone_no
        self.email_id = email_id


def main():
    """
    Description : This function made for access information of contact.
    parameter : None
    return : None

    """
    first_name = input("Enter first name: ")
    last_name = input("Enter first name: ")
    address = input("Enter first name: ")
    city = input("Enter first name: ")
    state = input("Enter first name: ")
    zip_code = input("Enter first name: ")
    phone_no = input("Enter first name: ")
    email_id = input("Enter first name: ")
    contact = Contact(first_name, last_name, address, city, state, zip_code, phone_no, email_id)


if __name__ == '__main__':
    main()  # function call
