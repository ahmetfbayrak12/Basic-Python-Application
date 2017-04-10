

def triangle(n):
    for i in range(1, n +1):
        print ("*" * i)

def square(a):
    for i in range(a):
        print ('*' * a)

def rectangle(row_count, coloumn_count):
   for row in range(row_count):
      for col in range(coloumn_count):
         print "*",
      print

def quitcont(n):
    if n == "E" or n == "e":
        quit()
    else:
        return menu(n)

def menu(n):
    menum = raw_input("Please press T for Triangle: \nPlease press S for Square: \nPlease press R for Rectangle: \n")
    if menum == "T" or menum == "t":
        tr_value = input("Please enter value of row count: \n")
        triangle(tr_value)
    elif menum == "S" or menum == "s":
        kr_value = input("Please enter value of row count \n")
        square(kr_value)

    elif menum == "R" or menum == "r":
        ddk_value = input("Please enter value of coloumn count: \n")
        ddu_value = input("Please enter value of row count: \n")
        rectangle(ddu_value, ddk_value)
    qcont = raw_input("Please press Enter for New Calculation: \nPlease press E for exit: \n")
    quitcont(qcont)
menu("s")

