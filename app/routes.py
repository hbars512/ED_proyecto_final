from flask import render_template, url_for, request, redirect
from app import app
from app.graph_bridge import GraphBridge


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/bridges', methods=['GET', 'POST'])
def bridges():
    grafo1 = None
    if request.method == 'POST':
        nodos = int(request.form['num_nodos'])
        aristas = request.form['num_aristas']

        grafo1 = GraphBridge(nodos)
        for arista in aristas.split(', '):
            nodos = []
            for nodo in arista.split('-'):
                nodos.append(int(nodo))
            grafo1.addEdge(nodos[0], nodos[1])

        grafo1.bridge()

    return render_template('bridge.html', title='Proyecto ED', grafo=grafo1)
