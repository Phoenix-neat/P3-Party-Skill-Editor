import skillID
import partySkills

#checks if for vanilla FES or New Moon
newMoonCheck = input("Type 'F' for unmodded Persona 3 FES, or 'M' for Persona 3 FES with the New Moon Balance Patch: ")
if newMoonCheck not in ["F", "f", "M", "m"]:
    errorMessage = input("Invalid response. Only 'F' and 'M' are acceptable")
    raise SystemExit

#checks if for The Journey or The Answer
gameCheck = input("Type 'J' for The Journey, or 'A' for The Answer: ")
if gameCheck not in ["J", "j", "A", "a"]:
    errorMessage = input("Invalid response. Only 'J' and 'A' are acceptable")
    raise SystemExit

#checks the level for each party member
print("Enter in the levels of each party member. If you do not have the party member, enter '0'")
yukariLvl = int(input("Yukari: "))
junpeiLvl = int(input("Junpei: "))
SoLCheck = input("Does Junpei have 'Spring of Life'? Type 'y' if so: ")
akihikoLvl = int(input("Akihiko: "))
mitsuruLvl = int(input("Mitsuru: "))
aigisLvl = int(input("Aigis: "))
koromaruLvl = int(input("Koromaru: "))
kenLvl = int(input("Ken: "))
if gameCheck in  ["J", "j"]:
    shinjiroLvl = int(input("Shinjiro: "))
elif gameCheck in ["A", "a"]:
    metisLvl = int(input("Metis: "))

overwrite = open("test.txt", "w")
overwrite.write("")
pnach = open("test.txt", "a")

#for Yukari (All, includes New Moon J/A and Vanilla J/A)
if yukariLvl != 0:
    if newMoonCheck in ["F", "f"]:
        partySkills.yukSkills.remove(skillID.Amrita)
        partySkills.yukSkills.remove(skillID.Panta_Rhei)
    elif newMoonCheck in ["M", "m"]:
        if yukariLvl >= 55:
            partySkills.yukSkills.remove(skillID.Me_Patra)
        if yukariLvl >= 80:
            partySkills.yukSkills.remove(skillID.Garudyne)
    if yukariLvl >= 25:
        partySkills.yukSkills.remove(skillID.Dia)
    if yukariLvl not in range(4, 35):
        partySkills.yukSkills.remove(skillID.Patra)
    if yukariLvl not in range(5, 31):
        partySkills.yukSkills.remove(skillID.Garu)
    if yukariLvl < 16:
        partySkills.yukSkills.remove(skillID.Charmdi)
    if yukariLvl not in range(21, 45):
        partySkills.yukSkills.remove(skillID.Magaru)
    if yukariLvl not in range(22, 42):
        partySkills.yukSkills.remove(skillID.Media)
    if yukariLvl not in range(25, 51):
        partySkills.yukSkills.remove(skillID.Diarama)
    if yukariLvl not in range(28, 67):
        partySkills.yukSkills.remove(skillID.Recarm)
    if yukariLvl not in range(32, 57):
        partySkills.yukSkills.remove(skillID.Garula)
    if yukariLvl < 36:
        partySkills.yukSkills.remove(skillID.Me_Patra)
    if yukariLvl not in range(43, 74):
        partySkills.yukSkills.remove(skillID.Mediarama)
    if yukariLvl not in range(46, 65):
        partySkills.yukSkills.remove(skillID.Magarula)
    if yukariLvl < 52:
        partySkills.yukSkills.remove(skillID.Diarahan)
    if yukariLvl < 57:
        partySkills.yukSkills.remove(skillID.Garudyne)
    if yukariLvl < 60:
        partySkills.yukSkills.remove(skillID.Wind_Break)
    if yukariLvl < 65:
        partySkills.yukSkills.remove(skillID.Magarudyne)
    if yukariLvl < 68:
        partySkills.yukSkills.remove(skillID.Samarecarm)
    if yukariLvl < 74:
        partySkills.yukSkills.remove(skillID.Mediarahan)

    pnach.write(
        "//Yukari skills \n//Yukari Persona Skill 1\npatch=1,EE,108340F8,short,0" + partySkills.yukSkills[0])
    if len(partySkills.yukSkills) > 1:
        pnach.write("\n//Yukari Persona Skill 2\npatch=1,EE,008340FA,short,0" + partySkills.yukSkills[1])
    if len(partySkills.yukSkills) > 2:
        pnach.write("\n//Yukari Persona Skill 3\npatch=1,EE,008340FC,short,0" + partySkills.yukSkills[2])
    if len(partySkills.yukSkills) > 3:
        pnach.write("\n//Yukari Persona Skill 4\npatch=1,EE,008340FE,short,0" + partySkills.yukSkills[3])
    if len(partySkills.yukSkills) > 4:
        pnach.write("\n//Yukari Persona Skill 5\npatch=1,EE,00834100,short,0" + partySkills.yukSkills[4])
    if len(partySkills.yukSkills) > 5:
        pnach.write("\n//Yukari Persona Skill 6\npatch=1,EE,00834102,short,0" + partySkills.yukSkills[5])
    if len(partySkills.yukSkills) > 6:
        pnach.write("\n//Yukari Persona Skill 7\npatch=1,EE,00834104,short,0" + partySkills.yukSkills[6])
    if len(partySkills.yukSkills) > 7:
        pnach.write("\n//Yukari Persona Skill 8\npatch=1,EE,00834106,short,0" + partySkills.yukSkills[7])

#for Junpei
if junpeiLvl != 0:
    if SoLCheck not in ["Y", "y"]:
        partySkills.junSkills.remove(skillID.Spring_of_Life)

    if newMoonCheck in ["F", "f"]:
        partySkills.junSkills.remove(skillID.Power_Charge)
        partySkills.junSkills.remove(skillID.Phys_Skill_Up)
        if junpeiLvl >= 18:
            partySkills.junSkills.remove(skillID.Cleave)
        if junpeiLvl not in range(5, 31):
            partySkills.junSkills.remove(skillID.Agi)
        if junpeiLvl not in range(9, 43):
            partySkills.junSkills.remove(skillID.Rakukaja)
        if junpeiLvl not in range(18, 24):
            partySkills.junSkills.remove(skillID.Assault_Dive)
        if junpeiLvl not in range(25, 54):
            partySkills.junSkills.remove(skillID.Kill_Rush)
        if junpeiLvl not in range(32, 63):
            partySkills.junSkills.remove(skillID.Agilao)
        if junpeiLvl not in range(35, 44):
            partySkills.junSkills.remove(skillID.Counter)
        if junpeiLvl < 44:
            partySkills.junSkills.remove(skillID.Marakukaja)
        if junpeiLvl < 55:
            partySkills.junSkills.remove(skillID.Gigantic_Fist)
        if junpeiLvl < 60:
            partySkills.junSkills.remove(skillID.Fire_Break)

    elif newMoonCheck in ["M", "m"]:
        partySkills.junSkills.remove(skillID.Assault_Dive)
        partySkills.junSkills.remove(skillID.Fire_Break)
        if gameCheck in ["J", "j"]:
            if junpeiLvl >= 31:
                partySkills.junSkills.remove(skillID.Cleave)
        if gameCheck in ["A", "a"]:
            partySkills.junSkills.remove(skillID.Cleave)
        if junpeiLvl not in range(5, 29):
            partySkills.junSkills.remove(skillID.Agi)
        if junpeiLvl not in range(9, 33):
            partySkills.junSkills.remove(skillID.Rakukaja)
        if junpeiLvl not in range(18, 54):
            partySkills.junSkills.remove(skillID.Kill_Rush)
        if junpeiLvl not in range(30, 63):
            partySkills.junSkills.remove(skillID.Agilao)
        if junpeiLvl not in range(31, 44):
            partySkills.junSkills.remove(skillID.Counter)
        if junpeiLvl < 34:
            partySkills.junSkills.remove(skillID.Marakukaja)
        if junpeiLvl not in range(55, 80):
            partySkills.junSkills.remove(skillID.Gigantic_Fist)
        if junpeiLvl < 60:
            partySkills.junSkills.remove(skillID.Power_Charge)
        if junpeiLvl < 80:
            partySkills.junSkills.remove(skillID.Phys_Skill_Up)

    if gameCheck in ["J", "j"]:
        partySkills.junSkills.remove(skillID.Vorpal_Blade_Answer)
        if junpeiLvl < 75:
            partySkills.junSkills.remove(skillID.Vorpal_Blade)
    elif gameCheck in ["A", "a"]:
        partySkills.junSkills.remove(skillID.Vorpal_Blade)
        if junpeiLvl < 75:
            partySkills.junSkills.remove(skillID.Vorpal_Blade_Answer)

    if junpeiLvl not in range(7, 49):
        partySkills.junSkills.remove(skillID.Re_Patra)
    if junpeiLvl not in range(20, 39):
        partySkills.junSkills.remove(skillID.Double_Fangs)
    if junpeiLvl not in range(40, 74):
        partySkills.junSkills.remove(skillID.Torrent_Shot)
    if junpeiLvl not in range(45, 57):
        partySkills.junSkills.remove(skillID.Counterstrike)
    if junpeiLvl not in range(50, 65):
        partySkills.junSkills.remove(skillID.Blade_of_Fury)
    if junpeiLvl < 58:
        partySkills.junSkills.remove(skillID.High_Counter)
    if junpeiLvl < 64:
        partySkills.junSkills.remove(skillID.Agidyne)
    if junpeiLvl < 65:
        partySkills.junSkills.remove(skillID.Brave_Blade)

    pnach.write(
        "\n\n//Junpei skills \n//Junpei Persona Skill 1\npatch=1,EE,10834B24,extended,00000" + partySkills.junSkills[0])
    if len(partySkills.junSkills) > 1:
        pnach.write("\n//Junpei Persona Skill 2\npatch=1,EE,10834B26,extended,00000" + partySkills.junSkills[1])
    if len(partySkills.junSkills) > 2:
        pnach.write("\n//Junpei Persona Skill 3\npatch=1,EE,10834B28,extended,00000" + partySkills.junSkills[2])
    if len(partySkills.junSkills) > 3:
        pnach.write("\n//Junpei Persona Skill 4\npatch=1,EE,10834B2A,extended,00000" + partySkills.junSkills[3])
    if len(partySkills.junSkills) > 4:
        pnach.write("\n//Junpei Persona Skill 5\npatch=1,EE,10834B2C,extended,00000" + partySkills.junSkills[4])
    if len(partySkills.junSkills) > 5:
        pnach.write("\n//Junpei Persona Skill 6\npatch=1,EE,10834B2E,extended,00000" + partySkills.junSkills[5])
    if len(partySkills.junSkills) > 6:
        pnach.write("\n//Junpei Persona Skill 7\npatch=1,EE,10834B30,extended,00000" + partySkills.junSkills[6])
    if len(partySkills.junSkills) > 7:
        pnach.write("\n//Junpei Persona Skill 8\npatch=1,EE,10834B32,extended,00000" + partySkills.junSkills[7])
