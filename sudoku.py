matriz = [  ["*", "*", "*", "*", "*", "*", "*", "*", "*",],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*",],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*",],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*",],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*",],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*",],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*",],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*",],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*",] ]

def lerInstanciaSudoku():
    print()
    print("Instância Sudoku:")
    print("  a b c d e f g h i")
    for i in range(9):
        l = input(chr(ord("A") + i) + " ").split()
        for j in range(9):
            matriz[i][j] = l[j]

def verificaFim(matriz, l, c):
    pass

def verificaLinha(matriz, l, c, v):
    for i in range(9):
        if i != c and matriz[l][i] == v:
            return False
    return True

def verificaColuna(matriz, l, c, v):
    for i in range(9):
        if i != l and matriz[i][c] == v:
            return False
    return True

def verificaQuadrante(matriz, l, c, v):
    l_quad = int(l / 3) * 3
    c_quad = int(c / 3) * 3
    for i in range(l_quad, l_quad + 3):
        for j in range(c_quad, c_quad + 3):
            if (i != l or j != c) and matriz[i][j] == v:
                return False
    return True

def exibirSudoku():
    print()
    print("   a b c  d e f  g h i")
    print()
    for linha in range(9):
        print(chr(ord("A") + linha) + " ", end=" ")
    
        for coluna in range(9):
            print(matriz[linha][coluna] + " ", end="")
            if (coluna + 1) % 3 == 0:
                print(" ", end="")
        print()
        if (linha + 1) % 3 == 0:
            print()

def lerValor():
    exibirSudoku()
    l, c, valor = input("Linha, coluna, valor: ").split()
    linha = ord(l) - ord("A")
    coluna = ord(c) - ord("a")
    
    if 0 <= linha <= 8:
        if 0 <= coluna <= 8:
            if ord("1") <= ord(valor) <= ord("9") or valor == "*":
                   return True, linha, coluna, valor
            else:
                print("Valor Inválido!")
                return False, 0, 0, ""
        else:
            print("Coluna Inválida!")
            return False, 0, 0, ""
    else:
        print("Linha Inválida!")
        return False, 0, 0, ""


lerInstanciaSudoku()
leituraValida = False
while not leituraValida:
    leituraValida, linha, coluna , valor = lerValor()
    if leituraValida:
        if verificaLinha(matriz, linha, coluna, valor):
            if verificaColuna(matriz, linha, coluna, valor):
                if verificaQuadrante(matriz, linha, coluna, valor):
                    matriz[linha][coluna] = valor
                    leituraValida = False
                else:
                    print("Valor Inválido! (Quadrante)")
                    leituraValida = False
            else:
                print("Valor Inválido! (Coluna)")
                leituraValida = False
        else:
            print("Valor Inválido! (Linha)")
            leituraValida = False
exibirSudoku()