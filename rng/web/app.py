import os
import sys

from flask import Flask, render_template, request, jsonify, redirect, url_for, send_file
from json import dumps

from rng.models.characters import Characters
from rng.resources.data.genders import Genders
from rng.resources.data.races import Races
from rng.resources.data.classes import Classes
from rng.resources.data.professions import Professions

from rng.web.builders import build_route
from rng.web.defaults import TITLE, HttpMethods

app = Flask(__name__)

_routes = {
    'index': build_route(),
    'random': build_route('random'),
    'npc': build_route('npc'),
    'pc': build_route('pc'),
}


@app.route(_routes['index'], methods=[HttpMethods.GET])
def index():
    html_data = {
        'page_title': TITLE,
        'genders': Genders.as_list(),
        'races': Races.as_list(),
        'classes': Classes.as_list(),
        'professions': Professions.categories(),
    }
    return render_template('index.html', html_data=html_data)


@app.route(_routes['random'], methods=[HttpMethods.GET, HttpMethods.POST])
def random():
    if request.method == HttpMethods.GET:
        return error()

    data = get_request_body(request)
    character_options = {}
    for k, v in data.items():
        print(f'{k}: {v}')

    character_type = data.get('type')
    if character_type == 'npc':
        character = Characters.roll_npc()
    elif character_type == 'pc':
        character = Characters.roll_pc()
    else:
        character = None

    html_data = {
        'page_title': TITLE,
        'character': character
    }
    return render_template('character.html', html_data=html_data)


@app.route(_routes['npc'], methods=[HttpMethods.GET])
def npc():
    char = Characters.roll_npc()
    html_data = {
        'page_title': f'New NPC: {char.name}',
        'character': char.to_json()
    }
    print(html_data)
    return render_template('character.html', html_data=html_data)


@app.route(_routes['pc'], methods=[HttpMethods.GET])
def pc():
    char = Characters.roll_pc()
    html_data = {
        'page_title': f'New PC: {char.name}',
        'character': char.to_json()
    }
    return render_template('character.html', html_data=html_data)


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


def error():
    return render_template('error.html', html_data={'page_title': TITLE})


if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)  # Run locally in debug
    # app.run(host='0.0.0.0')  # Run on host machine IP
    print('This module is not meant to be run directly. Run the ’server’ module instead using ’python server.py’')
    sys.exit(1)
