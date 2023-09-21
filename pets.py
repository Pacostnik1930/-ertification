class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.commands = []
        
    def add_command(self, command):
        self.commands.append(command)
        
    def classify_species(self):
        # Ваша логика определения класса животного
        pass
    
    def show_commands(self):
        for command in self.commands:
            print(command)
            
    def teach_command(self, new_command):
        self.commands.append(new_command)
        print("Животное успешно обучено новой команде.")
      
def main_menu():
    print("1. Завести новое животное")
    print("2. Определить животное в правильный класс")
    print("3. Увидеть список команд, которые выполняет животное")
    print("4. Обучить животное новым командам")
    print("5. Выйти")

animals = []

while True:
    main_menu()
    choice = input("Выберите пункт меню: ")

    if choice == "1":
        name = input("Введите имя животного: ")
        species = input("Введите вид животного: ")
        animal = Animal(name, species)
        animals.append(animal)
        print(f"Животное {name} успешно зарегистрировано!")

    elif choice == "2":
        name = input("Введите имя животного: ")
        for animal in animals:
            if animal.name == name:
                animal.classify_species()
                break
        else:
            print("Животное с таким именем не найдено.")

    elif choice == "3":
        name = input("Введите имя животного: ")
        for animal in animals:
            if animal.name == name:
                animal.show_commands()
                break
        else:
            print("Животное с таким именем не найдено.")

    elif choice == "4":
        name = input("Введите имя животного: ")
        new_command = input("Введите новую команду: ")
        for animal in animals:
            if animal.name == name:
                animal.teach_command(new_command)
                break
        else:
            print("Животное с таким именем не найдено.")

    elif choice == "5":
        print("Выход из программы...")
        break

    else:
        print("Некорректный выбор. Попробуйте еще раз.")
