
import math 
z = float(input("ENTER Z: "))
x = float(input("ENTER X: "))
if ((z-(x**3)/3)==0) or (z*z-math.fabs(x**2/(z-(x**3)/3))==0):
    print("ERROR!")
else:
    y = (z+(x/(z*z-math.fabs(x**2/(z-(x**3)/3)))))
    print(y)

