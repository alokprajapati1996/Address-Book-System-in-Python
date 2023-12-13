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


class AddressBookMain:

    def __init__(self, book_name):
        self.cont_person_dict = {}
        self.book_name = book_name

    def add_contact(self, contact_obj):
        """
        Description : This method made for add information of person.
        parameter : None
        return : None

        """

        self.cont_person_dict.update({contact_obj.first_name: contact_obj})


def main():
    """
    Description : This function made for access information of contact.
    parameter : None
    return : None

    """
    print("Welcome to Address Book Program in AddressBookMain class on START Master Branch")
    book_name = input("Enter book name: ")
    add_book_obj = AddressBookMain(book_name)

    print("0.exit : \n 1.Add person details: ")

    while True:
        your_choice = int(input("Enter your choice: "))
        match your_choice:
            case 1:
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                address = input("Enter address : ")
                city = input("Enter city name: ")
                state = input("Enter state name: ")
                zip_code = int(input("Enter zip code  name: "))
                phone_no = input("Enter mobile no.: ")
                email_id = input("Enter email id: ")
                contact_obj = Contact(first_name, last_name, address, city, state, zip_code, phone_no, email_id)
                add_book_obj.add_contact(contact_obj)
            case 0:
                break


if __name__ == '__main__':
    main()  # function call
