def getdata():
    months=int(input("ketna month work kiya:"))
    salary=float(input("ketni salary milte the:"))
    print(f"months={months}\n salary={salary}\ntotal={salary*months}\n\n")



user=int(input("input your data:"))
for i in range(1,user+1):
    getdata()
