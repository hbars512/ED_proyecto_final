from flask import render_template
from app import app
from app.graph_bridge import GraphBridge


@app.route('/')
@app.route('/index')
def index():
    grafo1 = GraphBridge(5)
    grafo1.addEdge(1, 0)
    grafo1.addEdge(0, 2)
    grafo1.addEdge(2, 1)
    grafo1.addEdge(0, 3)
    grafo1.addEdge(3, 4)
    grafo1.bridge()

    return render_template('index.html', title='Proyecto ED', grafo=grafo1)
