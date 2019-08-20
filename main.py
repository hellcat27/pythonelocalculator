from tkinter import *
from tkinter import ttk

def calculateELO(*args):
    try:
        value = float(playerELO.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("ELO Calculator")

mainframe = ttk.Frame(root, padding="2 2 2 2")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

playerELO = StringVar()
opponentELO = StringVar()
meters = StringVar()
playerTR = StringVar()
opponentTR = StringVar()
playerES = StringVar()
opponentES = StringVar()
kFactor = StringVar()


player_elo_entry = ttk.Entry(mainframe, width=7, textvariable=playerELO)
player_elo_entry.grid(column=2, row=1, sticky=(W))

opponent_elo_entry = ttk.Entry(mainframe, width=7, textvariable=opponentELO)
opponent_elo_entry.grid(column=2, row=2, sticky=(W))

kFactor_entry = ttk.Entry(mainframe, width=7, textvariable=kFactor)
kFactor_entry.grid(column=2, row=3, sticky=(W))

ttk.Label(mainframe, textvariable=meters).grid(column=3, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculateELO).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Player ELO").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Opponent ELO").grid(column=1, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=3, pady=3)

player_elo_entry.focus()
root.bind('<Return>', calculateELO)

root.mainloop()