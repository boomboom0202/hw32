import networkx as nx
import matplotlib.pyplot as plt

# Создаем граф
G = nx.Graph()

# Добавляем устройства в сеть
devices = {
    'PC1': {'type': 'PC'},
    'PC2': {'type': 'PC'},
    'Router1': {'type': 'Router'},
    'Router2': {'type': 'Router'},
    'Switch1': {'type': 'Switch'},
    'Switch2': {'type': 'Switch'},
    'Server1': {'type': 'Server'},
    'Printer1': {'type': 'Printer'},
    'Printer2': {'type': 'Printer'},
}

# Добавляем устройства в граф
for device, attr in devices.items():
    G.add_node(device, **attr)

# Добавляем связи между устройствами
connections = [
    ('PC1', 'Switch1', {'weight': 1}),
    ('PC2', 'Switch2', {'weight': 1}),
    ('Router1', 'Switch1', {'weight': 1}),
    ('Router1', 'Router2', {'weight': 2}),
    ('Router2', 'Switch2', {'weight': 1}),
    ('Switch1', 'Server1', {'weight': 1}),
    ('Switch2', 'Server1', {'weight': 1}),
    ('Switch1', 'Printer1', {'weight': 1}),
    ('Switch2', 'Printer2', {'weight': 1}),
]

G.add_edges_from(connections)

# Отрисовываем граф до оптимизации
plt.figure(figsize=(10, 5))
plt.subplot(121)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
plt.title("Network Topology (Before Optimization)")

# Рассчитываем кратчайший путь с использованием алгоритма Дейкстры
shortest_path = nx.shortest_path(G, weight='weight')

# Выводим результаты
print("Кратчайшие пути:")
for source, paths in shortest_path.items():
    for target, path in paths.items():
        if source != target:
            print(f"Из {source} в {target}: {' -> '.join(path)}")

# Отрисовываем граф после оптимизации
plt.subplot(122)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
plt.title("Network Topology (After Optimization)")

# Отображаем оба графика
plt.tight_layout()
plt.show()