def r1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors

        def display_flavors(self):
            print("Доступные вкусы мороженого:")
            for flavor in self.flavors:
                print("- " + flavor)

    ice_cream_stand = IceCreamStand("Мороженка", "Кафе - мороженое", ["ваниль", "шоколад", "клубника"])

    ice_cream_stand.display_flavors()



def r2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors, location, working_hours):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
            self.location = location
            self.working_hours = working_hours

        def display_flavors(self):
            print("Доступные вкусы мороженого:")
            for flavor in self.flavors:
                print("- " + flavor)

        def add_flavor(self, new_flavor):
            self.flavors.append(new_flavor)
            print(f"{new_flavor} добавлен успешно.")

        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f"{flavor} успешно удален")
            else:
                print(f"{flavor} вкус не найден в списке.")

        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f"{flavor} - вкус есть в наличии")
            else:
                print(f"{flavor} - вкуса нет в наличии")

        def serve_popsicle_ice_cream(self):
            print("Подача на палочке")

        def serve_soft_ice_cream(self):
            print("Подача в рожке")

    ice_cream_stand = IceCreamStand("Мороженка", "мороженое", ["ваниль", "шоколад", "клубника"], "торговый центр: Радуга",
                                    "10:00 - 20:00")

    ice_cream_stand.display_flavors()

    ice_cream_stand.add_flavor("вишня")
    ice_cream_stand.display_flavors()

    ice_cream_stand.remove_flavor("клубника")
    ice_cream_stand.display_flavors()

    ice_cream_stand.check_flavor("ваниль")

    ice_cream_stand.serve_popsicle_ice_cream()
    ice_cream_stand.serve_soft_ice_cream()


r2()