from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            size = int(request.form['size'])

            # Build the matrix dynamically based on size
            matrix = []
            for i in range(size):
                row = []
                for j in range(size):
                    field_name = f'a{i+1}{j+1}'
                    row.append(float(request.form[field_name]))
                matrix.append(row)

            # Compute eigenvalues and eigenvectors
            eigenvalues, eigenvectors = np.linalg.eig(np.array(matrix))

            # Format results
            eigenvalues = eigenvalues.round(4).tolist()
            eigenvectors = eigenvectors.round(4).tolist()

            return render_template(
                'index.html',
                size=size,
                matrix=matrix,
                eigenvalues=eigenvalues,
                eigenvectors=eigenvectors
            )
        except Exception as e:
            return render_template('index.html', error=str(e))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)