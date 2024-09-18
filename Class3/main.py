# Recursividade
# É uma função que chama ela mesma
# fatorial(1) =  1
# fatorail(2) =  2 * 1
# fatorial (3) = 3 * 2 * 1


# num  = 3 =  =  3 * fatorial(2) = 2
# num  = 2 = = 2 * fatorial(1)
# num = 1 =  1

import fat as ft


def main():
    num = int(input("Insira um número: "))
    word = str(input("Digite uma palavara: "))

    ans = ft.fatorial(num)
    print(f"fatorial: {ans}")
    print(f'A contagem da vogal 1 : {ft.count_vogal(word)}')
    print(f'A contagem de vogal 2 : {ft.count_vogal2(word)}')


if __name__ == "__main__":
    main()
