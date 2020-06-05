import shutil, os
import re

##########################################################################################
#### This script writes kicad footprints to create castellations with a pitch of 1.0mm ###
#### and 0.6mm diameter holes. The number of iterations (i) determines the number of   ###
#### files and the file number defines the number of pads created in that file.        ###
##########################################################################################

print("\nStarting creation of footprints")
### Horizontal 1x
string_p1 = "1x"
string_p2 = "_1.0mm_Castellations.kicad_mod"

string_text1 = '(module "1x'
# file number goes here(i)
string_text2 = '_1.0mm_Castellations" (layer F.Cu) (tedit 5EDA4C3A)\n\
  (fp_text reference "REF**" (at 0 -0.5 unlocked) (layer F.SilkS)\n\
    (effects (font (size 1 1) (thickness 0.15)))\n\
  )\n\
  (fp_text value "1x'
# file number goes here(i)
string_text3 = '_1.0mm_Castellations" (at 0 1 unlocked) (layer F.Fab)\n\
    (effects (font (size 1 1) (thickness 0.15)))\n\
  )\n'
# add footprints here (inner loop)
string_text4 = '(pad "'
# pad number goes here (j)
string_text5 = '" thru_hole roundrect (at '
# pad distance goes here (j-1)
string_text6 = " 0) (size 0.62 1) (drill 0.6 (offset 0 -0.2)) (layers *.Cu *.Mask) (roundrect_rratio 0.25) (tstamp 9bad289e-ae9f-484c-9112-4ab7218ffcb1))\n"

for i in range(1, 41):
    with open(string_p1 + str(i) + string_p2, "w") as f:
        f.write(string_text1)
        f.write(str(i))
        f.write(string_text2)
        f.write(str(i))
        f.write(string_text3)
        for j in range(1, i + 1):
            f.write(string_text4)
            f.write(str(j))
            f.write(string_text5)
            f.write(str(j - 1))
            f.write(string_text6)
        f.write(")")
        f.close()
print("Finished creating all files")
