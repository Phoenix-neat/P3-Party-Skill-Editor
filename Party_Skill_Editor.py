from skillID import *

yukSkills = []
junSkills = []
akiSkills = []
mitSkills = []
aigSkills = []
koroSkills = []
kenSkills = []
shinSkills = []
metSkills = []

# Python 2.7 compatibility
try:
    input = raw_input
except NameError:
    pass

# checks if for The Journey or The Answer
gameCheck = input("Type 'J' for The Journey, or 'A' for The Answer: ")
if gameCheck not in ["J", "j", "A", "a"]:
    errorMessage = input("Invalid response. Only 'J' and 'A' are acceptable")
    raise SystemExit

# checks if for vanilla FES or New Moon
modCheck = input("Type 'F' for vanilla Persona 3 FES, or 'M' for Persona 3 FES with the New Moon Balance Patch: ")
if modCheck in ["F", "f"] and gameCheck in ["J", "j"]:
    from Skill_Progressions.Party_Unmodded import *
elif modCheck in ["F", "f"] and gameCheck in ["A", "a"]:
    from Skill_Progressions.Party_Unmodded_A import *
elif modCheck in ["M", "m"] and gameCheck in ["J", "j"]:
    from Skill_Progressions.Party_Modded import *
elif modCheck in ["M", "m"] and gameCheck in ["A", "a"]:
    from Skill_Progressions.Party_Modded_A import *
else:
    errorMessage = input("Invalid response. Only 'F' and 'M' are acceptable")
    raise SystemExit


# checks the level for each party member
print("\nEnter the level of each party member. If you do not have the member, or want to skip them, enter '0'\n")
yukLv = int(input("Yukari: "))
for (minLv, maxLv, skill) in yukari:
    if(yukLv >= minLv and yukLv < maxLv):
        yukSkills.append(skill)

junLv = int(input("Junpei: "))
for (minLv, maxLv, skill) in junpei:
    if(junLv >= minLv and junLv < maxLv):
        junSkills.append(skill)

akiLv = int(input("Akihiko: "))
for (minLv, maxLv, skill) in akihiko:
    if(akiLv >= minLv and akiLv < maxLv):
        akiSkills.append(skill)

mitLv = int(input("Mitsuru: "))
for (minLv, maxLv, skill) in mitsuru:
    if(mitLv >= minLv and mitLv < maxLv):
        mitSkills.append(skill)

if gameCheck in ["J", "j"]:
    aigLv = int(input("Aigis: "))
    for (minLv, maxLv, skill) in aigis:
        if(aigLv >= minLv and aigLv < maxLv):
            aigSkills.append(skill)

koroLv = int(input("Koromaru: "))
for (minLv, maxLv, skill) in koromaru:
    if(koroLv >= minLv and koroLv < maxLv):
        koroSkills.append(skill)


kenLv = int(input("Ken: "))
for (minLv, maxLv, skill) in ken:
    if(kenLv >= minLv and kenLv < maxLv):
        kenSkills.append(skill)

if gameCheck in ["J", "j"]:
    shinLv = int(input("Shinjiro: "))
    for (minLv, maxLv, skill) in shinjiro:
        if(shinLv >= minLv and shinLv < maxLv):
            shinSkills.append(skill)
elif gameCheck in ["A", "a"]:
    metLv = int(input("Metis: "))
    for (minLv, maxLv, skill) in metis:
        if(metLv >= minLv and metLv < maxLv):
            metSkills.append(skill)

# Creates/ overwrites the pnach file
with open("94A82AAA_partySkills.pnach", "w") as overwrite:
    overwrite.write("Persona 3 FES Party Skill Overwrite")

with open("94A82AAA_partySkills.pnach", "a") as pnach:
    #Writes the first (and only) eight skills to the file
    #Yukari
        count = 0
        while count < len(yukSkills):
            if count == 0:
                pnach.write("\n\n//Yukari skills")
            pnach.write("\n//Yukari Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                        format(8601848 + (count * 2), "x") + ",short,0" + yukSkills[count])
            count += 1
        #fills in the remaining skill slots with blank entries to overwrite potential duplicates/ unwanted skills
        if count != 0:
            while count < 8:
                pnach.write("\n//Yukari Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                            format(8601848 + (count * 2), "x") + ",short,0000")
                count += 1
    
    #Junpei
        count = 0
        while count < len(junSkills):
            if count == 0:
                pnach.write("\n\n//Junpei skills")
            pnach.write("\n//Junpei Persona Skill " + (str(count + 1).upper()) + "\npatch=1,EE,00" +
                        format(8604452 + (count * 2), "x") + ",short,0" + junSkills[count])
            count += 1
        if count != 0:
            while count < 8:
                pnach.write("\n//Junpei Persona Skill " + (str(count + 1).upper()) + "\npatch=1,EE,00" +
                            format(8604452 + (count * 2), "x") + ",short,0000")
                count += 1
    
    #Akihiko
        count = 0
        while count < len(akiSkills):
            if count == 0:
                pnach.write("\n\n//Akihiko skills")
            pnach.write("\n//Akihiko Persona Skill " + (str(count + 1).upper()) + "\npatch=1,EE,00" +
                        format(8606188 + (count * 2), "x") + ",short,0" + akiSkills[count])
            count += 1
        if count != 0:
            while count < 8:
                pnach.write("\n//Akihiko Persona Skill " + (str(count + 1).upper()) + "\npatch=1,EE,00" +
                            format(8606188 + (count * 2), "x") + ",short,0000")
                count += 1

    #Mitsuru
        count = 0
        while count < len(mitSkills):
            if count == 0:
                pnach.write("\n\n//Mitsuru skills")
            pnach.write("\n//Mitsuru Persona Skill " + (str(count + 1).upper()) + "\npatch=1,EE,00" +
                        format(8603584 + (count * 2), "x") + ",short,0" + mitSkills[count])
            count += 1
        if count != 0:
            while count < 8:
                pnach.write("\n//Mitsuru Persona Skill " + (str(count + 1).upper()) + "\npatch=1,EE,00" +
                            format(8603584 + (count * 2), "x") + ",short,0000")
                count += 1
    
    #Aigis
        if gameCheck in ["J", "j"]:
            count = 0
            while count < len(aigSkills):
                if count == 0:
                    pnach.write("\n\n//Aigis skills")
                pnach.write("\n//Aigis Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                            format(8602716 + (count * 2), "x") + ",short,0" + aigSkills[count])
                count += 1
            if count != 0:
                while count < 8:
                    pnach.write("\n//Aigis Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                                format(8602716 + (count * 2), "x") + ",short,0000")
                    count += 1

    #Koromaru
        count = 0
        while count < len(koroSkills):
            if count == 0:
                pnach.write("\n\n//Koromaru skills")
            pnach.write("\n//Koromaru Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                        format(8608792 + (count * 2), "x") + ",short,0" + koroSkills[count])
            count += 1
        if count != 0:
            while count < 8:
                pnach.write("\n//Koromaru Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                            format(8608792 + (count * 2), "x") + ",short,0000")
                count += 1
    
    #Ken
        count = 0
        while count < len(kenSkills):
            if count == 0:
                pnach.write("\n\n//Ken skills")
            pnach.write("\n//Ken Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                        format(8607056 + (count * 2), "x") + ",short,0" + kenSkills[count])
            count += 1
        if count != 0:
            while count < 8:
                pnach.write("\n//Ken Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                            format(8607056 + (count * 2), "x") + ",short,0000")
                count += 1
    
    #Shinjiro and Metis
        if gameCheck in ["J", "j"]:
            count = 0
            while count < len(shinSkills):
                if count == 0:
                    pnach.write("\n\n//Shinjiro skills")
                pnach.write("\n//Shinjiro Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                            format(8607924 + (count * 2), "x") + ",short,0" + shinSkills[count])
                count += 1
            if count != 0:
                while count < 8:
                    pnach.write("\n//Shinjiro Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                                format(8607924 + (count * 2), "x") + ",short,0000")
                    count += 1
        elif gameCheck in ["A", "a"]:
            count = 0
            while count < len(metSkills):
                if count == 0:
                    pnach.write("\n\n//Metis skills")
                pnach.write("\n//Metis Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                            format(8607924 + (count * 2), "x") + ",short,0" + metSkills[count])
                count += 1
            if count != 0:
                while count < 8:
                    pnach.write("\n//Metis Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                                format(8607924 + (count * 2), "x") + ",short,0000")
                    count += 1

# closing message
redundant_check = input("\nDone! Place in your cheats folder.")
