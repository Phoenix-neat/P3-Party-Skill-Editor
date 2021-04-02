import skillID
import partySkills

# Python 2.7 compatibility
try:
    input = raw_input
except NameError:
    pass

# checks if for vanilla FES or New Moon
newMoonCheck = input("Type 'F' for vanilla Persona 3 FES, or 'M' for Persona 3 FES with the New Moon Balance Patch: ")
if newMoonCheck not in ["F", "f", "M", "m"]:
    errorMessage = input("Invalid response. Only 'F' and 'M' are acceptable")
    raise SystemExit

# checks if for The Journey or The Answer
gameCheck = input("Type 'J' for The Journey, or 'A' for The Answer: ")
if gameCheck not in ["J", "j", "A", "a"]:
    errorMessage = input("Invalid response. Only 'J' and 'A' are acceptable")
    raise SystemExit

# checks the level for each party member
print("\nEnter the level of each party member. If you do not have the member, or want to skip them, enter '0'\n")
yukariLvl = int(input("Yukari: "))
junpeiLvl = int(input("Junpei: "))
akihikoLvl = int(input("Akihiko: "))
mitsuruLvl = int(input("Mitsuru: "))
koromaruLvl = int(input("Koromaru: "))
kenLvl = int(input("Ken: "))
if gameCheck in ["J", "j"]:
    aigisLvl = int(input("Aigis: "))
    shinjiroLvl = int(input("Shinjiro: "))
# elif gameCheck in ["A", "a"]:
#    metisLvl = int(input("Metis: "))

# Creates/ overwrites the pnach file
with open("94A82AAA_partySkills.pnach", "w") as overwrite:
    overwrite.write("Persona 3 FES Party Skill Overwrite")

with open("94A82AAA_partySkills.pnach", "a") as pnach:

    # Yukari
    # Removes skills from the list depending on what level is inputted. Maximum of eight skills at any level
    if yukariLvl != 0:
        if newMoonCheck in ["F", "f"]:
            partySkills.yukSkills.remove(skillID.Amrita)
            partySkills.yukSkills.remove(skillID.Panta_Rhei)
            if yukariLvl < 36:
                partySkills.yukSkills.remove(skillID.Me_Patra)
            if yukariLvl < 57:
                partySkills.yukSkills.remove(skillID.Garudyne)
        elif newMoonCheck in ["M", "m"]:
            if yukariLvl not in range(36, 55):
                partySkills.yukSkills.remove(skillID.Me_Patra)
            if yukariLvl < 55:
                partySkills.yukSkills.remove(skillID.Amrita)
            if yukariLvl not in range(57, 80):
                partySkills.yukSkills.remove(skillID.Garudyne)
            if yukariLvl < 80:
                partySkills.yukSkills.remove(skillID.Panta_Rhei)
        if yukariLvl >= 25:
            partySkills.yukSkills.remove(skillID.Dia)
        if yukariLvl not in range(4, 36):
            partySkills.yukSkills.remove(skillID.Patra)
        if yukariLvl not in range(5, 32):
            partySkills.yukSkills.remove(skillID.Garu)
        if yukariLvl < 16:
            partySkills.yukSkills.remove(skillID.Charmdi)
        if yukariLvl not in range(21, 46):
            partySkills.yukSkills.remove(skillID.Magaru)
        if yukariLvl not in range(22, 43):
            partySkills.yukSkills.remove(skillID.Media)
        if yukariLvl not in range(25, 52):
            partySkills.yukSkills.remove(skillID.Diarama)
        if yukariLvl not in range(28, 68):
            partySkills.yukSkills.remove(skillID.Recarm)
        if yukariLvl not in range(32, 57):
            partySkills.yukSkills.remove(skillID.Garula)
        if yukariLvl not in range(43, 74):
            partySkills.yukSkills.remove(skillID.Mediarama)
        if yukariLvl not in range(46, 65):
            partySkills.yukSkills.remove(skillID.Magarula)
        if yukariLvl < 52:
            partySkills.yukSkills.remove(skillID.Diarahan)
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
                pnach.write("\n\n//Yukari skills")
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
            if junpeiLvl not in range(5, 32):
                partySkills.junSkills.remove(skillID.Agi)
            if junpeiLvl not in range(18, 25):
                partySkills.junSkills.remove(skillID.Assault_Dive)
            if junpeiLvl not in range(25, 55):
                partySkills.junSkills.remove(skillID.Kill_Rush)
            if junpeiLvl < 44:
                partySkills.junSkills.remove(skillID.Marakukaja)
            if junpeiLvl < 55:
                partySkills.junSkills.remove(skillID.Gigantic_Fist)
            if junpeiLvl < 60:
                partySkills.junSkills.remove(skillID.Fire_Break)

            if gameCheck in ["J", "j"]:
                partySkills.junSkills.remove(skillID.Deathbound)
                if junpeiLvl not in range(32, 64):
                    partySkills.junSkills.remove(skillID.Agilao)
                if junpeiLvl not in range(35, 45):
                    partySkills.junSkills.remove(skillID.Counter)
                if junpeiLvl not in range(9, 44):
                    partySkills.junSkills.remove(skillID.Rakukaja)
                if junpeiLvl < 65:
                    partySkills.junSkills.remove(skillID.Brave_Blade)
            elif gameCheck in ["A", "a"]:
                partySkills.junSkills.remove(skillID.Brave_Blade)
                if junpeiLvl not in range(30, 64):
                    partySkills.junSkills.remove(skillID.Agilao)
                if junpeiLvl not in range(31, 45):
                    partySkills.junSkills.remove(skillID.Counter)
                if junpeiLvl < 34:
                    partySkills.junSkills.remove(skillID.Marakukaja)
                if junpeiLvl < 65:
                    partySkills.junSkills.remove(skillID.Deathbound)

        elif newMoonCheck in ["M", "m"]:
            partySkills.junSkills.remove(skillID.Assault_Dive)
            partySkills.junSkills.remove(skillID.Fire_Break)
            partySkills.junSkills.remove(skillID.Deathbound)
            if gameCheck in ["J", "j"]:
                if junpeiLvl >= 31:
                    partySkills.junSkills.remove(skillID.Cleave)
            if gameCheck in ["A", "a"]:
                partySkills.junSkills.remove(skillID.Cleave)
            if junpeiLvl not in range(5, 30):
                partySkills.junSkills.remove(skillID.Agi)
            if junpeiLvl not in range(9, 34):
                partySkills.junSkills.remove(skillID.Rakukaja)
            if junpeiLvl not in range(18, 55):
                partySkills.junSkills.remove(skillID.Kill_Rush)
            if junpeiLvl not in range(30, 64):
                partySkills.junSkills.remove(skillID.Agilao)
            if junpeiLvl not in range(31, 45):
                partySkills.junSkills.remove(skillID.Counter)
            if junpeiLvl < 34:
                partySkills.junSkills.remove(skillID.Marakukaja)
            if junpeiLvl not in range(55, 80):
                partySkills.junSkills.remove(skillID.Gigantic_Fist)
            if junpeiLvl < 60:
                partySkills.junSkills.remove(skillID.Power_Charge)
            if junpeiLvl < 80:
                partySkills.junSkills.remove(skillID.Phys_Skill_Up)
            if junpeiLvl < 65:
                partySkills.junSkills.remove(skillID.Brave_Blade)

        if gameCheck in ["J", "j"]:
            partySkills.junSkills.remove(skillID.Vorpal_Blade_Answer)
            if junpeiLvl < 75:
                partySkills.junSkills.remove(skillID.Vorpal_Blade)
        elif gameCheck in ["A", "a"]:
            partySkills.junSkills.remove(skillID.Vorpal_Blade)
            if junpeiLvl < 75:
                partySkills.junSkills.remove(skillID.Vorpal_Blade_Answer)

        if junpeiLvl not in range(7, 50):
            partySkills.junSkills.remove(skillID.Re_Patra)
        if junpeiLvl not in range(20, 40):
            partySkills.junSkills.remove(skillID.Double_Fangs)
        if junpeiLvl not in range(40, 75):
            partySkills.junSkills.remove(skillID.Torrent_Shot)
        if junpeiLvl not in range(45, 58):
            partySkills.junSkills.remove(skillID.Counterstrike)
        if junpeiLvl not in range(50, 65):
            partySkills.junSkills.remove(skillID.Blade_of_Fury)
        if junpeiLvl < 58:
            partySkills.junSkills.remove(skillID.High_Counter)
        if junpeiLvl < 64:
            partySkills.junSkills.remove(skillID.Agidyne)

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
        elif newMoonCheck in ["M", "m"]:
            partySkills.akiSkills.remove(skillID.Masukunda)
            if akihikoLvl not in range(53, 80):
                partySkills.akiSkills.remove(skillID.Ziodyne)
            if akihikoLvl < 66:
                partySkills.akiSkills.remove(skillID.Debilitate)
            if akihikoLvl < 80:
                partySkills.akiSkills.remove(skillID.Thunder_Reign)

        if akihikoLvl >= 50:
            partySkills.akiSkills.remove(skillID.Sonic_Punch)
        if akihikoLvl >= 29:
            partySkills.akiSkills.remove(skillID.Zio)
        if akihikoLvl >= 38:
            partySkills.akiSkills.remove(skillID.Dia)
        if akihikoLvl not in range(16, 47):
            partySkills.akiSkills.remove(skillID.Tarunda)
        if akihikoLvl not in range(21, 41):
            partySkills.akiSkills.remove(skillID.Mazio)
        if akihikoLvl not in range(25, 57):
            partySkills.akiSkills.remove(skillID.Rakunda)
        if akihikoLvl not in range(29, 53):
            partySkills.akiSkills.remove(skillID.Zionga)
        if akihikoLvl not in range(33, 66):
            partySkills.akiSkills.remove(skillID.Sukunda)
        if akihikoLvl not in range(37, 76):
            partySkills.akiSkills.remove(skillID.Elec_Boost)
        if akihikoLvl not in range(38, 65):
            partySkills.akiSkills.remove(skillID.Diarama)
        if akihikoLvl not in range(41, 74):
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
            if mitsuruLvl not in range(55, 80):
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
        if mitsuruLvl not in range(21, 55):
            partySkills.mitSkills.remove(skillID.Bufula)
        if mitsuruLvl not in range(25, 58):
            partySkills.mitSkills.remove(skillID.Diarama)
        if mitsuruLvl < 27:
            partySkills.mitSkills.remove(skillID.Spirit_Drain)
        if mitsuruLvl < 32:
            partySkills.mitSkills.remove(skillID.Tentarafoo)
        if mitsuruLvl not in range(42, 71):
            partySkills.mitSkills.remove(skillID.Mabufula)
        if mitsuruLvl not in range(45, 76):
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
    if gameCheck in ["J", "j"]:
        if aigisLvl != 0:
            if newMoonCheck in ["F", "f"]:
                partySkills.aigSkills.remove(skillID.Heat_Riser)
                if aigisLvl < 47:
                    partySkills.aigSkills.remove(skillID.Masukukaja)
            if newMoonCheck in ["M", "m"]:
                partySkills.aigSkills.remove(skillID.Masukukaja)
                if aigisLvl < 47:
                    partySkills.aigSkills.remove(skillID.Heat_Riser)

            if aigisLvl >= 35:
                partySkills.aigSkills.remove(skillID.Kill_Rush)
            if aigisLvl >= 51:
                partySkills.aigSkills.remove(skillID.Swift_Strike)
            if aigisLvl >= 47:
                partySkills.aigSkills.remove(skillID.Sukukaja)
            if aigisLvl not in range(32, 56):
                partySkills.aigSkills.remove(skillID.Rakukaja)
            if aigisLvl not in range(35, 73):
                partySkills.aigSkills.remove(skillID.Fatal_End)
            if aigisLvl not in range(36, 60):
                partySkills.aigSkills.remove(skillID.Tarukaja)
            if aigisLvl < 42:
                partySkills.aigSkills.remove(skillID.Dekunda)
            if aigisLvl not in range(51, 77):
                partySkills.aigSkills.remove(skillID.Heat_Wave)
            if aigisLvl < 56:
                partySkills.aigSkills.remove(skillID.Marakukaja)
            if aigisLvl < 59:
                partySkills.aigSkills.remove(skillID.Diarahan)
            if aigisLvl < 60:
                partySkills.aigSkills.remove(skillID.Matarukaja)
            if aigisLvl < 65:
                partySkills.aigSkills.remove(skillID.Samarecarm)
            if aigisLvl < 73:
                partySkills.aigSkills.remove(skillID.Akasha_Arts)
            if aigisLvl < 77:
                partySkills.aigSkills.remove(skillID.Gods_Hand)

            count = 0
            while count < len(partySkills.aigSkills):
                if count == 0:
                    pnach.write("\n\n//Aigis skills")
                pnach.write("\n//Aigis Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                            format(8602716 + (count * 2), "x") + ",short,0" + partySkills.aigSkills[count])
                count += 1

    # Koromaru
    if koromaruLvl != 0:
        if newMoonCheck in ["F", "f"]:
            partySkills.koroSkills.remove(skillID.Apt_Pupil)
            partySkills.koroSkills.remove(skillID.Mighty_Swing)
            partySkills.koroSkills.remove(skillID.Desecrate)
            partySkills.koroSkills.remove(skillID.Heavens_Blade)
            partySkills.koroSkills.remove(skillID.Ragnarok)
            if koromaruLvl >= 56:
                partySkills.koroSkills.remove(skillID.Mudo)
            if koromaruLvl >= 40:
                partySkills.koroSkills.remove(skillID.Counter)
            if koromaruLvl not in range(40, 51):
                partySkills.koroSkills.remove(skillID.Counterstrike)
            if koromaruLvl not in range(42, 70):
                partySkills.koroSkills.remove(skillID.Mamudo)
            if koromaruLvl < 45:
                partySkills.koroSkills.remove(skillID.Agidyne)
            if koromaruLvl < 52:
                partySkills.koroSkills.remove(skillID.High_Counter)
            if koromaruLvl < 60:
                partySkills.koroSkills.remove(skillID.Mudo_Boost)
            if gameCheck in ["J", "j"]:
                if koromaruLvl not in range(38, 67):
                    partySkills.koroSkills.remove(skillID.Maragion)
                if koromaruLvl not in range(48, 77):
                    partySkills.koroSkills.remove(skillID.Fire_Boost)
                if koromaruLvl < 56:
                    partySkills.koroSkills.remove(skillID.Mudoon)
                if koromaruLvl < 71:
                    partySkills.koroSkills.remove(skillID.Mamudoon)
            elif gameCheck in ["A", "a"]:
                if koromaruLvl not in range(34, 67):
                    partySkills.koroSkills.remove(skillID.Maragion)
                if koromaruLvl not in range(39, 77):
                    partySkills.koroSkills.remove(skillID.Fire_Boost)
                if koromaruLvl < 33:
                    partySkills.koroSkills.remove(skillID.Mudoon)
                if koromaruLvl < 49:
                    partySkills.koroSkills.remove(skillID.Mamudoon)

        elif newMoonCheck in ["M", "m"]:
            partySkills.koroSkills.remove(skillID.Counter)
            partySkills.koroSkills.remove(skillID.Counterstrike)
            partySkills.koroSkills.remove(skillID.High_Counter)
            partySkills.koroSkills.remove(skillID.Mudo_Boost)
            if koromaruLvl >= 33:
                partySkills.koroSkills.remove(skillID.Mudo)
            if koromaruLvl not in range(34, 67):
                partySkills.koroSkills.remove(skillID.Maragion)
            if koromaruLvl not in range(40, 75):
                partySkills.koroSkills.remove(skillID.Mighty_Swing)
            if koromaruLvl not in range(42, 49):
                partySkills.koroSkills.remove(skillID.Mamudo)
            if koromaruLvl not in range(45, 80):
                partySkills.koroSkills.remove(skillID.Agidyne)
            if koromaruLvl not in range(39, 77):
                partySkills.koroSkills.remove(skillID.Fire_Boost)
            if koromaruLvl not in range(33, 71):
                partySkills.koroSkills.remove(skillID.Mudoon)
            if koromaruLvl < 49:
                partySkills.koroSkills.remove(skillID.Mamudoon)
            if koromaruLvl < 71:
                partySkills.koroSkills.remove(skillID.Desecrate)
            if koromaruLvl < 75:
                partySkills.koroSkills.remove(skillID.Heavens_Blade)
            if koromaruLvl < 80:
                partySkills.koroSkills.remove(skillID.Ragnarok)

        if koromaruLvl >= 45:
            partySkills.koroSkills.remove(skillID.Agilao)
        if koromaruLvl >= 50:
            partySkills.koroSkills.remove(skillID.Sukukaja)
        if koromaruLvl < 50:
            partySkills.koroSkills.remove(skillID.Masukukaja)
        if koromaruLvl < 67:
            partySkills.koroSkills.remove(skillID.Maragidyne)
        if koromaruLvl < 77:
            partySkills.koroSkills.remove(skillID.Fire_Amp)

        count = 0
        while count < len(partySkills.koroSkills):
            if count == 0:
                pnach.write("\n\n//Koromaru skills")
            pnach.write("\n//Koromaru Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                        format(8608792 + (count * 2), "x") + ",short,0" + partySkills.koroSkills[count])
            count += 1

    # Ken
    if kenLvl != 0:
        if newMoonCheck in ["F", "f"]:
            partySkills.kenSkills.remove(skillID.Sukunda)
            partySkills.kenSkills.remove(skillID.Masukunda)
            partySkills.kenSkills.remove(skillID.Primal_Force)
            partySkills.kenSkills.remove(skillID.Sanctify)
            partySkills.kenSkills.remove(skillID.Thunder_Reign)
            if kenLvl >= 41:
                partySkills.kenSkills.remove(skillID.Hama)
            if kenLvl >= 59:
                partySkills.kenSkills.remove(skillID.Cruel_Attack)
            if kenLvl not in range(51, 78):
                partySkills.kenSkills.remove(skillID.Mediarama)
            if kenLvl < 54:
                partySkills.kenSkills.remove(skillID.Hama_Boost)
            if kenLvl < 55:
                partySkills.kenSkills.remove(skillID.Ziodyne)
            if gameCheck in ["J", "j"]:
                if kenLvl not in range(37, 62):
                    partySkills.kenSkills.remove(skillID.Diarama)
                if kenLvl < 41:
                    partySkills.kenSkills.remove(skillID.Hamaon)
                if kenLvl not in range(42, 73):
                    partySkills.kenSkills.remove(skillID.Recarm)
                if kenLvl < 59:
                    partySkills.kenSkills.remove(skillID.Vile_Assault)
                if kenLvl < 62:
                    partySkills.kenSkills.remove(skillID.Diarahan)
                if kenLvl < 65:
                    partySkills.kenSkills.remove(skillID.Spear_Master)
                if kenLvl < 73:
                    partySkills.kenSkills.remove(skillID.Samarecarm)
                if kenLvl < 78:
                    partySkills.kenSkills.remove(skillID.Mediarahan)
            elif gameCheck in ["A", "a"]:
                if kenLvl not in range(29, 60):
                    partySkills.kenSkills.remove(skillID.Diarama)
                if kenLvl < 35:
                    partySkills.kenSkills.remove(skillID.Hamaon)
                if kenLvl not in range(32, 71):
                    partySkills.kenSkills.remove(skillID.Recarm)
                if kenLvl < 46:
                    partySkills.kenSkills.remove(skillID.Vile_Assault)
                if kenLvl < 60:
                    partySkills.kenSkills.remove(skillID.Diarahan)
                if kenLvl < 64:
                    partySkills.kenSkills.remove(skillID.Spear_Master)
                if kenLvl < 71:
                    partySkills.kenSkills.remove(skillID.Samarecarm)
                if kenLvl < 76:
                    partySkills.kenSkills.remove(skillID.Mediarahan)

        elif newMoonCheck in ["M", "m"]:
            partySkills.kenSkills.remove(skillID.Hama_Boost)
            if kenLvl >= 35:
                partySkills.kenSkills.remove(skillID.Hama)
            if kenLvl >= 46:
                partySkills.kenSkills.remove(skillID.Cruel_Attack)
            if kenLvl >= 42:
                partySkills.kenSkills.remove(skillID.Sukunda)
            if kenLvl >= 60:
                partySkills.kenSkills.remove(skillID.Diarama)
            if kenLvl not in range(35, 74):
                partySkills.kenSkills.remove(skillID.Hamaon)
            if kenLvl not in range(32, 71):
                partySkills.kenSkills.remove(skillID.Recarm)
            if kenLvl not in range(37, 76):
                partySkills.kenSkills.remove(skillID.Mediarama)
            if kenLvl < 42:
                partySkills.kenSkills.remove(skillID.Masukunda)
            if kenLvl not in range(55, 80):
                partySkills.kenSkills.remove(skillID.Ziodyne)
            if kenLvl not in range(46, 65):
                partySkills.kenSkills.remove(skillID.Vile_Assault)
            if kenLvl < 60:
                partySkills.kenSkills.remove(skillID.Diarahan)
            if kenLvl < 54:
                partySkills.kenSkills.remove(skillID.Spear_Master)
            if kenLvl < 65:
                partySkills.kenSkills.remove(skillID.Primal_Force)
            if kenLvl < 71:
                partySkills.kenSkills.remove(skillID.Samarecarm)
            if kenLvl < 74:
                partySkills.kenSkills.remove(skillID.Sanctify)
            if kenLvl < 76:
                partySkills.kenSkills.remove(skillID.Mediarahan)
            if kenLvl < 80:
                partySkills.kenSkills.remove(skillID.Thunder_Reign)

        if kenLvl >= 55:
            partySkills.kenSkills.remove(skillID.Zionga)

        count = 0
        while count < len(partySkills.kenSkills):
            if count == 0:
                pnach.write("\n\n//Ken skills")
            pnach.write("\n//Ken Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                        format(8607056 + (count * 2), "x") + ",short,0" + partySkills.kenSkills[count])
            count += 1

    # Shinjiro
    if gameCheck in ["J", "j"]:
        if shinjiroLvl != 0:
            if newMoonCheck in ["F", "f"]:
                partySkills.shinSkills.remove(skillID.Regenerate3)
                partySkills.shinSkills.remove(skillID.Phys_Skill_Up)
                if shinjiroLvl < 65:
                    partySkills.shinSkills.remove(skillID.Regenerate2)
            elif newMoonCheck in ["M", "m"]:
                if shinjiroLvl not in range(65, 75):
                    partySkills.shinSkills.remove(skillID.Regenerate2)
                if shinjiroLvl < 75:
                    partySkills.shinSkills.remove(skillID.Regenerate3)
                if shinjiroLvl < 80:
                    partySkills.shinSkills.remove(skillID.Phys_Skill_Up)

            if shinjiroLvl >= 65:
                partySkills.shinSkills.remove(skillID.Regenerate1)
            if shinjiroLvl >= 42:
                partySkills.shinSkills.remove(skillID.Counter)
            if shinjiroLvl >= 77:
                partySkills.shinSkills.remove(skillID.Fatal_End)
            if shinjiroLvl < 39:
                partySkills.shinSkills.remove(skillID.Evil_Smile)
            if shinjiroLvl not in range(42, 55):
                partySkills.shinSkills.remove(skillID.Counterstrike)
            if shinjiroLvl < 50:
                partySkills.shinSkills.remove(skillID.Power_Charge)
            if shinjiroLvl not in range(52, 60):
                partySkills.shinSkills.remove(skillID.Blade_of_Fury)
            if shinjiroLvl not in range(53, 72):
                partySkills.shinSkills.remove(skillID.Akasha_Arts)
            if shinjiroLvl < 55:
                partySkills.shinSkills.remove(skillID.High_Counter)
            if shinjiroLvl < 60:
                partySkills.shinSkills.remove(skillID.Deathbound)
            if shinjiroLvl < 77:
                partySkills.shinSkills.remove(skillID.Gods_Hand)

            count = 0
            while count < len(partySkills.shinSkills):
                if count == 0:
                    pnach.write("\n\n//Shinjiro skills")
                pnach.write("\n//Shinjiro Persona Skill " + (str(count + 1)).upper() + "\npatch=1,EE,00" +
                            format(8607924 + (count * 2), "x") + ",short,0" + partySkills.shinSkills[count])
                count += 1

# closing message
redundant_check = input("\nDone! Place in your cheats folder.")
