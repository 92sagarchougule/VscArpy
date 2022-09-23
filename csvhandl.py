import csv

with open("D:\\DataforArcObject\\Shingtaluru_Data.csv",'w') as f:
    w = csv.writer(f)
    w.writerow(['ENO','ENAME','EADD'])
    while True:
        eno = int(input('Enter a number :'))
        ename = input('Enter a Name :')
        Edd = input('Enter a Address :')

        w.writerow([eno,ename,Edd])
        option = input('Yes of no')

        if(option.lower() == 'no'):
            break
    


    


