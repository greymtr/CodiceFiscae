def tyl1(sname):
    consonants='bcdfghjklmnpqrstvwxyz'
    count=0
    sname=sname.lower()
    cons=""
    for x in sname:
        if x in consonants:
            count+=1
            cons=(cons+x)
    vowel='aeiou'
    v=''
    for y in sname:
        if y in vowel:
            v=(v+y)
    code=""  
    letters=0
    for z in sname:
        letters+=1
    if(letters<3):
        code=(cons+v+'X')
    elif(count>=3):
        code=cons[:3]
    elif(count<3):
        code=(cons+v[:(3-count)])
    code=code.upper()
    return code
