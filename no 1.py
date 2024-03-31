#soal no 1

#1 2 3 4 5
#2 4 6 8 10
#3 6 9 12 15 
#4 8 12 16 20
#5 10 15 20 25 

row = 6
col = 6

for i in range (1 , row):
    for f in range (1 ,col):
        print (f * i, end=" ")
    print ()
