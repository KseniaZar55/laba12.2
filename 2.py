import tkinter as tk

class IceCreamStand:
    def __init__(self, master, flavors):
        self.master = master
        self.flavors = flavors
        self.master.title("Ice Cream Stand")

        self.label = tk.Label(master, text="Доступные вкусы мороженого:")
        self.label.pack()

        for flavor in self.flavors:
            flavor_label = tk.Label(master, text=flavor)
            flavor_label.pack()

def main():
    flavors = ["Ваниль", "Шоколад", "Клубника", "Вишня"]

    root = tk.Tk()
    app = IceCreamStand(root, flavors)
    root.mainloop()

if __name__ == "__main__":
    main()
