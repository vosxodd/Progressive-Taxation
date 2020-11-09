

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
