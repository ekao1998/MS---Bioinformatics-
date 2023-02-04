# To calculate the dominant --> 1 - the rate of recessive
x=24
y=29
z=23
total = x+y+z
TotalCombimation = (total*(total-1)/2) * 4 # C6 pick 2 * 4 combination example:Aa x Aa 4 ans

##calculate recessive

# Y x Z Aa x aa
cal_YZ = (y*z) * 2 # 2 possible combinaiton for recessive

# Z x Z aa x aa
cal_ZZ = (z * (z-1)/2) * 4 # from group z ramdomly pick 2, 4 possible combination for recessive

# Y x Y Aa x Aa
Cal_YY = (y * (y-1)/2) * 1 # from group y ramdomly pick 2, 1 possible combination for recessive

## calculate dominant
Ans = 1 - ((cal_YZ + cal_ZZ + Cal_YY) / TotalCombimation)
print(Ans)