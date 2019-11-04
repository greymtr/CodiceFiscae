def tyl3(d,m,y,gender):
    a=str(d)
    b=str(m)
    c=str(y)
    f=c[2:4]
    first = f

    if gender=='M':
        if(d<10):
            code=('0'+a)
        else:
            code=(a)
    else:
        temp=(40+d)
        code=str(temp)
    last = code
    Dict={1:'A',2:'B',3:'C',4:'D',5:'E',6:'H',7:'L',8:'M',9:'P',10:'R',11:'S',12:'T'}
    letter=Dict[m]
    mid=Dict[m]
    final = first+mid+last
    return final
