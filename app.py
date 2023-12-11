from flask import Flask, render_template, request, jsonify, abort
from __main__ import get_food_data, extract_protein_content, categorize_protein

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_food_data')
def get_food_data_route():
    food_item = request.args.get('food_item')

    data = get_food_data(food_item)
    protein_content = extract_protein_content(data)
    category, category_image = categorize_protein(protein_content)

    return jsonify({'protein_content': protein_content, 'category': category, 'category_image': category_image})


if __name__ == '__main__':
    app.run(debug=True)