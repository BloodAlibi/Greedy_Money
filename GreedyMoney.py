# BloodAlibi // 2023

values = [1,2,5,10,20,50,100] # Change the chosen values here

def greedy_aglorithm(number, system):
    if number<=0: return "Impossible - Number is below or equal to 0. Impossible."
    result=[]
    i=len(system)-1
    while number>0:
        if number-system[i]>=0:
            number-=system[i]
            result.append(system[i])
        else:
            if i<0:
                return "Impossible - Values of system can't solve the chosen number."
            i-=1
    return result

print("Welcome to Greedy Money. You will be able of decomposing a specific number with the least chosen values. For real life instance, this method can be used to pay with the least amount of cash/coins a specific amount (example: 78€ => 50€ + 20€ + 5€ + 2€ + 1€).")

while True:
    num=int(input("\n--------------------------\nPick a number above 0.\n>>>\t"))
    print("*", num," ==> ", greedy_aglorithm(num, values))
