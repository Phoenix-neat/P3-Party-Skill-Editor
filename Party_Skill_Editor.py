from GUI_data import *

# Creates blank list for all party members that will be used to push skills into
yukSkills = []
junSkills = []
akiSkills = []
mitSkills = []
aigSkills = []
koroSkills = []
kenSkills = []
shinSkills = []
metSkills = []

errorMessage = 0

# Python 2.7 compatibility
try:
    input = raw_input
except NameError:
    pass

# Checks for The Journey or The Answer, and then for Vanilla or Modded. Imports relevant data from files in Data
gameType = gameType.get()
modCheck = modCheck.get()
if gameType == 'J':
    if modCheck == 'V':
        from Data.Party_Unmodded import *
        from Data.Levels_Unmodded import *
        patch_print = "Unmodded, The Journey"
    elif modCheck == 'M':
        from Data.Party_Modded import *
        from Data.Levels_Modded import *
        patch_print = "New Moon, The Journey"
# Determines if Personas are evolved by checking the date inputted
    monthCheck = int(monthCheck.get())
    dayCheck = int(dayCheck.get())
    if monthCheck > 10 or monthCheck == 1 or monthCheck == 10 and dayCheck > 4:
        akihiko = akihikoEv
        ken = kenEv
    if monthCheck > 11 or monthCheck == 1 or monthCheck == 11 and dayCheck > 7:
        yukari = yukariEv
    if monthCheck > 11 or monthCheck == 1 or monthCheck == 11 and dayCheck > 17:
        mitsuru = mitsuruEv
    if monthCheck > 11 or monthCheck == 1 or monthCheck == 11 and dayCheck > 22:
        junpei = junpeiEv
    if monthCheck > 12 or monthCheck == 1 or monthCheck == 12 and dayCheck > 29:
        aigis = aigisEv
# Displays an error message for invalid dates, but still creates a cheat code
    if monthCheck in [0, 2, 3] or monthCheck > 12:
        errorMessage = 2
    if dayCheck == 0 or dayCheck > 31:
        errorMessage = 2
elif gameType == 'A':
    if modCheck == 'V':
        from Data.Party_Unmodded_A import *
        from Data.Levels_Unmodded_A import *
        patch_print = "Unmodded, The Answer"
    elif modCheck == 'M':
        from Data.Party_Modded_A import *
        from Data.Levels_Modded_A import *
        patch_print = "New Moon, The Answer"
else:
    errorMessage = 1

if errorMessage != 1:
    yukLv = int(yukLv.get())
    junLv = int(junLv.get())
    akiLv = int(akiLv.get())
    mitLv = int(mitLv.get())
    aigLv = int(aigLv.get())
    koroLv = int(koroLv.get())
    kenLv = int(kenLv.get())
    shinLv = int(shinLv.get())
    metLv = int(metLv.get())

# checks the level for each party member
    for (minLv, maxLv, skill) in yukari:
        if minLv <= yukLv < maxLv:
            yukSkills.append(skill)

    for (minLv, maxLv, skill) in junpei:
        if minLv <= junLv < maxLv:
            junSkills.append(skill)

    for (minLv, maxLv, skill) in akihiko:
        if minLv <= akiLv < maxLv:
            akiSkills.append(skill)

    for (minLv, maxLv, skill) in mitsuru:
        if minLv <= mitLv < maxLv:
            mitSkills.append(skill)

    if gameType == 'J':
        for (minLv, maxLv, skill) in aigis:
            if minLv <= aigLv < maxLv:
                aigSkills.append(skill)

    for (minLv, maxLv, skill) in koromaru:
        if minLv <= koroLv < maxLv:
            koroSkills.append(skill)

    for (minLv, maxLv, skill) in ken:
        if minLv <= kenLv < maxLv:
            kenSkills.append(skill)

    if gameType == 'J':
        for (minLv, maxLv, skill) in shinjiro:
            if minLv <= shinLv < maxLv:
                shinSkills.append(skill)
    elif gameType == 'A':
        for (minLv, maxLv, skill) in metis:
            if minLv <= metLv < maxLv:
                metSkills.append(skill)

# Creates/ overwrites the pnach file
    with open("94A82AAA_partySkills.pnach", "w") as overwrite:
        overwrite.write(f"//Persona 3 FES Party Skill Overwrite, {patch_print}")

# Writes the first (and only) eight skills to the file
    with open("94A82AAA_partySkills.pnach", "a") as pnach:
        # Yukari
        count = 0
        while count < len(yukSkills):
            if count == 0:
                pnach.write(f"\n\n//Yukari Skills (Level {yukLv})")
            pnach.write(f"\n//Persona Skill {(str(count + 1))}\npatch=1,EE,00"
                        f"{format(8601848 + (count * 2), 'x').upper()},short,0{yukSkills[count]}")
            count += 1
        # fills in the remaining skill slots with blank entries to overwrite potential duplicates/ unwanted skills
        if count != 0:
            while count < 8:
                pnach.write(f"\n//Persona Skill {(str(count + 1))}\npatch=1,EE,00"
                            f"{format(8601848 + (count * 2), 'x').upper()},short,0000")
                count += 1

        # Takes in Stats data and outputs level cheat codes
        if yukLv != 0:
            Strength = 0
            Magic = 0
            Endurance = 0
            Agility = 0
            Luck = 0
            for(Level, Str, Mag, End, Agi, Luc) in yukari_Stats:
                if yukLv >= Level:
                    Strength += Str
                    Magic += Mag
                    Endurance += End
                    Agility += Agi
                    Luck += Luc

            pnach.write(f"\n\n//Yukari Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                        f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,20834108,"
                        f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                        f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,0083410C,"
                        f"extended,000000{format(Luck, 'x').upper()}")

        # Junpei
        count = 0
        while count < len(junSkills):
            if count == 0:
                pnach.write(f"\n\n//Junpei skills (Level {junLv})")
            pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                        f"{format(8604452 + (count * 2), 'x').upper()},short,0{junSkills[count]}")
            count += 1
        if count != 0:
            while count < 8:
                pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                            f"{format(8604452 + (count * 2), 'x').upper()},short,0000")
                count += 1

        if junLv != 0:
            Strength = 0
            Magic = 0
            Endurance = 0
            Agility = 0
            Luck = 0
            for (Level, Str, Mag, End, Agi, Luc) in junpei_Stats:
                if Level <= junLv:
                    Strength += Str
                    Magic += Mag
                    Endurance += End
                    Agility += Agi
                    Luck += Luc

            pnach.write(f"\n\n//Junpei Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                        f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,20834B34,"
                        f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                        f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,00834B38,"
                        f"extended,000000{format(Luck, 'x').upper()}")

        # Akihiko
        count = 0
        while count < len(akiSkills):
            if count == 0:
                pnach.write(f"\n\n//Akihiko skills (Level {akiLv})")
            pnach.write(f"\n//Persona Skill {str(count + 1)} \npatch=1,EE,00"
                        f"{format(8606188 + (count * 2), 'x').upper()},short,0{akiSkills[count]}")
            count += 1
        if count != 0:
            while count < 8:
                pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                            f"{format(8606188 + (count * 2), 'x').upper()},short,0000")
                count += 1

        if akiLv != 0:
            Strength = 0
            Magic = 0
            Endurance = 0
            Agility = 0
            Luck = 0
            for (Level, Str, Mag, End, Agi, Luc) in akihiko_Stats:
                if Level <= akiLv:
                    Strength += Str
                    Magic += Mag
                    Endurance += End
                    Agility += Agi
                    Luck += Luc

            pnach.write(f"\n\n//Akihiko Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                        f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,208351FC,"
                        f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                        f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,00835200,"
                        f"extended,000000{format(Luck, 'x').upper()}")

        # Mitsuru
        count = 0
        while count < len(mitSkills):
            if count == 0:
                pnach.write(f"\n\n//Mitsuru skills (Level {mitLv})")
            pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                        f"{format(8603584 + (count * 2), 'x').upper()},short,0{mitSkills[count]}")
            count += 1
        if count != 0:
            while count < 8:
                pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                            f"{format(8603584 + (count * 2), 'x').upper()},short,0000")
                count += 1

        if mitLv != 0:
            Strength = 0
            Magic = 0
            Endurance = 0
            Agility = 0
            Luck = 0
            for (Level, Str, Mag, End, Agi, Luc) in mitsuru_Stats:
                if Level <= mitLv:
                    Strength += Str
                    Magic += Mag
                    Endurance += End
                    Agility += Agi
                    Luck += Luc

            pnach.write(f"\n\n//Mitsuru Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                        f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,208347D0,"
                        f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                        f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,008347D4,"
                        f"extended,000000{format(Luck, 'x').upper()}")

        # Aigis
        if gameType == 'J':
            count = 0
            while count < len(aigSkills):
                if count == 0:
                    pnach.write(f"\n\n//Aigis skills (Level {aigLv})")
                pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                            f"{format(8602716 + (count * 2), 'x').upper()},short,0{aigSkills[count]}")
                count += 1
            if count != 0:
                while count < 8:
                    pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                                f"{format(8602716 + (count * 2), 'x').upper()},short,0000")
                    count += 1

            if aigLv != 0:
                Strength = 0
                Magic = 0
                Endurance = 0
                Agility = 0
                Luck = 0
                for (Level, Str, Mag, End, Agi, Luc) in aigis_Stats:
                    if Level <= aigLv:
                        Strength += Str
                        Magic += Mag
                        Endurance += End
                        Agility += Agi
                        Luck += Luc

                pnach.write(f"\n\n//Aigis Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                            f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,2083446C,"
                            f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                            f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,00834470,"
                            f"extended,000000{format(Luck, 'x').upper()}")

        # Koromaru
        count = 0
        while count < len(koroSkills):
            if count == 0:
                pnach.write(f"\n\n//Koromaru skills (Level {koroLv})")
            pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                        f"{format(8608792 + (count * 2), 'x').upper()},short,0{koroSkills[count]}")
            count += 1
        if count != 0:
            while count < 8:
                pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                            f"{format(8608792 + (count * 2), 'x').upper()},short,0000")
                count += 1

        if koroLv != 0:
            Strength = 0
            Magic = 0
            Endurance = 0
            Agility = 0
            Luck = 0
            for (Level, Str, Mag, End, Agi, Luc) in koromaru_Stats:
                if Level <= koroLv:
                    Strength += Str
                    Magic += Mag
                    Endurance += End
                    Agility += Agi
                    Luck += Luc

            pnach.write(f"\n//Koromaru Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                        f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,20835C28,"
                        f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                        f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,00835C2C,"
                        f"extended,000000{format(Luck, 'x').upper()}")

        # Ken
        count = 0
        while count < len(kenSkills):
            if count == 0:
                pnach.write(f"\n\n//Ken skills (Level {kenLv})")
            pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                        f"{format(8607056 + (count * 2), 'x').upper()},short,0{kenSkills[count]}")
            count += 1
        if count != 0:
            while count < 8:
                pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                            f"{format(8607056 + (count * 2), 'x').upper()},short,0000")
                count += 1

        if kenLv != 0:
            Strength = 0
            Magic = 0
            Endurance = 0
            Agility = 0
            Luck = 0
            for (Level, Str, Mag, End, Agi, Luc) in ken_Stats:
                if Level <= kenLv:
                    Strength += Str
                    Magic += Mag
                    Endurance += End
                    Agility += Agi
                    Luck += Luc

            pnach.write(f"\n\n//Ken Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                        f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,20835560,"
                        f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                        f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,00835564,"
                        f"extended,000000{format(Luck, 'x').upper()}")
        
        # Shinjiro
        if gameType == 'J':
            count = 0
            while count < len(shinSkills):
                if count == 0:
                    pnach.write(f"\n\n//Shinjiro skills (Level {shinLv})")
                pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                            f"{format(8607924 + (count * 2), 'x').upper()},short,0{shinSkills[count]}")
                count += 1
            if count != 0:
                while count < 8:
                    pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                                f"{format(8607924 + (count * 2), 'x').upper()},short,0000")
                    count += 1

            if shinLv != 0:
                Strength = 0
                Magic = 0
                Endurance = 0
                Agility = 0
                Luck = 0
                for (Level, Str, Mag, End, Agi, Luc) in shinjiro_Stats:
                    if Level <= shinLv:
                        Strength += Str
                        Magic += Mag
                        Endurance += End
                        Agility += Agi
                        Luck += Luc

                pnach.write(f"\n\n//Shinjiro Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                            f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,208358C4,"
                            f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                            f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,008358C8,"
                            f"extended,000000{format(Luck, 'x').upper()}")

        # Metis
        elif gameType == 'A':
            count = 0
            while count < len(metSkills):
                if count == 0:
                    pnach.write(f"\n\n//Metis skills (Level {metLv})")
                pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                            f"{format(8607924 + (count * 2), 'x').upper()},short,0{metSkills[count]}")
                count += 1
            if count != 0:
                while count < 8:
                    pnach.write(f"\n//Persona Skill {str(count + 1)}\npatch=1,EE,00"
                                f"{format(8607924 + (count * 2), 'x').upper()},short,0000")
                    count += 1

            if metLv != 0:
                Strength = 0
                Magic = 0
                Endurance = 0
                Agility = 0
                Luck = 0
                for (Level, Str, Mag, End, Agi, Luc) in metis_Stats:
                    if Level <= metLv:
                        Strength += Str
                        Magic += Mag
                        Endurance += End
                        Agility += Agi
                        Luck += Luc

                pnach.write(f"\n\n//Metis Stats\n//Strength: {str(Strength)}\t\tMagic: {str(Magic)}\t\tEndurance: "
                            f"{str(Endurance)}\t\tAgility: {str(Agility)}\t\tLuck: {str(Luck)}\npatch=1,EE,208358C4,"
                            f"extended,{format(Agility, 'x').upper()}{format(Endurance, 'x').upper()}"
                            f"{format(Magic, 'x').upper()}{format(Strength, 'x').upper()}\npatch=1,EE,008358C8,"
                            f"extended,000000{format(Luck, 'x').upper()}")

# Calls another window to display results
root = Tk()
root.title("Party Skill Editor")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Prints out the results of the user input
# Error message if radio buttons are not selected
if errorMessage == 1:
    ttk.Label(mainframe, text="Invalid response. Please select the Journey or Answer AND New Moon or Vanilla").grid(
        column=1, row=1, sticky=W)
else:
    ttk.Label(mainframe, text="Cheat code created for:").grid(column=1, row=1, sticky=W)
# Prints "The Journey" or "The Answer"    
    if gameType == 'A':
        ttk.Label(mainframe, text="The Answer").grid(column=1, row=2, sticky=W)
        ttk.Label(mainframe, text="Date check skipped").grid(column=1, row=3, sticky=W)
    elif gameType == 'J':
        ttk.Label(mainframe, text="The Journey").grid(column=1, row=2, sticky=W)
# Prints the date or an error message for an invalid date       
        if errorMessage == 2:
            ttk.Label(mainframe, text="Invalid date. Personas may be unevolved").grid(column=1, row=3, sticky=W)
        else:
            ttk.Label(mainframe, text="Date entered: " + str(monthCheck) + "/" + str(dayCheck)).grid(
                column=1, row=3, sticky=W)
# Prints "Vanilla" or "New Moon" 
    if modCheck == 'V':
        ttk.Label(mainframe, text="Vanilla (unmodded)").grid(column=1, row=4, sticky=W)
    elif modCheck == 'M':
        ttk.Label(mainframe, text="New Moon (modded)").grid(column=1, row=4, sticky=W)
# Prints out whichever characters have codes and the levels inputted for each
    if yukLv != 0:
        ttk.Label(mainframe, text="Yukari: Level " + str(yukLv)).grid(column=1, row=5, sticky=W)
    if junLv != 0:
        ttk.Label(mainframe, text="Junpei: Level " + str(junLv)).grid(column=1, row=6, sticky=W)
    if akiLv != 0:
        ttk.Label(mainframe, text="Akihiko: Level " + str(akiLv)).grid(column=1, row=7, sticky=W)
    if mitLv != 0:
        ttk.Label(mainframe, text="Mitsuru: Level " + str(mitLv)).grid(column=1, row=8, sticky=W)
    if aigLv != 0 and gameType != 'A':
        ttk.Label(mainframe, text="Aigis: Level " + str(aigLv)).grid(column=1, row=9, sticky=W)
    if koroLv != 0:
        ttk.Label(mainframe, text="Koromaru: Level " + str(koroLv)).grid(column=1, row=10, sticky=W)
    if kenLv != 0:
        ttk.Label(mainframe, text="Ken: Level " + str(kenLv)).grid(column=1, row=11, sticky=W)
    if shinLv != 0 and gameType != 'A':
        ttk.Label(mainframe, text="Shinjiro: Level " + str(shinLv)).grid(column=1, row=12, sticky=W)
    if metLv != 0 and gameType == 'A':
        ttk.Label(mainframe, text="Metis: Level " + str(metLv)).grid(column=1, row=12, sticky=W)

root.mainloop()
