class Contact:
    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Nome deve ser um string")
        self._name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not isinstance(value, int):
            raise TypeError("Phone dev ser do tipo inteiro")
        self._phone = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Email deve ser uma string")
        self._email = value


class ContactBook:
    def __init__(self):
        self.__contacts: list[Contact] = []

    @property
    def contacts(self):
        return self.__contacts

    def add_contact(self, contact):
        if not isinstance(contact, Contact):
            raise TypeError("Contato deve ser do tipo Contato")
        self.__contacts.append(contact)

    def list_contact(self):
        for i in self.__contacts:
            print(f"Nome: {i.name} - Telefone: {i.phone} - Email: {i.email}")

    def get_contact(self, value):
        for contact in self.__contacts:
            if contact.name == value:
                return contact

    def remove_contact(self, value):
        self.__contacts.remove(value)
