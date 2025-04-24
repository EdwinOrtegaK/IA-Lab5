# --------- definición del árbol ---------
tree = {
    'root': ['A', 'B', 'C'],
    'A': [5, 2, 3],
    'B': [1, 2, 3],
    'C': [4, 0, 5]
}
is_max = {            # True = MAX, False = MIN
    'root': True,
    'A': False,
    'B': False,
    'C': False
}

# ============ MINIMAX PURO ============ #
def minimax(node, depth=0, stats=None):
    indent = "  " * depth
    if isinstance(node, int):                 # hoja
        print(f"{indent}- hoja {node}")
        stats['leaves'] += 1
        return node

    print(f"{indent}{'MAX' if is_max[node] else 'MIN'} {node}")
    children = tree[node]
    values = []

    for ch in children:
        val = minimax(ch, depth + 1, stats)
        values.append(val)

    res = max(values) if is_max[node] else min(values)
    print(f"{indent}→ valor de {node} = {res}")
    return res


# ============ ALFA-BETA ============ #
def alphabeta(node, alpha=-float('inf'), beta=float('inf'),
              depth=0, stats=None):
    indent = "  " * depth
    if isinstance(node, int):                 # hoja
        print(f"{indent}- hoja {node}")
        stats['leaves'] += 1
        return node

    print(f"{indent}{'MAX' if is_max[node] else 'MIN'} {node}  "
          f"(α={alpha}, β={beta})")
    children = tree[node]

    if is_max[node]:                          # --- MAX ---
        value = -float('inf')
        for ch in children:
            val = alphabeta(ch, alpha, beta, depth + 1, stats)
            value = max(value, val)
            alpha = max(alpha, value)
            if beta <= alpha:                 # poda
                podadas = len(children) - children.index(ch) - 1
                stats['pruned'] += podadas
                print(f"{indent}**poda {podadas} rama(s)")
                break
        print(f"{indent}→ valor de {node} = {value}")
        return value
    else:                                     # --- MIN ---
        value = float('inf')
        for ch in children:
            val = alphabeta(ch, alpha, beta, depth + 1, stats)
            value = min(value, val)
            beta = min(beta, value)
            if beta <= alpha:                 # poda
                podadas = len(children) - children.index(ch) - 1
                stats['pruned'] += podadas
                print(f"{indent}**poda {podadas} rama(s)")
                break
        print(f"{indent}→ valor de {node} = {value}")
        return value


# ------------- EJECUCIÓN -------------
print("=== Minimax clásico ===")
stats_mm = {'leaves': 0, 'pruned': 0}
val_mm = minimax('root', stats=stats_mm)
print(f"\nResultado Minimax: valor raíz = {val_mm}")
print(f"Hojas evaluadas = {stats_mm['leaves']}\n")

print("=== Minimax con poda α-β ===")
stats_ab = {'leaves': 0, 'pruned': 0}
val_ab = alphabeta('root', stats=stats_ab)
print(f"\nResultado α-β  : valor raíz = {val_ab}")
print(f"Hojas evaluadas = {stats_ab['leaves']}")
print(f"Hojas podadas   = {stats_ab['pruned']}")