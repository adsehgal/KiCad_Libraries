import shutil, os
import re

print("\nStarting removing square pad 1 and replacing with circular")
### Horizontal 1x
string_p1 = "Custom_Horizontal_1x_1.27mm_Pin_Header.pretty/PinHeader_1x"
string_p2 = "_P1.27mm_Horizontal.kicad_mod"
for i in range(1, 41):
    with open(string_p1 + str(i).zfill(2) + string_p2, "r+") as f:
        text = f.read()
        text = re.sub("rect", "oval", text)
        f.seek(0)
        f.write(text)
        f.truncate()
print("Finished with Horizontal 1x__ headers")


# ### Vertical 1x
string_p1 = "Custom_Vertical_1x_1.27mm_Pin_Header.pretty/PinHeader_1x"
string_p2 = "_P1.27mm_Vertical.kicad_mod"
for i in range(1, 41):
    with open(string_p1 + str(i).zfill(2) + string_p2, "r+") as f:
        text = f.read()
        text = re.sub("rect", "oval", text)
        f.seek(0)
        f.write(text)
        f.truncate()
print("Finished with Vertical 1x__ headers")

### Horizontal 2x
string_p1 = "Custom_Horizontal_2x_1.27mm_Pin_Header.pretty/PinHeader_2x"
string_p2 = "_P1.27mm_Horizontal.kicad_mod"
for i in range(1, 41):
    with open(string_p1 + str(i).zfill(2) + string_p2, "r+") as f:
        text = f.read()
        text = re.sub("rect", "oval", text)
        f.seek(0)
        f.write(text)
        f.truncate()
print("Finished with Horizontal 2x__ headers")


# ### Vertical 2x
string_p1 = "Custom_Vertical_2x_1.27mm_Pin_Header.pretty/PinHeader_2x"
string_p2 = "_P1.27mm_Vertical.kicad_mod"
for i in range(1, 41):
    with open(string_p1 + str(i).zfill(2) + string_p2, "r+") as f:
        text = f.read()
        text = re.sub("rect", "oval", text)
        f.seek(0)
        f.write(text)
        f.truncate()
print("Finished with Vertical 2x__ headers")

print()
