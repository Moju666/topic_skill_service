import os
from flask import Flask, jsonify
from data_manager import JsonDataManager

app = Flask(__name__)
data_manager = JsonDataManager()


DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
TOPICS_FILE = os.path.join(DATA_DIR, 'topics.json')
SKILLS_FILSE = os.path.join(DATA_DIR, 'skills.json')


@app.route('/')
def hello_world():
    return 'Hello from Topic and Skill Service!'


@app.route('/topics', methods=['GET'])
def get_topics():
    topics = data_manager.read_data(TOPICS_FILE)
    return jsonify(topics)


@app.route('/skills', methods=['GET'])
def get_skills():
    skills = data_manager.read_data(SKILLS_FILSE)
    return jsonify(skills)


@app.route('/topics/<id>', methods=['GET'])
def get_topic_by_id(id):
    topics =data_manager.read_data(TOPICS_FILE)
    found_topics =[t for t in topics if t ['id'] == id]
    topics = found_topics[0] if found_topics else None

    #topics = data_manager.read_data(TOPICS_FILE)
    #topic = [t for t in topics if t['id'] == id][0] #es gibt nur eine Liste daher Null 
    #topic = next((topic for topic in topics if topic.get('id') == id), None)
    return jsonify(topic)

if __name__ == '__main__':
    app.run(debug=True, port=5000)