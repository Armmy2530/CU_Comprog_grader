def total(pocket):
    return sum(x*y for x,y in pocket.items())
def take(pocket, money_in):
    for key, value in money_in.items():
        if key in pocket.keys():
            pocket[key] += value
        else:
            pocket[key] = value
def pay(pocket, amt):
    found = False
    money_out = {}
    while amt != 0:
        for i in pocket.keys():
            if i <= amt and pocket[i] != 0:
                amt -= i
                pocket[i] -= 1
                if(i in money_out.keys()):
                    money_out[i] += 1
                else:
                    money_out[i] = 1
                found = True
                break
        if not(found):
            for i in money_out:
                pocket[i] += money_out[i]
            return {}
        else:
            found = False
    return money_out
exec(input().strip())
