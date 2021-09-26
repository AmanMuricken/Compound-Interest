#Amount = principle * (pow((1 + rate / 100), time))
#CI = Amount - principle

def compoundInterest(p,r,t):
    a=p*(pow((1+r/100),t))
    ci=a-p
    print("The compoundInterest is:",ci)
    return ci

p=float(input("Enter the value for principle:"))
r=float(input("Enter the value for rate:"))
t=float(input("Enter the value for time:"))

compoundInterest(p,r,t)

   
