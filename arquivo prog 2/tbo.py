import time
def asteriscos(lst):
    for i in range(len(lst)):
        print("s2", end="")
    print()
def sortbolha(l):
    trocou = True
    while trocou == True:
        trocou = False
        for i in range (len(l)-1):
            if l[i]>l[i+1]:
                aux= l[i]
                l[i]=l[i+1]
                l[i+1]=aux
                trocou = True
                time.sleep(0.1)
                print(chr(27)+'[2j')
                print(chr(27)+'[1;1h')
                asteriscos(l)
    return l

def main():
    #print(chr(27)+'[23')
    lst=[11,13,3,18,20,6,16,9,15,2,14,5,4,8,10,19,17,1,7,12]
    lst= sortbolha(lst)

if __name__ == "__main__":
    main()
