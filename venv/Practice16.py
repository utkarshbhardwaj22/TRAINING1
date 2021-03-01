"""
Lists of lists
"""

pixel1 = [120,29,100]
pixel2 = [140,176,130]
pixel3 = [220,34,53]
pixel4 = [45,200,99]
pixel5 = [234,235,91]
pixel6 = [124,140,65]
pixel7 = [78,222,244]
pixel8 = [189,111,150]
pixel9 = [190,11,250]

image= [
    [pixel1,pixel2,pixel3],
    [pixel4,pixel5,pixel6],
    [pixel7,pixel8,pixel9]
]

for i in image:
    for j in i:
        j= sum(j)//3
            

