from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("The phone number must contain 10 digits")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        # Видаляємо телефон зі списку, якщо він існує
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
               
    def edit_phone(self, old_phone, new_phone):
        # Створюємо об'єкт Phone для перевірки коректності нового номера
        new_phone_obj = Phone(new_phone)
       
        # Редагування телефонів (Змінюємо існуючий телефон на новий)
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone_obj.value
                return
            
        # Якщо телефон для заміни не знайдено, виникає помилка
        raise ValueError(f"Phone {old_phone} not found")

    def find_phone(self, phone):
        # Пошук телефону у списку
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        # Формування рядка для відображення контакту
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        # Додавання нового запису до адресної книги
        self.data[record.name.value] = record

    def find(self, name):
        # Пошук запису за іменем, повертає об'єкт Record або None
        return self.data.get(name)

    def delete(self, name):
        # Видалення запису за іменем, якщо запис існує
        if name in self.data:
            del self.data[name]

    def __str__(self):
        # Повертає список усіх контактів для виводу
        if not self.data:
            # Якщо контакти відсутні, повертає рядок
            return "AddressBook is empty"
        return "\n".join(record.name.value for record in self.data.values())


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

print("After deleting record 'Jane':")
print(book)
