import ipywidgets as widgets
from IPython.display import display
import pandas as pd

# Create a file dialog widget
file_dialog = widgets.FileUpload()

# Display the file dialog widget
display(file_dialog)

# Wait for the user to select a file
while not file_dialog.value:
    pass

# Get the uploaded file
uploaded_file = file_dialog.value[0]

# Read the file into a pandas DataFrame
df = pd.read_csv(uploaded_file)

# Display the DataFrame
df