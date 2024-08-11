from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_scores', methods=['POST'])
def calculate_scores():
    data = request.json
    fine_tuning_score = sum([
        int(data['nature_of_task']) * 0.3,
        int(data['upfront_cost']) * 3,
        int(data['ongoing_cost']) * 0.1,
        int(data['scalability']) * 0.1,
        int(data['real_time_updates']) * 0.1,
        int(data['accuracy_relevance']) * 0.3,
        int(data['data_privacy']) * 0.1,
        int(data['maintenance']) * 0.1
    ])
    
    rag_score = sum([
        int(data['nature_of_task']) * 0.1,
        int(data['upfront_cost']) * 1,
        int(data['ongoing_cost']) * 0.3,
        int(data['scalability']) * 0.1,
        int(data['real_time_updates']) * 0.3,
        int(data['accuracy_relevance']) * 0.3,
        int(data['data_privacy']) * 0.05,
        int(data['maintenance']) * 0.05
    ])
    
    return jsonify({
        'fine_tuning_score': fine_tuning_score,
        'rag_score': rag_score
    })

if __name__ == '__main__':
    app.run(debug=True)
