# from flask import Flask, request, jsonify
# from kafka import KafkaProducer, KafkaConsumer

# app = Flask(__name__)

# producer = KafkaProducer(
#     bootstrap_servers=['kafka:9092'],
#     value_serializer=lambda v: v.encode('utf-8')
# )

# @app.route('/send', methods=['POST'])
# def send_message():
#     message = request.json.get('message')
#     print(message)
#     producer.send('my_topic', message)
#     return "Message sent!", 200

# @app.route('/receive')
# def receive_message():
#     consumer = KafkaConsumer(
#         'my_topic',
#         bootstrap_servers=['kafka:9092'],
#         auto_offset_reset='earliest',
#         value_deserializer=lambda v: v.decode('utf-8'),
#         group_id='my-group'
#     )
#     messages = []
#     for message in consumer:
#         messages.append(message.value)
#         if len(messages) == 10:  # You can adjust this condition
#             consumer.close()
#             break
#     return jsonify(messages)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


from flask import Flask, request, jsonify
from kafka import KafkaProducer, KafkaConsumer
# import joblib
import json

# Load your trained machine learning model
# model = joblib.load('model.joblib')

app = Flask(__name__)

producer = KafkaProducer(
    bootstrap_servers=['kafka1:9092'],
    value_serializer=lambda v: v.encode('utf-8')
)

@app.route('/send', methods=['POST'])
def send_message():
    message = request.json.get('message')
    print(message)
    producer.send('my_topic', message)
    return "Message sent!", 200

@app.route('/receive')
def receive_message():
    consumer = KafkaConsumer(
        'my_topic',
        bootstrap_servers=['kafka1:9092'],
        auto_offset_reset='earliest',
        value_deserializer=lambda v: v.decode('utf-8'),
        group_id='my-group'
    )
    messages = []
    for message in consumer:
        # Assuming each message is a JSON string representing the input data for the model
        input_data = json.loads(message.value)
        # Make a prediction with your model
        # prediction = model.predict([input_data])
        prediction = 0.75
        # Append the prediction to your messages list
        messages.append({'input': input_data, 'prediction': prediction.tolist()})
        print(prediction)
        if len(messages) == 10:  # You can adjust this condition
            consumer.close()
            break
    return jsonify(messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
