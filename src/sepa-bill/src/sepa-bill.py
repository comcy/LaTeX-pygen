from jinja2 import Template

# Define the LaTeX template
latex_template = r"""
\documentclass{article}
\begin{document}


\section*{My Document}

Hello, {{ name }}!

This is a LaTeX document with parameters. Here's a parameter value: {{ parameter_value }}.

\end{document}
"""

# Create a Jinja2 template
template = Template(latex_template)

# Define the parameters you want to include in the LaTeX document
params = {
    'name': 'John Doe',
    'parameter_value': '42',
}

# Render the LaTeX document with the parameters
latex_document = template.render(params)

# Write the LaTeX document to a .tex file
with open('output.tex', 'w') as f:
    f.write(latex_document)

print("LaTeX document has been generated as 'output.tex'.")
