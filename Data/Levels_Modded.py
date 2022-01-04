from Data.Levels_Unmodded import *

# Overwrites only the specific altered levels from Unmodded FES

yukari_Stats_mod = [
    (1, 1, 3, 2, 3, 1),   # +2 agi, -2 luc
    (2, 1, 1, 1, 1, 0),   # +1 agi
    (3, 0, 2, 1, 0, 1),   # +1 mag
    (4, 1, 1, 0, 2, 0),   # +1 agi
    (5, 2, 0, 0, 1, 1),   # +1 str
    (6, 0, 1, 0, 2, 1),   # +1 agi
    (7, 0, 1, 1, 1, 1),   # +1 luc
    (8, 1, 1, 1, 1, 0),   # +1 agi
    (9, 0, 1, 0, 1, 2),   # +1 agi
    (10, 1, 1, 1, 0, 1),  # +1 luc
    (11, 0, 1, 0, 2, 1),  # +1 luc
    (15, 0, 0, 0, 2, 1),  # +1 agi, -1 mag
    (18, 1, 1, 0, 1, 0),  # +1 agi, -1 luc
    (25, 0, 1, 1, 1, 0),  # +1 agi, -1 luc
    (36, 0, 1, 0, 2, 0),  # +1 agi, -1 str
    (52, 1, 0, 1, 1, 0)   # +1 agi, -1 mag
]

count = 0
for (Level, st, mag, vit, agi, luc) in yukari_Stats_mod:
    yukari_Stats[Level - 1] = yukari_Stats_mod[count]
    count += 1

junpei_Stats_mod = [
    (2, 1, 0, 1, 1, 1),   # +1 agi
    (3, 1, 1, 2, 0, 0),   # +1 end
    (4, 0, 1, 0, 1, 2),   # +1 luc
    (5, 1, 1, 1, 1, 0),   # +1 mag
    (6, 1, 0, 0, 2, 1),   # +1 agi
    (7, 1, 1, 1, 0, 1),   # +1 luc
    (8, 0, 0, 1, 2, 1),   # +1 agi
    (9, 1, 1, 2, 0, 0),   # +1 end
    (10, 1, 1, 0, 1, 1),  # +1 mag
    (11, 1, 0, 1, 1, 1),  # +1 luc
]

count = 0
for (Level, st, mag, vit, agi, luc) in junpei_Stats_mod:
    junpei_Stats[Level - 1] = junpei_Stats_mod[count]
    count += 1

akihiko_Stats_mod = [
    (1, 0, 0, 8, 4, 8),   # -2 str -2 mag +6 end +2 agi +6 luc
    (16, 0, 0, 1, 1, 1),  # -1 str, +1 end
    (27, 0, 0, 1, 1, 1),  # -1 mag, +1 end
    (35, 0, 0, 1, 1, 1),  # -1 mag, +1 luc
    (37, 0, 0, 1, 0, 1),  # -1 str, -1 mag, +2 luc
    (38, 1, 0, 1, 0, 1),  # -1 mag, +1 end
    (40, 0, 1, 0, 1, 1),  # -1 str, +1 luc
    (44, 0, 0, 1, 0, 2),  # -1 mag, +1 luc
    (47, 0, 0, 1, 1, 1),  # -1 mag, +1 end
    (48, 0, 1, 1, 0, 1),  # -1 str, +1 luc
    (54, 0, 1, 2, 0, 0),  # -1 str, +1 end
]

count = 0
for (Level, st, mag, vit, agi, luc) in akihiko_Stats_mod:
    akihiko_Stats[Level - 1] = akihiko_Stats_mod[count]
    count += 1

mitsuru_Stats[0] = (1, 2, 4, 7, 5, 2)   # +2 mag, +5 end, +3 agi

aigis_Stats[0] = (1, 5, 2, 3, 3, 7)   # +3 str, +1 end, +1 agi, +5 luc

koromaru_Stats[0] = (1, 4, 5, 2, 2, 7)   # +2 str, +3 mag, +5 luc

ken_Stats[0] = (1, 3, 2, 4, 4, 7)   # +1 str, +2 end, +2 agi, +5 luc

shinjiro_Stats[0] = (1, 6, 2, 3, 3, 6)   # +4 str, +1 end, +1 agi, +4 luc
