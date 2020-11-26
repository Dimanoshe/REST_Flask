from flask import Flask, jsonify, request

app = Flask(__name__)

client = app.test_client()
"""
Тестовый клиент.
Для получения данных - data = client.get('/tutorial')
Для представления данных - data.get_json
Добавление данных - data = client.post('/tutorials', json={'title': 'test'})
Проверка статуса запроса data.status
Изменить данные - data = client.put('/tutorials/2', json={'title': 'test ok'})
Удалить данные - data = client.delete('/tutorials/2')
"""

tutorials = [
    {
        'id': 1,
        'title': 'Video #1. Intro',
        'description': 'GET, POST routes'
    },
    {
        'id': 2,
        'title': 'Video #2. More features',
        'description': 'PUT, DELETE routes'
    }
]


@app.route('/tutorials', methods=['GET'])
def get_list():
    return jsonify(tutorials)


@app.route('/tutorials', methods=['POST'])
def update_list():
    new_one = request.json
    tutorials.append(new_one)
    return jsonify(tutorials)


@app.route('/tutorials/<int:tutorial_id>', methods=['PUT'])
def update_tutorial(tutorial_id):
    '''
        Итератор item проходит по всем словарям из tutorials в поиске tutorial_id, если не находит,
    то следующий элемент - None=
    '''
    item = next((x for x in tutorials if x['id'] == tutorial_id), None)
    params = request.json
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    item.update(params)
    return item


@app.route('/tutorials/<int:tutorial_id>', methods=['DELETE'])
def delete_tutorial(tutorial_id):
    idx, _ = next((x for x in enumerate(tutorials)
                   if x[1]['id'] == tutorial_id), (None, None))

    tutorials.pop(idx)
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
