# Dominio y restricciones
dominios = {
    'X1': [1, 2, 3, 4],
    'X2': ['a', 'b', 'c'],
    'X3': ['α', 'β', 'γ']
}

restricciones = {
    ('X1', 'X2'): {(1,'a'), (2,'b'), (3,'a'), (3,'b'), (4,'b')},
    ('X1', 'X3'): {(1,'β'), (3,'β'), (4,'β')},
    ('X2', 'X3'): {('a','γ'), ('b','β'), ('b','α'), ('c','γ')}
}

asignacion = {}
soluciones = []

def consistente(var, val):
    # Chequear cada restricción entre `var` y variables ya asignadas
    for v_asig, val_asig in asignacion.items():
        par = (v_asig, var) if (v_asig, var) in restricciones else (var, v_asig)
        if par in restricciones:
            if par == (v_asig, var):
                if (val_asig, val) not in restricciones[par]:
                    return False
            else:
                if (val, val_asig) not in restricciones[par]:
                    return False
    return True

def backtrack(vars_por_asignar):
    if not vars_por_asignar:
        soluciones.append(asignacion.copy())
        return
    X = vars_por_asignar[0]
    for valor in dominios[X]:
        if consistente(X, valor):
            asignacion[X] = valor
            backtrack(vars_por_asignar[1:])
            del asignacion[X]

# Ejecutar búsqueda
backtrack(['X1','X2','X3'])

# Mostrar soluciones
for sol in soluciones:
    print(sol)
