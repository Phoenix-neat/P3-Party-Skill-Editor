from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Party Skill Editor")

# Closes the GUI and runs the code in Party Skill Editor.py
def test():
    root.destroy()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Creates input boxes that take in relevant data
yukLv = IntVar()
yuk_entry = ttk.Entry(mainframe, width=4, textvariable=yukLv)
yuk_entry.grid(column=4, row=2, sticky=E)

junLv = IntVar()
jun_entry = ttk.Entry(mainframe, width=4, textvariable=junLv)
jun_entry.grid(column=4, row=3, sticky=E)

akiLv = IntVar()
aki_entry = ttk.Entry(mainframe, width=4, textvariable=akiLv)
aki_entry.grid(column=4, row=4, sticky=E)

mitLv = IntVar()
mit_entry = ttk.Entry(mainframe, width=4, textvariable=mitLv)
mit_entry.grid(column=4, row=5, sticky=E)

aigLv = IntVar()
aig_entry = ttk.Entry(mainframe, width=4, textvariable=aigLv)
aig_entry.grid(column=4, row=6, sticky=E)

koroLv = IntVar()
koro_entry = ttk.Entry(mainframe, width=4, textvariable=koroLv)
koro_entry.grid(column=4, row=7, sticky=E)

kenLv = IntVar()
ken_entry = ttk.Entry(mainframe, width=4, textvariable=kenLv)
ken_entry.grid(column=4, row=8, sticky=E)

shinLv = IntVar()
shin_entry = ttk.Entry(mainframe, width=4, textvariable=shinLv)
shin_entry.grid(column=4, row=9, sticky=E)

metLv = IntVar()
met_entry = ttk.Entry(mainframe, width=4, textvariable=metLv)
met_entry.grid(column=4, row=10, sticky=E)

monthCheck = IntVar()
month_entry = ttk.Entry(mainframe, width=7, textvariable=monthCheck)
month_entry.grid(column=1, row=8, sticky=W)

dayCheck = IntVar()
day_entry = ttk.Entry(mainframe, width=7, textvariable=dayCheck)
day_entry.grid(column=1, row=10, sticky=W)

# Creates the button select for The Journey vs The Answer and New Moon vs Vanilla
gameType = StringVar()
journey = ttk.Radiobutton(mainframe, text='The Journey     ', variable=gameType, value='J').grid(column=1, row=1, sticky=W)
answer = ttk.Radiobutton(mainframe, text='The Answer', variable=gameType, value='A').grid(column=1, row=2, sticky=W)

modCheck = StringVar()
vanilla = ttk.Radiobutton(mainframe, text='Vanilla (unmodded)', variable=modCheck, value='V').grid(column=1, row=4, sticky=W)
newMoon = ttk.Radiobutton(mainframe, text='New Moon (modded)', variable=modCheck, value='M').grid(column=1, row=5, sticky=W)

# Creates the labels for the GUI
ttk.Label(mainframe, text="Party Levels").grid(column=5, row=1, sticky=W)
ttk.Label(mainframe, text="Yukari").grid(column=5, row=2, sticky=W)
ttk.Label(mainframe, text="Junpei").grid(column=5, row=3, sticky=W)
ttk.Label(mainframe, text="Akihiko").grid(column=5, row=4, sticky=W)
ttk.Label(mainframe, text="Mitsuru").grid(column=5, row=5, sticky=W)
ttk.Label(mainframe, text="Aigis").grid(column=5, row=6, sticky=W)
ttk.Label(mainframe, text="Koromaru").grid(column=5, row=7, sticky=W)
ttk.Label(mainframe, text="Ken").grid(column=5, row=8, sticky=W)
ttk.Label(mainframe, text="Shinjiro").grid(column=5, row=9, sticky=W)
ttk.Label(mainframe, text="Metis").grid(column=5, row=10, sticky=W)

ttk.Label(mainframe, text="Month #").grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, text="Day #").grid(column=1, row=9, sticky=W)
ttk.Button(mainframe, text="SSSend it", command=test).grid(column=1, row=11, sticky=W)

ttk.Label(mainframe, text="                                      Instructions").grid(column=6, row=1, sticky=W)
ttk.Label(mainframe, text="         Choose a game mode (example: The Journey and New Moon)").grid(column=6, row=2, sticky=W)
ttk.Label(mainframe, text="         Enter levels for the Party Members (0 to skip)").grid(column=6, row=3, sticky=W)
ttk.Label(mainframe, text="         Enter the date for The Journey").grid(column=6, row=4, sticky=W)
ttk.Label(mainframe, text="         pnach file will be located in this program's folder").grid(column=6, row=5, sticky=W)

root.mainloop()
