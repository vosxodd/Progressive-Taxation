status=input()
revenue=int(input())
if status=="родитель-одиночка":
    if 0<=revenue<=12950:
        print(0.1*revenue)
    elif 12951<=revenue<=49400:
        print(0.15*revenue)
    elif 49401<=revenue<=127550:
        print(0.25*revenue)
    elif 127551<=revenue<=206600:
        print(0.28*revenue)
    elif 206601<=revenue<=405100:
        print(0.33*revenue)
    elif 405101<=revenue<=432200:
        print(0.35*revenue)
    elif 432201<=revenue:
        print(0.396*revenue)
        
       
if status=="один субъект":
    if 0<=revenue<=9075:
        tax=0.1*revenue
    elif 9076<=revenue<=36900:
        tax=0.15*revenue
    elif 36901 <= revenue <= 89350:
        tax = 0.25 * revenue
    elif 89351 <= revenue <= 186350:
        tax = 0.28 * revenue
    elif 186351 <= revenue <= 405100:
        tax = 0.33 * revenue
    elif 405101 <= revenue <= 406750:
        tax = 0.35 * revenue
    elif 406751 <= revenue:
        tax = 0.396 * revenue
        
        
if status == 'для супружеской пары':
    if 0<=revenue<=18150:
        print(0.1*revenue)
    elif 18151<=revenue<=73800:
        print(0.15*revenue)
    elif 73801<=revenue<=148850:
        print(0.25*revenue)
    elif 148851<=revenue<=226850:
        print(0.28*revenue)
    elif 226851<=revenue<=405100:
        print(0.33*revenue)
    elif 405101<=revenue<=457600:
        print(0.35*revenue)
    elif 457601<=revenue:
        print(0.396*revenue)
