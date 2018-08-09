print('''
               Welcome to the Cosmological Distance Calculator!''')
unit = "Mpc"
z = eval(input("Type in Redshift: "))
distance = z * (300000/74)
print( str(distance) + " in " + unit)
