from collections import UserDict
import re

# Реалізація класу Field
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

# Реалізація класу Name
class Name(Field):
    def __init__(self, name):
        if self.name_check(name):  
            super().__init__(name)
        else:
            raise ValueError(f"Невірний формат імені: {name}")
    
    def name_check(self,name):
        pattern = r"^[A-Za-z]+$"
        match = re.search(pattern, name)    # Перевірка формату імені
        if match:
            return True

# Реалізація класу Phone
class Phone(Field):
    def __init__(self, phone):
        if self.phone_check(phone):  
            super().__init__(phone)
        else:
            raise ValueError(f"Невірний формат телефону: {phone}")
    
    def phone_check(self,phone):
        pattern = r"^[0-9]{10}$"
        match = re.search(pattern, phone)    # Перевірка формату телефону
        if match:
            return True

# Реалізація класу Record
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, entered_phone):
        self.phones = [phone for phone in self.phones if phone.value != entered_phone]

    def edit_phone(self, old_phone, new_phone):
        found = False
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = Phone(new_phone).value
                found = True
                break 

        if not found:
            raise ValueError(f"Телефон відсутній: {old_phone}")
            
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# Реалізація класу AddressBook
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, record):
        self.data.pop(record)
         
    def __str__(self):
        if not self.data:
            return "Address Book is empty"
        
        return "\n".join(str(record) for record in self.data.values())

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
    
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")

john_record.add_phone("0504567890")
john.edit_phone("5555555555", "2222222222")
print(book)