import tkinter as tk
from _item_input_widget import Item_input_widget as Item
from _population_input_widget import Population_input_widget as Population


class Town_input_widget(tk.Frame):
    ITEMSTRING = 'beer bricks cloth fish ' \
        'grain hemp honey iron-goods leather ' \
        'meat iron-ore pitch pottery salt skins ' \
        'spices timber whale-oil wine wool'
    def __init__(self, parent):
        super(self.__class__, self).__init__(parent)
        self.population = Population(self)
        self.items = dict()
        for item in self.ITEMSTRING.split():
            print(item)
            self.items[item] = Item(self, item)
            self.items[item].pack()
            print(self.items[item])



if __name__ == '__main__':
    app = tk.Tk()
    Town_input_widget(app)

    app.mainloop()
