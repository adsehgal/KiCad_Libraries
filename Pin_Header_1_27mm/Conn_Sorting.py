import shutil, os

# ### SMD_Pin1Right
string_p1 = "PinHeader_1x"
string_p2 = "_P1.27mm_Vertical_SMD_Pin1Right.kicad_mod"

for i in range(2, 41):
    files = string_p1 + str(i).zfill(2) + string_p2
    shutil.move(files, "Vertical_SMD_Pin1Right")
    print(files)

# ### SMD_Pin1Left
string_p1 = "PinHeader_1x"
string_p2 = "_P1.27mm_Vertical_SMD_Pin1Left.kicad_mod"

for i in range(2, 41):
    files = string_p1 + str(i).zfill(2) + string_p2
    shutil.move(files, "Vertical_SMD_Pin1Left")
    print(files)

# ### Horizontal 1x
string_p1 = "PinHeader_1x"
string_p2 = "_P1.27mm_Horizontal.kicad_mod"

for i in range(1, 41):
    files = string_p1 + str(i).zfill(2) + string_p2
    shutil.move(files, "Custom_Horizontal_1x_1.27mm_Pin_Header.pretty")
    print(files)

# ### Vertical 1x
string_p1 = "PinHeader_1x"
string_p2 = "_P1.27mm_Vertical.kicad_mod"

for i in range(1, 41):
    files = string_p1 + str(i).zfill(2) + string_p2
    shutil.move(files, "Custom_Vertical_1x_1.27mm_Pin_Header.pretty")
    print(files)

# ### Horizontal 2x
string_p1 = "PinHeader_2x"
string_p2 = "_P1.27mm_Horizontal.kicad_mod"

for i in range(1, 41):
    files = string_p1 + str(i).zfill(2) + string_p2
    shutil.move(files, "Custom_Horizontal_2x_1.27mm_Pin_Header.pretty")
    print(files)

# ### Vertical 2x
string_p1 = "PinHeader_2x"
string_p2 = "_P1.27mm_Vertical.kicad_mod"

for i in range(1, 41):
    files = string_p1 + str(i).zfill(2) + string_p2
    shutil.move(files, "Custom_Vertical_2x_1.27mm_Pin_Header.pretty")
    print(files)

# ### Vertical 2x
string_p1 = "PinHeader_2x"
string_p2 = "_P1.27mm_Vertical_SMD.kicad_mod"

for i in range(1, 41):
    files = string_p1 + str(i).zfill(2) + string_p2
    shutil.move(files, "VerticalSMD")
    print(files)
