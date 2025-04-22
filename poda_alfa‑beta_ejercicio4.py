# Representación del árbol del Ejercicio 4:
# Cada nodo es una lista de sus hijos; las hojas son enteros.
tree = [
    # Subárbol izquierdo de la raíz (Min₂ convertido vía Negamax)
    [
        # M₁
        [
            # m₁₁
            [-2, 4],
            # m₁₂
            [6, -8]
        ],
        # M₂
        [
            # m₂₁
            [-3, -1],
            # m₂₂
            [7, -5]
        ]
    ],
    # Subárbol derecho de la raíz
    [
        # M₃
        [
            # m₃₁
            [2, -4],
            # m₃₂
            [-6, 8]
        ],
        # M₄
        [
            # m₄₁
            [3, 1],
            # m₄₂
            [-7, 5]
        ]
    ]
]

def negamax(node, alpha, beta, color):
    """
    Negamax con poda α–β.
    - node: lista (interno) o entero (hoja)
    - alpha, beta: valores de poda
    - color: +1 para Max, -1 para Min
    Devuelve: mejor valor (desde la perspectiva del color positivo).
    """
    # Caso base: hoja
    if isinstance(node, int):
        return color * node

    best_val = float('-inf')
    for child in node:
        # Negamos color y roles de alpha/beta
        val = -negamax(child, -beta, -alpha, -color)
        best_val = max(best_val, val)
        alpha = max(alpha, best_val)
        if alpha >= beta:
            # Poda beta
            break
    return best_val

# Para determinar la mejor acción en la raíz, probamos cada hijo:
alpha, beta = float('-inf'), float('inf')
best_value = float('-inf')
best_action = None

for i, child in enumerate(tree):
    val = -negamax(child, -beta, -alpha, -1)  # color = -1 porque la raíz es Max
    if val > best_value:
        best_value = val
        best_action = i  # 0 = izquierda, 1 = derecha
    alpha = max(alpha, val)

print(f"Valor óptimo en la raíz: {best_value}")
print(f"Mejor acción en la raíz: ir al subárbol {'izquierdo' if best_action==0 else 'derecho'}")
