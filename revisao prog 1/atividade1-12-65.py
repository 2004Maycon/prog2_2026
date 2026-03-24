def main():
    n=int(input("quantas cordenadas sera incerida? "))
    totalx = 0
    totaly=0
    totalx2=0
    totaly2=0
    totalxy=0
    for i in range(n):
        x=float(input("digite o primeiro valor "))
        y=float(input("digite o primeiro valor "))
        totalx+=x
        totaly+=y
        totalx2+= x**2
        totaly2+= y**2
        totalxy+= y*x
        print("-"*35)
    infA=((n*totalxy)-(totalx*totaly))
    supA=(n*totalx2)-(totalx)**2
    A=infA/supA
    print(infA,supA,A)
    print("-"*35)
    infB=(totaly*totalx2)-(totalx*totalxy)
    B=infB/supA
    print(infB,supA,B)
    print("-"*35)
    supR=(n*totalxy)-(totalx*totaly)
    infR=(n*totaly2)-(totaly)**2
    R=supR/(infR*supA)**0.5
    print(infR,supR,R)
    print("-"*35)
    print(f"parte de cima {A}")
    print("-"*35)
    print(f"parte de baixo {B:.2f}")
    print("-"*35)
    print(f"resultado  {R}")
main()