from num import numtotext

def wrt(i):
    text = ""
    for j in i:
        try:
            j = int(j)
            text = text + ":" + numtotext(int(j)) + ":" + " "
        except ValueError:
            if(j == " " or j == ""):
                text = text + " "
            elif(j == "#"):
                text = text + ":hash:" 
            else:
                text = text + ":regional_indicator_" + j + ":" + " "
    return text

def uinput(n):
    i = []
    for j in n:
        i.append(j.lower())
    return i
