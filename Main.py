status=input()
revenue=input()
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
