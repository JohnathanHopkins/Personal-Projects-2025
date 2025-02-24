import tkinter as tk
import plotly.graph_objects as go
import plotly.io as pio

# Create a Plotly figure
fig = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[4, 1, 3])])

# Convert the Plotly figure to HTML
html_string = pio.to_html(fig, full_html=False)

# Create the Tkinter window
root = tk.Tk()

# Embed the Plotly graph in a Tkinter Label widget
label = tk.Label(root, text=html_string)
label.pack()

# Start the Tkinter event loop
root.mainloop()