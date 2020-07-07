less=int(input())
more=int(input())
sleep=int(input())
if sleep>more:
    print("Excess")
elif more>=sleep>=less:
    print("Normal")
else:
    print("Deficiency")