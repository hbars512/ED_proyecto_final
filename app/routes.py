from flask import render_template, url_for, request
from app import app
from app.graph_bridge import GraphBridge
from app.graph_cycles import GraphCycles
import numpy as np
from time import time


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/bridges', methods=['GET', 'POST'])
def bridges():
    grafo1 = None
    if request.method == 'POST':
        n_nodos = int(request.form['num_nodos'])
        aristas = request.form['num_aristas']

        start_time = time()
        grafo1 = GraphBridge(n_nodos)
        for arista in aristas.split(', '):
            nodos = []
            for nodo in arista.split('-'):
                nodos.append(int(nodo))
            grafo1.addEdge(nodos[0], nodos[1])

        grafo1.bridge()
        elapsed_time = time() - start_time
        return render_template(
            'bridge.html',
            title='Proyecto ED',
            grafo=grafo1,
            ar=aristas,
            numero_nodos=n_nodos,
            elapsed_time=elapsed_time
        )

    return render_template('bridge.html', title='Proyecto ED', grafo=grafo1)


@app.route('/cycles', methods=['GET', 'POST'])
def cycles():
    if request.method == 'POST':
        n_nodos = int(request.form['num_nodos'])
        aristas = request.form['aristas']
        n_ciclos = int(request.form['n_ciclos'])

        nodos = []
        for arista in aristas.split(', '):
            row_nodos = []
            for nodo in arista.split('-'):
                row_nodos.append(int(nodo))
            nodos.append(row_nodos)

        graph = np.zeros((n_nodos, n_nodos))
        for i in range(n_nodos):
            for j in range(n_nodos):
                if [i, j] in nodos:
                    graph[i][j] = 1
                    graph[j][i] = 1

        start_time = time()
        grafo1 = GraphCycles(n_nodos, graph)
        num_ciclos = grafo1.count_cycles(n_ciclos)
        elapsed_time = time() - start_time

        return render_template(
            'cycles.html',
            title='Proyecto ED',
            aristas=aristas,
            n_ciclos=n_ciclos,
            num_ciclos=num_ciclos,
            numero_nodos=n_nodos,
            elapsed_time=elapsed_time
        )

    return render_template('cycles.html')
