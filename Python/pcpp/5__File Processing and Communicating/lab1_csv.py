import csv


class PhoneContact:

    def __init__(self, name, phone) -> None:
        self.name = name
        self.phone = phone

    def __repr__(self) -> str:
        return f'{self.name}  -- {self.phone}'
    

class Phone:

    def __init__(self) -> None:
        self.contacts = [] 

    def load_contacts_from_csv(self, file):

        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.contacts.append(PhoneContact(row['Name'], row['Phone'])) 
                        
    def search_contacts(self, search):

        results = [ x for x in self.contacts if x.name.upper().startswith(search.upper()) ]

        if len(results) :
            for contact in results:
                print(contact)
        else :
            print("No contacts found")


# -------- test 
x = Phone()
x.load_contacts_from_csv('.\\5__File Processing and Communicating\\contacts.csv')
x.search_contacts('mother')

