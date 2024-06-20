
import os
import openai
import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_DATABASE'),
}

def init_db():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mcq (
            id INT AUTO_INCREMENT PRIMARY KEY,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/generate_mcq', methods=['POST'])
def generate_mcq():
    prompt = request.json['prompt']
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    generated_text = response.choices[0].text.strip()
    # Assume the generated text is in the format "Question: ... Answer: ..."
    question, answer = generated_text.split('Answer:')
    question = question.replace('Question:', '').strip()
    answer = answer.strip()

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO mcq (question, answer) VALUES (%s, %s)', (question, answer))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'message': 'MCQ generated and added successfully'}), 201

@app.route('/add_mcq', methods=['POST'])
def add_mcq():
    question = request.json['question']
    answer = request.json['answer']
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO mcq (question, answer) VALUES (%s, %s)', (question, answer))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'message': 'MCQ added successfully'}), 201

@app.route('/mcqs', methods=['GET'])
def get_mcqs():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('SELECT id, question, answer FROM mcq')
    mcqs = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return jsonify(mcqs)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
    