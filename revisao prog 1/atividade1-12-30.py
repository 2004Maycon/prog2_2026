def main():
    A =0.0
    while A <= 6.3:
        T1 = A
        T2 = A**3/6
        T3 = A**5/120
        T4 = A**7/5040
        sen_A=T1-T2+T3-T4
        print(f"{'Ângulo (A)':<12} | {'Seno Aproximado':<18}")
        print(f'{A:.1f}| {sen_A:18.6f}')
        print("-" * 35)
        A = A+0.1
main()