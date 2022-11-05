import re

def findDigit(line):
    #https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
    for count in re.findall(r'[-]*[\d]*[.][\d]+', line):
        #print(count)
        return(count)

#outputFloat = 2
def inputData(inputValue, outputFloat):
#with open('input.txt','r') as f:
    xValues = []
    yValues = []
    zValues = []
    #lines = f.readlines()
    lines = inputValue.splitlines()

    for line in lines:
        if 'X = ' in line:
            value = findDigit(line)
            if value is None:
                value = '0'
                xValues.append(value)
            else:
                xValues.append(str(round(float(value), outputFloat)))

        if 'Y = ' in line:
            value = findDigit(line)
            if value is None:
                value = '0'
                yValues.append(value)
            else:
                yValues.append(str(round(float(value), outputFloat)))

        if 'Z = ' in line:
            value = findDigit(line)
            if value is None:
                value = '0'
                zValues.append(value)
            else:
                zValues.append(str(round(float(value), outputFloat)))

    return('\n'.join(xValues), '\n'.join(yValues), '\n'.join(zValues))