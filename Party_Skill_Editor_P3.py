import skillID
import partySkills

# checks if for vanilla FES or New Moon
newMoonCheck = input("Type 'F' for unmodded Persona 3 FES, or 'M' for Persona 3 FES with the New Moon Balance Patch: ")
if newMoonCheck not in ["F", "f", "M", "m"]:
    errorMessage = input("Invalid response. Only 'F' and 'M' are acceptable")
    raise SystemExit

# checks if for The Journey or The Answer
gameCheck = input("Type 'J' for The Journey, or 'A' for The Answer: ")
if gameCheck not in ["J", "j", "A", "a"]:
    errorMessage = input("Invalid response. Only 'J' and 'A' are acceptable")
    raise SystemExit

# checks the level for each party member
print("Enter the level of each party member. If you do not have the member, or want to skip them, enter '0'")
yukariLvl = int(input("Yukari: "))
junpeiLvl = int(input("Junpei: "))
akihikoLvl = int(input("Akihiko: "))
mitsuruLvl = int(input("Mitsuru: "))
aigisLvl = int(input("Aigis: "))
koromaruLvl = int(input("Koromaru: "))
kenLvl = int(input("Ken: "))
if gameCheck in ["J", "j"]:
    shinjiroLvl = int(input("Shinjiro: "))
elif gameCheck in ["A", "a"]:
    metisLvl = int(input("Metis: "))

# Creates/ overwrites the pnach file
overwrite = open("94A82AAA_partySkills.pnach", "w")
overwrite.write("")
pnach = open("94A82AAA_partySkills.pnach", "a")

# Yukari
# Removes skills from the list depending on what level is inputted. Maximum of eight skills at any level
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

#   Writes the first (and only) eight skills to the file
    count = 0
    while count < len(partySkills.yukSkills):
        if count == 0:
            pnach.write("//Yukari skills")
        pnach.write("\n//Yukari Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                    format(8601848 + (count * 2), "x") + ",short,0" + partySkills.yukSkills[count])
        count += 1

# Junpei
if junpeiLvl != 0:
    SoLCheck = input("Does Junpei have 'Spring of Life'? Type 'y' if so: ")
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

    count = 0
    while count < len(partySkills.junSkills):
        if count == 0:
            pnach.write("\n\n//Junpei skills")
        pnach.write("\n//Junpei Persona Skill " + (str(count + 1).upper()) + "\npatch=1,EE,00" +
                    format(8604452 + (count * 2), "x") + ",short,0" + partySkills.junSkills[count])
        count += 1

#   Akihiko
if akihikoLvl != 0:
    if newMoonCheck in ["F", "f"]:
        partySkills.akiSkills.remove(skillID.Debilitate)
        partySkills.akiSkills.remove(skillID.Thunder_Reign)
        if akihikoLvl < 53:
            partySkills.akiSkills.remove(skillID.Ziodyne)
        if akihikoLvl < 66:
            partySkills.akiSkills.remove(skillID.Masukunda)
    if newMoonCheck in ["M", "m"]:
        partySkills.akiSkills.remove(skillID.Masukunda)
        if akihikoLvl not in range(53, 79):
            partySkills.akiSkills.remove(skillID.Ziodyne)
        if akihikoLvl < 66:
            partySkills.akiSkills.remove(skillID.Debilitate)

    if akihikoLvl >= 50:
        partySkills.akiSkills.remove(skillID.Sonic_Punch)
    if akihikoLvl >= 29:
        partySkills.akiSkills.remove(skillID.Zio)
    if akihikoLvl >= 38:
        partySkills.akiSkills.remove(skillID.Dia)
    if akihikoLvl not in range(16, 46):
        partySkills.akiSkills.remove(skillID.Tarunda)
    if akihikoLvl not in range(21, 40):
        partySkills.akiSkills.remove(skillID.Mazio)
    if akihikoLvl not in range(25, 56):
        partySkills.akiSkills.remove(skillID.Rakunda)
    if akihikoLvl not in range(29, 52):
        partySkills.akiSkills.remove(skillID.Zionga)
    if akihikoLvl not in range(33, 65):
        partySkills.akiSkills.remove(skillID.Sukunda)
    if akihikoLvl not in range(37, 75):
        partySkills.akiSkills.remove(skillID.Elec_Boost)
    if akihikoLvl not in range(38, 64):
        partySkills.akiSkills.remove(skillID.Diarama)
    if akihikoLvl not in range(41, 73):
        partySkills.akiSkills.remove(skillID.Mazionga)
    if akihikoLvl < 47:
        partySkills.akiSkills.remove(skillID.Matarunda)
    if akihikoLvl < 50:
        partySkills.akiSkills.remove(skillID.Fist_Master)
    if akihikoLvl < 57:
        partySkills.akiSkills.remove(skillID.Marakunda)
    if akihikoLvl < 65:
        partySkills.akiSkills.remove(skillID.Diarahan)
    if akihikoLvl < 74:
        partySkills.akiSkills.remove(skillID.Maziodyne)
    if akihikoLvl < 76:
        partySkills.akiSkills.remove(skillID.Elec_Amp)

    count = 0
    while count < len(partySkills.akiSkills):
        if count == 0:
            pnach.write("\n\n//Akihiko skills")
        pnach.write("\n//Akihiko Persona Skill " + (str(count + 1).upper()) + "\npatch=1,EE,00" +
                    format(8606188 + (count * 2), "x") + ",short,0" + partySkills.akiSkills[count])
        count += 1

# Mitsuru
if mitsuruLvl != 0:
    if newMoonCheck in ["F", "f"]:
        partySkills.mitSkills.remove(skillID.Niflheim)
        if mitsuruLvl < 55:
            partySkills.mitSkills.remove(skillID.Bufudyne)
    if newMoonCheck in ["M", "m"]:
        if mitsuruLvl not in range(55, 79):
            partySkills.mitSkills.remove(skillID.Bufudyne)
        if mitsuruLvl < 80:
            partySkills.mitSkills.remove(skillID.Niflheim)

    if mitsuruLvl >= 21:
        partySkills.mitSkills.remove(skillID.Bufu)
    if mitsuruLvl >= 42:
        partySkills.mitSkills.remove(skillID.Mabufu)
    if mitsuruLvl >= 25:
        partySkills.mitSkills.remove(skillID.Dia)
    if mitsuruLvl >= 50:
        partySkills.mitSkills.remove(skillID.Marin_Karin)
    if mitsuruLvl not in range(21, 41):
        partySkills.mitSkills.remove(skillID.Bufula)
    if mitsuruLvl not in range(25, 57):
        partySkills.mitSkills.remove(skillID.Diarama)
    if mitsuruLvl < 27:
        partySkills.mitSkills.remove(skillID.Spirit_Drain)
    if mitsuruLvl < 32:
        partySkills.mitSkills.remove(skillID.Tentarafoo)
    if mitsuruLvl not in range(42, 70):
        partySkills.mitSkills.remove(skillID.Mabufula)
    if mitsuruLvl not in range(45, 75):
        partySkills.mitSkills.remove(skillID.Ice_Boost)
    if mitsuruLvl < 50:
        partySkills.mitSkills.remove(skillID.Mind_Charge)
    if mitsuruLvl < 58:
        partySkills.mitSkills.remove(skillID.Diarahan)
    if mitsuruLvl < 61:
        partySkills.mitSkills.remove(skillID.Ice_Break)
    if mitsuruLvl < 71:
        partySkills.mitSkills.remove(skillID.Mabufudyne)
    if mitsuruLvl < 76:
        partySkills.mitSkills.remove(skillID.Ice_Amp)

    count = 0
    while count < len(partySkills.mitSkills):
        if count == 0:
            pnach.write("\n\n//Mitsuru skills")
        pnach.write("\n//Mitsuru Persona Skill " + (str(count + 1).upper()) + "\npatch=1,EE,00" +
                    format(8603584 + (count * 2), "x") + ",short,0" + partySkills.mitSkills[count])
        count += 1

# Aigis


# closing message
print("Done! Place in your cheats folder.")
