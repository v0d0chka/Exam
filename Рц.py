class PlayerInventory:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)

    def show_inventory(self):
        for item in self.__items:
            print(item)

inventory = PlayerInventory()

while True:
    command = input("Введите команду (add, remove, show, exit): ").lower()
    if command == "add":
        item = input("Введите название предмета: ")
        inventory.add_item(item)
    elif command == "remove":
        item = input("Введите название предмета для удаления: ")
        inventory.remove_item(item)
    elif command == "show":
        inventory.show_inventory()
    elif command == "exit":
        break
    else:
        print("Неверная команда, попробуйте снова.")