import tkinter as tk

root = tk.Tk()

class MainMenu:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.grid(column=0, row=0)
        tk.Button(self.frame, text = 'Quick Calculator', width = 25, command = self.new_quick_calc_window).grid(column=0, row=0)
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
        self.frame.grid(column=0, row=0, sticky=("N", "S", "E", "W"))
        self.setupButtons()
        self.setupDataEntryAndLabels()
        for child in self.master.winfo_children(): child.grid_configure(padx=1, pady=1)

    def calculateELO(self):
        try:
            self.playerTR = (10.0**(float(self.playerELO.get())/400.0))
            self.opponentTR = (10.0**(float(self.opponentELO.get())/400.0))
            print(self.playerTR)
            self.playerES = (self.playerTR/(self.playerTR+self.opponentTR))
            self.opponentES = (self.opponentTR/(self.playerTR+self.opponentTR))
            print(self.playerES)
            print(self.opponentES)
            self.winELO = (float(self.playerELO.get()) + float(self.kFactor.get()) * (1.0 - self.playerES))
            self.loseELO = (float(self.playerELO.get()) + float(self.kFactor.get()) * (0.0 - self.playerES))
            self.winELO = round(self.winELO,2)
            self.loseELO = round(self.loseELO,2)
            print(self.winELO)
            print(self.loseELO)

            self.winELODisplay.set(self.winELO)
            self.loseELODisplay.set(self.loseELO)
        except ValueError:
            pass

    def clearFields(self):
        self.winELODisplay.set('')
        self.loseELODisplay.set('')
        self.opponent_elo_entry.delete(0, tk.END)
        self.player_elo_entry.delete(0, tk.END)
        self.kFactor_entry.delete(0, tk.END)

    def setupButtons(self):
        tk.Button(self.master, text = "Calculate", command=self.calculateELO).grid(column=4, row=1, sticky="E")
        tk.Button(self.master, text = "Clear", command=self.clearFields).grid(column=4, row=2, sticky="E")

    def setupDataEntryAndLabels(self):
        tk.Label(self.master, text="Player ELO").grid(column=1, row=1, sticky="W")
        tk.Label(self.master, text="Opponent ELO").grid(column=1, row=2, sticky="W")
        tk.Label(self.master, text="K Factor").grid(column=1, row=3, sticky="W")
        tk.Label(self.master, text="ELO on win").grid(column=1, row=4, sticky="W")
        tk.Label(self.master, text="ELO on loss").grid(column=1, row=5, sticky="W")
        tk.Label(self.master, textvariable=self.winELODisplay).grid(column=2, row=4, sticky=("W", "E"))
        tk.Label(self.master, textvariable=self.loseELODisplay).grid(column=2, row=5, sticky=("W", "E"))
        self.player_elo_entry = tk.Entry(self.master, width=7, textvariable=self.playerELO)
        self.player_elo_entry.grid(column=2, row=1, sticky="W")
        self.opponent_elo_entry = tk.Entry(self.master, width=7, textvariable=self.opponentELO)
        self.opponent_elo_entry.grid(column=2, row=2, sticky="W")
        self.kFactor_entry = tk.Entry(self.master, width=7, textvariable=self.kFactor)
        self.kFactor_entry.grid(column=2, row=3, sticky="W")
        

def main():
    root.title("ELO Calculator")
    app = MainMenu(root)
    root.mainloop()

main()