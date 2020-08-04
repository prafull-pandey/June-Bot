from functools import wraps
from flask import request, g, abort
from jwt import decode,exceptions
import json

def login_required(funct):
    @wraps(funct)
    def wrap(*args,**kwargs):
        auth=request.headers.get("authorization", None)
        if not auth:
            return json.dumps({'error':'No auth token provided'}),403,{'Content-type': 'application/json'}
        
        try:
            token = auth.split(' ')[1]
            resp=decode(token, None, verify=False, algorithms=['HS256'])
            g.user=resp['sub']
        except exceptions.DecodeError as identifier:
            return json.dumps({'error':'Invalid auth token provided'}),403,{'Content-type': 'application/json'}
        
        return funct(*args, **kwargs)
    return wrap
            