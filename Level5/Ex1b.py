# Python Mentee - Level 5 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 1b - Create a simple local web server with an API endpoint that proxies the TODOs API used above and accepts
#       the "completed" and the "name" filtering. You can use any web framework you prefer.

from flask import Flask, request
import requests


app = Flask(__name__)


@app.route('/query_TODOs')
def query_todos():
    lis = requests.get('https://jsonplaceholder.typicode.com/todos/').json()

    completed = request.args.get('completed')
    name = request.args.get('name')

    html = '<h1>Hot to call this API endpoint</h1>'
    html += '<h2>http://localhost:5000/query_TODOs\
                [?[completed=True|False]&[name= whatever you want to filter the title]] </h2>'
    html += f'<h3>The completed value is: {completed}</h3>'
    html += f'<h3>The name value is: {name}</h3>'

    if not completed and not name:  # no one filled
        ll = lis
    elif completed and not name:
        ll = [d for d in lis if str(d['completed']) == completed]
    elif not completed and name:
        ll = [d for d in lis if name in d['title']]
    else:                           # completed and name filled
        ll = [d for d in lis if str(d['completed']) == completed and name in d['title']]
    for d in ll:
        html += f'<p>{d}</p>'
    return html


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
