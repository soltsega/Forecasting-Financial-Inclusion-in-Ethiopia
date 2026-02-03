import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import sys

# Read notebook
with open('notebooks/03_event_impact_modeling.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Execute
ep = ExecutePreprocessor(timeout=120, kernel_name='python3')

try:
    print("Executing notebook...")
    ep.preprocess(nb, {'metadata': {'path': 'notebooks/'}})
    print("✅ Notebook executed successfully!")
    
    # Save executed notebook
    with open('notebooks/03_event_impact_modeling.ipynb', 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print("✅ Saved executed notebook")
    
except Exception as e:
    print(f"❌ Error during execution: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
