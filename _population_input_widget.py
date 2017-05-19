import tkinter as tk

class Population_input_widget(tk.Frame):
    DATEENTRYWIDTH = 10
    ENTRYWIDTH = 7
    LABELSPACES = 2
    LABELSTRING = 'DATE RI WE PO BE'
    ENTRYSTRING = 'date rich wealthy poor beggers'
    INDEXCOUNT = len(LABELSTRING.split())

    def __init__(self, parent):
        super(self.__class__, self).__init__(parent)
        self.labels = dict()
        for label in self.LABELSTRING.split():
            string = ' ' * self.LABELSPACES + label + ':'
            self.labels[label] = tk.Label(self, text = string)

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
    item = Population_input_widget(app)
    item.pack()
    def iprint(_item= item):
        print(item.getValues())

    delete = tk.Button(app, text='del', command = item.clearEntries).pack()
    prnt = tk.Button(app, text = 'print', command = iprint).pack()
    app.mainloop()