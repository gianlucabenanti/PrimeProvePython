from FMDBC import FMDBC as F

row = F().select("test","Cod='C058'","Txt")

x = F().select("test","Cod='C069'","Txt")

print(row,x)