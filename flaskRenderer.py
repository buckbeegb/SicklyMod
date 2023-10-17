from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_sample_results():
    # Define your sample data with the desired number of rows for each table
    sample_data = [
        {
            'title': 'Sample Point 1',
            'data': [
                {'parameter': 'Parameter 1', 'result': 10},
                {'parameter': 'Parameter 2', 'result': 5},
                # Add more rows as needed
            ]
        },
        {
            'title': 'Sample Point 2',
            'data': [
                {'parameter': 'Parameter A', 'result': 15},
                {'parameter': 'Parameter B', 'result': 8},
                # Add more rows as needed
            ]
        }
        # Add more sample points with custom row data as required
    ]

    return render_template('Lab Sheet.html', sample_data=sample_data)

if __name__ == '__main__':
    app.run()
