import tkinter as tk

"""
def calculateELO(*args):
    try:
        playerTR = (10.0**(float(playerELO.get())/400.0))
        opponentTR = (10.0**(float(opponentELO.get())/400.0))
        print(playerTR)
        playerES = (playerTR/(playerTR+opponentTR))
        opponentES = (opponentTR/(playerTR+opponentTR))
        print(playerES)
        print(opponentES)
        winELO = (float(playerELO.get()) + float(kFactor.get()) * (1.0 - playerES))
        loseELO = (float(playerELO.get()) + float(kFactor.get()) * (0.0 - playerES))
        winELO = round(winELO,2)
        loseELO = round(loseELO,2)
        print(winELO)
        print(loseELO)

        winELODisplay.set(winELO)
        loseELODisplay.set(loseELO)
        #value = float(playerELO.get())
        #meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

def clearFields(*args):
    winELODisplay.set('')
    loseELODisplay.set('')
    opponent_elo_entry.delete(0, END)
    player_elo_entry.delete(0, END)
    kFactor_entry.delete(0, END)
"""



root = tk.Tk()

class MainMenu:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quickCalcButton = tk.Button(self.frame, text = 'Quick Calculator', width = 25, command = self.new_quick_calc_window)
        self.quickCalcButton.pack()
        self.frame.pack()

    def new_quick_calc_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = QuickCalculator(self.newWindow)

class QuickCalculator:

    playerELO = tk.StringVar()
    opponentELO = tk.StringVar()
    winELO = float()
    loseELO = float()
    winELODisplay = tk.StringVar()
    loseELODisplay = tk.StringVar()
    playerTR = tk.StringVar()
    opponentTR = tk.StringVar()
    playerES = tk.StringVar()
    opponentES = tk.StringVar()
    kFactor = tk.StringVar()

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.setupButtons()

    def setupButtons(self):
        self.calculateButton = tk.Button(self.master, text = "Calculate")
        self.clearButton = tk.Button(self.master, text = "Clear")
        self.calculateButton.pack()
        self.clearButton.pack()
        self.frame.pack()

def main():
    root.title("ELO Calculator")
    app = MainMenu(root)
    root.mainloop()

main()
"""

player_elo_entry = ttk.Entry(mainframe, width=7, textvariable=playerELO)
player_elo_entry.grid(column=2, row=1, sticky=(W))

opponent_elo_entry = ttk.Entry(mainframe, width=7, textvariable=opponentELO)
opponent_elo_entry.grid(column=2, row=2, sticky=(W))

kFactor_entry = ttk.Entry(mainframe, width=7, textvariable=kFactor)
kFactor_entry.grid(column=2, row=3, sticky=(W))

ttk.Label(mainframe, textvariable=winELODisplay).grid(column=2, row=4, sticky=(W, E))
ttk.Label(mainframe, textvariable=loseELODisplay).grid(column=2, row=5, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculateELO).grid(column=4, row=1, sticky=E)
ttk.Button(mainframe, text="Clear", command=clearFields).grid(column=4, row=2, sticky=E)

ttk.Label(mainframe, text="Player ELO").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Opponent ELO").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="K Factor").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="ELO on win").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="ELO on loss").grid(column=1, row=5, sticky=W)
for child in mainframe.winfo_children(): child.grid_configure(padx=3, pady=3)


"""



"""
mainframe = ttk.Frame(root, padding="2 2 2 2")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
"""

"""
player_elo_entry.focus()
root.bind('<Return>', calculateELO)
"""