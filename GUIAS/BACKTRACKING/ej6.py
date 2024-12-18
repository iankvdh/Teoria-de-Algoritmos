import sys

def fila(cant_elem):
    return cant_elem // 9

def columna(cant_elem):
    return cant_elem % 9

# Funcio que verifica si puede poner el numero pasado (num) en la posicion pasado (cant_elem)
def puedo_poner(num, cant_elem, M):
    # Se fija si no esta el mismo numero en la fila
    fil = fila(cant_elem)
    for c in range(0, 9):
        if M[fil][c] == num:
            return False

    # Se fija si no esta el mismo numero en la columna
    col = columna(cant_elem)
    for f in range(0, 9):
        if M[f][col] == num:
            return False

    # Se fija si no esta el mismo numero en el cuadrante
    c_corner = (col // 3) * 3
    f_corner = (fil // 3) * 3
    for f_c in range(f_corner, f_corner + 3):
        for c_c in range(c_corner, c_corner + 3):
            if M[f_c][c_c] == num:
                return False
    return True

def sig_pos_a_usar(cant_elem, M):
    for x in range(cant_elem, 9 * 9):
        if M[fila(x)][columna(x)] == 0:
            return x
    return 9 * 9

def sudoku_solver(M):
    sudoku(0, M)
    return M

# Funcion backtraking sudoku
def sudoku(cant_elem, M):
    if cant_elem >= 9 * 9:
        return True

    cant_elem = sig_pos_a_usar(cant_elem, M)
    
    if cant_elem >= 9 * 9:
        return True
    
    for num in range (1, 10):
        if puedo_poner(num, cant_elem, M):
            M[fila(cant_elem)][columna(cant_elem)] = num
            if sudoku(cant_elem, M):
                return True
            M[fila(cant_elem)][columna(cant_elem)] = 0

    return False
