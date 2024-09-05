import os
from flask import Flask, request, render_template
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

def create_budget_sankey_diagram(df, source_col='source_category', target_col='target_category', amount_col='amount'):
    """
    Creates a Sankey diagram figure from a DataFrame with multiple categories.
    """
    df = df.rename(columns={source_col: 'source', target_col: 'target', amount_col: 'amount'})
    
    all_nodes = pd.concat([df['source'], df['target']]).unique()
    node_indices = {node: idx for idx, node in enumerate(all_nodes)}
    
    df['source_index'] = df['source'].map(node_indices)
    df['target_index'] = df['target'].map(node_indices)
    
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color='black', width=0.5),
            label=all_nodes
        ),
        link=dict(
            source=df['source_index'],
            target=df['target_index'],
            value=df['amount']
        )
    )])

    fig.update_layout(title_text="Budget Allocation Sankey Diagram", font_size=10)
    return fig

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if not file.filename.endswith('.csv'):
        return "Only CSV files are allowed"

    try:
        file.filename = secure_filename(file.filename)
        df = pd.read_csv(file)
    except Exception as e:
        return f"Error reading file: {e}"

    source_col = 'source_category'
    target_col = 'target_category'
    amount_col = 'amount'

    try:
        fig = create_budget_sankey_diagram(df, source_col=source_col, target_col=target_col, amount_col=amount_col)
    except Exception as e:
        return f"Error creating Sankey diagram: {e}"
    
    graph_html = pio.to_html(fig, full_html=False)
    
    return render_template('sankey.html', graph_html=graph_html)

if __name__ == '__main__':
    app.run(debug=False)
