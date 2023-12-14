"""

@Author: Alok kumar

@Date: 13-12-23 2:38:30

@Last Modified by: Alok kumar

@Last Modified time: 13-12-2023 5:30:30

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

    def update_personal_details(self):
        """
        Description : This function made for edit all information of contact.
        parameter : None
        return : None

        """
        while True:
            print("""Enter what you want to edit...
              1.for first name :
              2.for last name:
              3.for address : 
              4.for city : 
              5.state : 
              6.for zip: 
              7.mobile no.:
              8.email :
              9.exit :
        """)
            edit_choice = int(input("enter your choice : "))
            match edit_choice:
                case 1:
                    name = input("enter your name : ")
                    self.first_name = name
                case 2:
                    l_name = input("enter last name : ")
                    self.last_name = l_name
                case 3:
                    che_address = input("enter address name : ")
                    self.address = che_address
                case 4:
                    che_city = input("enter city name : ")
                    self.city = che_city
                case 5:
                    che_state = input("enter state name : ")
                    self.state = che_state
                case 6:
                    new_zip = input("enter zip code. : ")
                    self.zip_code = new_zip
                case 7:
                    new_mobile = input("enter mobile no. : ")
                    self.phone_no = new_mobile
                case 8:
                    new_mail = input("enter new mail : ")
                    self.email_id = new_mail
                case 9:
                    break

    def display_person_details(self):
        """
        Description : This function made for print person information of contact.
        parameter : None
        return : None

        """
        print(f"Name: {self.first_name} Last Name : {self.last_name}")
        print(f"Address: {self.address} city : {self.city}")
        print(f"State: {self.state} Last Zip_code : {self.zip_code}")
        print(f"Mobile N0.: {self.phone_no} email id : {self.email_id}")


class AddressBookMain:

    def __init__(self, book_name):
        self.cont_person_dict = {}
        self.book_name = book_name

    def delete_contact(self, name):
        contact_obj: Contact = self.cont_person_dict.get(name)
        if contact_obj:
            self.cont_person_dict.pop(name)
        else:
            print("contact is not found !!")

    def add_contact(self, contact_obj):
        """
        Description : This method made for add information of person.
        parameter : None
        return : None

        """

        self.cont_person_dict.update({contact_obj.first_name: contact_obj})

    def edit_person_details(self):
        """
        Description : This function made for check person availability ofter that call  contact class function.
        parameter : None
        return : None

        """
        name = input("Enter your name : ")
        contact_obj: Contact = self.cont_person_dict.get(name)
        if contact_obj:
            print(contact_obj.zip_code)
            contact_obj.update_personal_details()
        else:
            print("contact is not found!!")

    def display_all_contact_details(self):
        """
        Description : This function made for display information of contact.
        parameter : None
        return : None

        """
        for key, value in self.cont_person_dict.items():
            value.display_person_details()


def main():
    """
    Description : This function made for access information of contact.
    parameter : None
    return : None

    """
    print("Welcome to Address Book Program in AddressBookMain class on START Master Branch")
    book_name = input("Enter book name: ")
    add_book_obj = AddressBookMain(book_name)

    while True:
        print("0.exit : \n 1.Add person details: \n 2.edit person details : \n 3.display all details : \n "
              "4.Delete for person details :")
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
            case 2:
                add_book_obj.edit_person_details()
            case 3:
                add_book_obj.display_all_contact_details()
            case 4:
                name = input("Enter name you want to delete :")
                add_book_obj.delete_contact(name)

            case 0:
                break


if __name__ == '__main__':
    main()  # function call
