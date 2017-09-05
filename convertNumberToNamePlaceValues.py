import re

# input question
str = "There are 12345 stars in mars"


# Assign positions to numbers in the string
def getNumberPositions(str) :
    # convert the list into array of charactersd
    liststr = list(str)
    # the final value to be returned
    arr = {"str" : str, "val" : []}
    prevCharSpace = []
    index = 0
    # iterate
    for char in liststr:
        # length pf array
        lenArr = len (arr['val'])

        # check if the previous character was a number and the current character is an alphabet.
        # if yes, then we set the flag in previous char data
        if lenArr > 0 and char.isalpha() and (index - (arr['val'][lenArr-1]["startIndex"] + len(arr['val'][lenArr-1]["val"]) -1) == 1):
            arr['val'][lenArr-1]["nextCharSpace"] = 1

        # check if current char is digit
        if char.isdigit():
            # if the previous char was a digit and current is also digit
            # we append the two to make whole number

            if lenArr > 0 and (index - (arr['val'][lenArr-1]["startIndex"] + len(arr['val'][lenArr-1]["val"]) -1) ==1):
                arr['val'][lenArr-1]["val"] = arr['val'][lenArr-1]["val"]+ char
            # check if previous char was alphabet and current is digit
            # if yes, then set the flag along with data
            elif len(prevCharSpace) > 0 and prevCharSpace[1] == 1 and (index - prevCharSpace[0] == 1):
                arr['val'].append({"startIndex" : index, "prevCharSpace" : 1, "nextCharSpace" : 0, "val" : char})
            else :
                arr['val'].append({"startIndex" : index, "prevCharSpace" : 0, "nextCharSpace" : 0, "val" : char})

        # check if current char is alphabet, and set the flag in variable
        if char.isalpha() :
            prevCharSpace = [index, 1]
        else :
            prevCharSpace = []
        # increment index
        index = index +1
    #return final data
    return arr

# function converts number into place value names and returns it
def getPlaceValueName(numberStr, res) :

    if isinstance(numberStr, int) or (numberStr.isdigit()) :
        singles = ["ZERO", "ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]

        doubles = ["TEN","ELEVEN","TWELVE","THIRTEEN","FOURTEEN","FIFTEEN","SIXTEEN", "SEVENTEEN","EIGHTEEN","NINTEEN"]

        tens = ["TEN","TWENTY","THIRTY","FOURTY","FIFTY","SIXTY","SEVENTY", "EIGHTY","NINTY"]

        no = int(numberStr)

        if no >= 100000 :
            t = no/ 100000
            if (t >= 10) :
                res = getPlaceValueName(t, res)
            else :
                res.append(singles[t])
            res.append("LAKH")
            no = no%100000
            res = getPlaceValueName(no, res)
            return res
        if no > 1000 :
            t=no/1000
            if (t >= 10 ) :
                res = getPlaceValueName(t, res)
            elif (t < 10):
                res.append(singles[t])
            res.append("THOUSAND")
            no = no%1000
            res = getPlaceValueName(no, res)
            return res
        if no>100 :
            t=no/100
            res.append(singles[t])
            res.append("HUNDRED AND")
            no=no%100
            if (no > 0) :
                res = getPlaceValueName(no, res)
            return res
        if no >= 10 and no < 20 :
            t=no%10
            res.append(doubles[t])
            return res
        if (no>19 and no<=100) :
            t=no/10
            res.append(tens[t-1])
            no=no%10
            if (no > 0) :
                res = getPlaceValueName(no, res)
            return res
        if (no<10) :
            res.append(singles[no])
            return res


def getStringUtterance(values) :
    #  get the string
    str = values['str']
    nameStr = ""
    # legth of string
    strlen = len(str)
    # starting index
    startIndex = 0
    # iterate
    for index, value in enumerate(values['val']) :
        # value to be appended
        valToAppend = ""
        # Set the string
        nameStr +=  str[startIndex:value["startIndex"]]
        # check if prev character was a alphabet, and if yes then add a space
        if (value["prevCharSpace"] == 1) :
            valToAppend += " "
        # set the string value of number
        valToAppend += value["strVal"]

        # check if next character was a alphabet, and if yes then add a space
        if (value["nextCharSpace"] == 1) :
            valToAppend += " "
        # add value to string
        nameStr += valToAppend
        # set the new index, i.e previous number staring index added with length of the number
        startIndex = value["startIndex"]+len(value["val"])

    # add the remaining string
    nameStr += str[startIndex:strlen]
    # return
    return nameStr



def init() :
    # get number positions of a given string
    values = getNumberPositions(str)

    # iterate over numbers
    for index, value in enumerate(values['val']) :
        # get place value name in list
        res = getPlaceValueName(value["val"], [])
        # join  with space
        res = " ".join(res)
        # set it in data
        values['val'][index]['strVal'] = res

    # replace the numbers with string equivalents
    strVal = getStringUtterance(values)
    print strVal

# initiate
init()
