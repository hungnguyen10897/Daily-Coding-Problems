
def countChange(money, coinList): # [3, 2, 1]
    """
    This function counts the number of different ways an amount of money can be exchanged,
    given a lst of coin denominations
    E.g: countChange(3,[2,1]) = 3 sice 3 can be exchanged with 1+1+1 or 2+1


    Parameters:
        money (int): The amount of money to be exchanged
        coinList (list[Int]): List of coin denominations
    """    
    def count(money, coinList, acc):
        if len(coinList) == 1:
            if money % coinList[0] == 0:
                return acc + 1
            else:
                return acc
        else:
            head = coinList[0] 
            surplus = money - head      
            if surplus < 0:
                return count(money, coinList[1:], acc)
            elif surplus == 0:
                return count(money, coinList[1:], acc + 1)
            else: 
                return count(money, coinList[1:], count(surplus, coinList, acc))
    return count(money, coinList, 0)

print(countChange(11, [8,7]))

