import os
import sys

from flask import Flask, render_template, request, jsonify, redirect, url_for, send_file
from json import dumps

from rng.models.characters import Characters

from rng.web.builders import build_route
from rng.web.defaults import TITLE, HttpMethods

app = Flask(__name__)

_routes = {
    'index': build_route(),
    'npc': build_route('npc'),
    'pc': build_route('pc'),
}

@app.route(_routes['index'], methods=[HttpMethods.GET])
def index():
    html_data = {
        'page_title': TITLE,
    }
    return render_template('index.html', html_data=html_data)

@app.route(_routes['npc'], methods=[HttpMethods.GET])
def npc():
    char = Characters.roll_npc()
    html_data = {
        'page_title': TITLE,
        'character': char.to_json()
    }
    print(html_data)
    return render_template('npc.html', html_data=html_data)


@app.route(_routes['pc'], methods=[HttpMethods.GET])
def pc():
    char = Characters.roll_pc()
    html_data = {
        'page_title': TITLE,
        'character': char.to_json()
    }
    return render_template('pc.html', html_data=html_data)


# @app.route(_routes['filter'], methods=[HttpMethods.POST])
# def filter():
#     MasterHandlerHelper.reload_master()

#     data = get_request_body(request)

#     arg_dict = create_kwargs(data['columns'], sort=data['sort_order'], sort_column=data['sort_column'], case_insensitive=True)
    
#     rows = MasterHandlerHelper.select(**arg_dict)
#     header = MasterHandlerHelper.readable_fieldnames

#     html_data = {
#         'master_table': {
#             'header': header,
#             'rows': rows,
#         }
#     }

#     return jsonify({'data': render_template('master_table_body.html', html_data=html_data), 'count': len(rows)})

def get_request_body(request):
    if request.get_json():
        return request.get_json()
    if request.form:
        return request.form
    if request.data:
        return request.data

if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)  # Run locally in debug
    # app.run(host='0.0.0.0')  # Run on host machine IP
    print('This module is not meant to be run directly. Run the ’server’ module instead using ’python server.py’')
    sys.exit(1)
