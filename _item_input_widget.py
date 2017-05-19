import tkinter as tk

class Item_input_widget(tk.Frame):
    ENTRYWIDTH = 5
    LABELSPACES = 2
    LABELSTRING = 'PB PS TS TP TC OS OP OC'
    ENTRYSTRING = 'PriceBuy PriceSell ' \
        'townStock townProduction townConsumption ' \
        'ownStock ownProduction ownConsumption'
    INDEXCOUNT = len(LABELSTRING.split())

    def __init__(self, parent, name):
        super(self.__class__, self).__init__(parent)
        self.name = name
        self.nameLabel = tk.Label(self, text = self.name).pack(side = 'left')

        self.labels = dict()
        for label in self.LABELSTRING.split():
            string = ' ' * self.LABELSPACES + label + ':'
            self.labels[label] = tk.Label(self, text = string)

        self.entries = dict()
        for entry in self.ENTRYSTRING.split():
            self.entries[entry] = tk.Entry(self, width = self.ENTRYWIDTH)

        for i in range(self.INDEXCOUNT):
            label = self.LABELSTRING.split()[i]
            entry = self.ENTRYSTRING.split()[i]
            self.labels[label].pack(side = 'left')
            self.entries[entry].pack(side = 'left')

    def getValues(self):
        self.values = dict()
        for entry in self.ENTRYSTRING.split():
            self.values[entry] = self.entries[entry].get()
        return self.values

    def clearEntries(self):
        for entry in self.ENTRYSTRING.split():
            self.entries[entry].delete(0,tk.END)

    def validateEntry(self):
        for entry in self.entries:
            value = entry.get()
            # good idea
            # ??LOGIC??




if __name__ == '__main__':
    app = tk.Tk()
    item = Item_input_widget(app, 'asdfdsdf - ')
    item.pack()
    def iprint(_item= item):
        print(item.getValues())

    delete = tk.Button(app, text='del', command = item.clearEntries).pack()
    prnt = tk.Button(app, text = 'print', command = iprint).pack()
    app.mainloop()