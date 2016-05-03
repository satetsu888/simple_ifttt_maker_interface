from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MenuModel,
    )

import json
import urllib.request

import configparser

config = configparser.ConfigParser()
config.read('user.conf')

@view_config(route_name='list', renderer='templates/list.pt')
def list(request):
    return {}

@view_config(route_name='menus', renderer='json')
def menus(request):
    menus = DBSession.query(MenuModel).all()
    return {"data": [ menu.toDict() for menu in menus]}

@view_config(route_name='fire', renderer='json')
def fire(request):

    key = config["ifttt"]["maker_key"]

    url = 'https://maker.ifttt.com/trigger/' + request.params["action"] + '/with/key/' + key
    print(url)
    data = {
        "value1": request.params["value1"],
        "value2": request.params["value2"],
        "value3": request.params["value3"],
    }
    req = urllib.request.Request(
            url,
            data=json.dumps(data).encode('utf8'),
            headers={'content-type': 'application/json'},
    )
    from pprint import pprint
    pprint(req)
    response = urllib.request.urlopen(req)

    pprint(response)

    return {}
