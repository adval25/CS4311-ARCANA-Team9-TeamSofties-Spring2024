from dash import Dash, html
import dash_cytoscape as cyto

app = Dash(__name__)

directed_edges = [
    {'data': {'id': src+tgt, 'source': src, 'target': tgt}}
    for src, tgt in ['BA', 'BC', 'CD', 'DA']
]

directed_elements = [{'data': {'id': id_}} for id_ in 'ABCD'] + directed_edges
print(directed_edges)

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-styling-9',
        layout={'name': 'circle'},
        style={'width': '100%', 'height': '400px'},
        elements=directed_elements,
        stylesheet=[
            {
                'selector': 'node',
                'style': {
                    'label': 'data(id)'
                    
                }
            },
            {
                'selector': 'edge',
                'style': {
                    'line-color': 'red',  # Apply the same line color to all edges
                    'target-arrow-color': 'blue',  # Apply arrow color
                    'target-arrow-shape': 'triangle',  # Apply arrow shape
                    'curve-style': 'bezier'  # Adjust curve style if needed
                }
            }
        ]
    )
])

if __name__ == '__main__':
    app.run(debug=True)
