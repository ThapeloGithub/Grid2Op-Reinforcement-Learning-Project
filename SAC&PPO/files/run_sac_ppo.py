import os
import sys
from nbconvert import NotebookExporter
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat

def run_notebook(notebook_path):
    # Load the notebook
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)

    # Create an executor
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

    # Execute the notebook
    try:
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})
        print(f"Successfully ran {notebook_path}")
    except Exception as e:
        print(f"Error while executing the notebook: {e}")

if __name__ == "__main__":

    notebook_path = "SAC&PPO/files/sac&ppo.ipynb"
    run_notebook(notebook_path)
